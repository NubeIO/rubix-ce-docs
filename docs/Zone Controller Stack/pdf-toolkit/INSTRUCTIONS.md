# PDF Build Toolkit

Turns manual Markdown into branded, print-ready client PDFs. This folder is
self-contained and reusable: everything product-specific lives in
`project.toml`, and everything brand-specific lives in a skin stylesheet, so
pointing it at another product or OEM is a config change rather than a code
change. See "Reusing the toolkit" in the repo README.

Currently configured for the Zoneconnex guides in the anywAiR / Fujitsu General
brand.

**Source of truth:** the manual `.md` files in `docs/Zone Controller Stack/` are the
single source — they are ALSO the live website pages. The PDFs are generated *from*
them for the client and are not served on the website. Never edit the PDFs by hand;
change the `.md` and rebuild.

## What's in this folder

| File | Purpose |
|------|---------|
| `project.toml` | **What to build.** Guide list, cover titles/subtitles/images, model number, per-guide TOC opt-out, PDF-only intro copy, and which skin to use. The only file that names a product — edit this, not the scripts. |
| `brand.py` | The converter. Rewrites the website-flavoured Markdown into the print-ready form the CSS expects (unwraps Docusaurus `require()` images, tags inline icons, groups phone screenshots into rows, wraps pin tables, fixes list/code-block issues, injects the cover + back page). Reads `project.toml`; names no document itself. |
| `engine.css` | Layout and structure — page furniture, headings, lists, tables, callouts, cover/back-page geometry, TOC. **Brand-neutral:** no colours, no font names. |
| `anywair-skin.css` | The anywAiR brand layer — palette, typeface, callout/table fills, cover chrome. Copy this to add another OEM. |
| `page-a4.css` / `page-a5.css` | Page size, margins, type scale, image scale. Pick exactly one. |
| `_page-template.css` | Blank page file to copy when adding a new format. |
| `insert-toc.lua` | Pandoc filter that auto-builds the clickable Table of Contents after the cover. |
| `compress.py` | Post-pass image compression (PyMuPDF: cap 1800px, JPEG q82, white-composite). |
| `assets/` | Cover/logo images referenced from `project.toml` (`logos/anywair-logo.svg`, `images/zc-cover.png`). |
| `INSTRUCTIONS.md` | This file. |

> This whole `pdf-toolkit/` folder is excluded from the Docusaurus site build, so
> none of it (including this file) becomes a web page.

---

## 1. Prerequisites (macOS)

```bash
brew install pandoc
pip install weasyprint
# WeasyPrint needs these native libs; install if missing:
brew install glib pango cairo gdk-pixbuf fontconfig harfbuzz
```

- **Pandoc** stitches the Markdown + Lua filter together.
- **WeasyPrint** is the PDF engine that reads the CSS layers and paints the pages.
- **Python 3.11+** is required — `brand.py` and `build.sh` read `project.toml`
  with the stdlib `tomllib`. The pinned venv (`.venv/`) is 3.12.

---

## 2. Build — use `build.sh` (the one canonical command)

**Always build with `pdf-toolkit/build.sh`.** It is the single source of truth for
the recipe — it copies the folder to a throwaway temp dir, runs `brand.py`, calls
pandoc + weasyprint with the right CSS, compresses images, and copies the finished
PDF into `pdfs/`. Do NOT hand-assemble pandoc commands: that is how PDFs drifted
back to the old spread-out format. `brand.py` rewrites `.md` in place, which is why
the script always works on a copy — never run it against the source folder.

```bash
# from the repo root OR from this "Zone Controller Stack" folder:
pdf-toolkit/build.sh                                  # all guides — A5 (print deliverable), no TOC
pdf-toolkit/build.sh --a4                             # all guides — A4 (screen/desk reference)
pdf-toolkit/build.sh --toc                            # A5, with a Table of Contents page
pdf-toolkit/build.sh --a4 "Zoneconnex Quick Start Guide"    # just one guide
pdf-toolkit/build.sh --size a5 --toc "Zoneconnex INSTALL & USER MANUAL"
```

**Page size is an argument, and A5 is the default.** A5 is the print
deliverable and is *built* at A5 — nothing is ever shrunk to reach a format.
A4 is screen/desk reference only. Every output filename ends in `-A4` or
`-A5`; there are deliberately no unsuffixed PDFs, so nobody has to open a
file to find out what size it is.

The CSS chain is, in load order (later layers win by cascade):

| Layer | File | Holds |
|---|---|---|
| engine | `engine.css` | layout + structure. No colours, no fonts, no page dimensions. |
| skin | `anywair-skin.css` | colour, typeface, cover chrome. Set by `[brand].css` in `project.toml`. |
| page size | `page-a4.css` / `page-a5.css` | page size, margins, type scale, image scale |

Page size comes from the CSS `@page` rule only — there is no `-V papersize`
flag, so the two can never disagree. To add a format, copy
`_page-template.css` to `page-<name>.css`, fill in the values, and add a row
to the format registry in the repo README. Read the floors at the top of the
template first: 9pt body, 10mm margins, ~40mm images. When a format hits a
floor the answer is less content per page, more pages — never smaller type.

**Print density is built in.** Numbered `# H1`s no longer force a fresh page
(title + intro + first section flow together), images sit at reference
density, and spacing is tighter. These were previously a separate
`anywair-print.css` override layer; they are now density variables in the
page-size files, so each format sets its own rhythm.

**The Table of Contents is OPTIONAL** — off by default, added with `--toc` (which
switches on `insert-toc.lua`).

Compression is `compress.py` (run automatically as the last build step): composites
transparency onto white, caps the long edge at 1800 px, re-encodes JPEG q82.

Eyeball each PDF (cover, footer page numbers, screenshot rows, pin tables) before
handing it to the client. To preview a page as an image without opening Preview:
`qlmanage -t -s 1100 -o /tmp "some.pdf"`.

### Ground truth — verified, please don't re-derive

These were each established by a regression that page count alone did not catch.

- **Percentage image widths only work when the containing block is the text
  column.** Inside `<td>`/`<th>` and inside the `.img-row` flex rows `brand.py`
  generates, a percentage resolves against the cell or flex item and collapses
  images to 16–28mm, under the ~40mm legibility floor. `--img-cell`,
  `--img-phone`, `--img-qr` and `--img-app-qr` are absolute lengths for this
  reason.
- **`.cover` is full-bleed.** Its `@page` has zero margin, so it must span the
  whole sheet. The text column is pinned via
  `body > *:not(.cover):not(.back-page)`, *not* on `body` itself — a body-level
  width pushes the cover's border off the right edge of the page.
- **Density lives in the page files** (`--h1-break`, `--p-margin`,
  `--figure-margin`, `--orphans`, …), not in a separate override layer. If a
  build ever looks too loose or too sparse, check those variables first.
- **A5 is not A4 scaled by 0.707.** Its type scale was set to match the
  effective printed size of the approved originals. Deriving one format's scale
  from another's reproduces the oversized-text problem the page-size layer
  exists to remove.
- **Screenshot row count is a capacity limit, not a preference.** A5 genuinely
  cannot carry three phones per row: 3-up would need ≤36.6mm each, under the
  40mm floor. `SCREENSHOTS_PER_ROW` in `brand.py` is the counterpart to
  `--img-phone` in the page file — keep the two in step.

---

## 3. What `brand.py` does (so you can predict the output)

Run automatically by the command above. Passes 1–2 below run once over the whole
build copy; the rest are applied per manual page:

0. **`flatten_transparent_pngs`** *(runs once, on the whole build copy)* — composites
   **every** transparent PNG onto a WHITE background. Many product renders, LCD
   screenshots and icons are transparent RGBA; WeasyPrint / the image compressor can
   otherwise composite them onto BLACK, giving the "product on a black box" bug
   (covers were the worst offender). Flattening happens only in the throwaway build
   copy, so the source PNGs — which the website also serves — stay transparent and
   untouched. This fixes every current and future transparent image at once.
1. **`fix_require`** — Docusaurus `<img src={require("./x.png").default}>` → plain `<img src="x.png">` (Pandoc can't resolve `require`).
1b. **strip emoji variation selector (U+FE0F)** — browsers render `⚠️`/`ℹ️` as one colour glyph, but WeasyPrint renders the trailing U+FE0F as a stray bullet/pilcrow next to callout emoji. Removing it leaves the plain `⚠` / `ℹ` symbol. (Source `.md`/website keep the full emoji.)
2. **`rasterize_svgs`** — converts every `LCD-Screenshots/*.svg` to PNG (`*.from-svg.png`)
   in the build copy and rewrites the ref. WeasyPrint will not scale these SVGs up to a
   CSS width, so SVG screenshots render at an inconsistent intrinsic size next to the
   PNG ones. Rasterizing makes them all size uniformly via the `.lcd` class. A distinct
   `.from-svg.png` suffix is used so an existing (possibly differently-annotated) PNG of
   the same base name is never overwritten. Source `.md` / website `.svg` refs unaffected.
3. **`normalize_and_tag_icons`** — restores the store-badge width cap, removes the `![max800px](…)` alt-text size hack, and tags inline UI glyphs with `{.icon}` so they sit inline at text height. Detection is **automatic by image size**: any PNG ≤ 64×64px is treated as an icon — no list to maintain, new icons just work.
4. **`wrap_diagram_tables`** — wraps pin/connector tables (blank or image-only header row) in `::: diagram-table :::` so they drop the teal header bar and shrink to ~95mm.
5. **`group_screenshots`** — tags phone screenshots `{.phone}` and packs consecutive ones into `<div class="img-row">` rows; a lone screenshot becomes a `{.phone}` single. **The row size is per page format** — 3 at A4, 2 at A5 — because three phones do not fit inside the A5 column (see `SCREENSHOTS_PER_ROW` in `brand.py`). Screenshots render at `--img-phone` from the page file: 54mm at A4, 46mm at A5.
6. **`fix_orphan_code_blocks`** — flattens deep (4+ space) list bullets so Pandoc doesn't mis-parse a bullet that follows an image block as an overflowing code block.
7. **cover + back page** — drops the doc's first `# H1` and injects the branded cover, then appends the copyright back page.

Icons are detected automatically by image size (≤ 64×64px) — there is no icon list
to maintain. To tweak that threshold, screenshot columns, or cover text, edit the
constants near the top/bottom of `brand.py` (`ICON_MAX_PX`, `SCREENSHOTS_PER_ROW`, `COVER_INSTALL`, `COVER_MIA`).

**LCD TouchPoint screenshots — one consistent size across guides:** tag each with
the **alt-text tag `![lcd](…)`** in the `.md`. `brand.py` converts it to `{.lcd}` at
build time; the `.lcd` CSS class then forces a single fixed width (120mm) for both
raster PNGs and the SVGs rasterized by pass 2, so the same screen never renders at
different sizes between the Quick Start and User guides. To change that width, edit
the `img.lcd` rule in `engine.css`.

> **IMPORTANT — the `.md` is ALSO the live website (Docusaurus).** Never write bare
> Pandoc attributes like `{.lcd}`, `{.large}`, or `{width=…}` directly in the `.md`:
> Pandoc understands them, but **Docusaurus prints the braces as literal text on the
> web page**. Instead put the hint in the **alt text**, which is invisible on the
> website, and let `brand.py` translate it for the PDF:
>
> | Author in the `.md` (web-safe) | brand.py emits for the PDF |
> |--------------------------------|----------------------------|
> | `![lcd](x)`                    | `![](x){.lcd}` — fixed 120mm LCD screenshot |
> | `![large](x)`                  | `![](x){.large width=80%}` — wide diagram at 80% |
> | `![max800px](x)`               | `![](x)` — hint stripped, default 108mm |

---

## 4. Authoring reference — classes the CSS provides

You normally don't hand-write these (brand.py adds them), but for reference:

- `{.phone}` — phone-screenshot sizing (`--img-phone`, an **absolute** length: 54mm at A4, 46mm at A5). Rows: wrap figures in `<div class="img-row">`, 3 per row at A4 and 2 at A5.
- `{.icon}` — inline button glyph at text height.
- `::: diagram-table … :::` — compact wiring/pin table, white header, 55% of the column.
- Callouts: blockquote starting `**Please note:**` (accent) / `**Warning:**` (amber) / `**Danger:**` (red).
- Every `# H1` starts a new page automatically; `<div class="page-break"></div>` forces one elsewhere.

### Image size tiers

Percentages of the text column. **A4 and A5 use the same percentages**, so an
image occupies the same fraction of the page at both sizes and reads at the
same visual weight. Change a tier in one page file, change it in the other.

| Class | % of column | A4 (col 174mm) | A5 (col 122mm) |
|---|---|---|---|
| `{.small}` | 38% | 66mm | 46mm |
| `{.medium}` | 58% | 101mm | 71mm |
| *(none — default)* | 88% | 153mm | 107mm |
| `{.lcd}` | 78% | 136mm | 95mm |
| `{.large}` | 100% (full column) | 174mm | 122mm |

**Percentages only work when the containing block is the text column.** Inside
`<td>`/`<th>` and inside `.img-row` flex rows, a percentage resolves against the
cell or flex item and collapses the image to 16–28mm — under the ~40mm
legibility floor. `--img-cell`, `--img-phone`, `--img-qr` and `--img-app-qr` are
therefore **absolute lengths** in each page file. Don't "tidy" them into
percentages.

---

## 5. Editing the design

Pick the layer that matches what you're changing:

| Changing… | Edit |
|---|---|
| Which guides build, cover text/images, model no., TOC opt-outs | `project.toml` |
| A colour, the typeface, cover chrome | `anywair-skin.css` |
| Spacing, breaking, structure, a new rule | `engine.css` |
| Page size, margins, type scale, image tiers | `page-a4.css` / `page-a5.css` |
| The Markdown→print transform itself | `brand.py` |

Then re-run the build in section 2 and commit the regenerated PDFs alongside
your changes.

**Before and after any change, capture a baseline and diff it** — page counts,
per-image rendered widths, and extracted word counts. Image widths are the
sensitive signal; they catch regressions that page count alone misses.

```bash
./pdf-toolkit/build.sh --a4 --toc && cp pdfs/*-A4.pdf /tmp/baseline/
# ...make changes...
./pdf-toolkit/build.sh --a4 --toc
# then compare
```
