# Zoneconnex / MIA PDF Build Toolkit

Everything needed to turn the Zoneconnex and MIA manual Markdown into the branded
anywAiR / Fujitsu General client PDFs. This folder is self-contained.

**Source of truth:** the manual `.md` files in `docs/Zone Controller Stack/` are the
single source — they are ALSO the live website pages. The PDFs are generated *from*
them for the client and are not served on the website. Never edit the PDFs by hand;
change the `.md` and rebuild.

## What's in this folder

| File | Purpose |
|------|---------|
| `brand.py` | The converter. Rewrites the website-flavoured Markdown into the print-ready form the CSS expects (unwraps Docusaurus `require()` images, tags inline icons, groups phone screenshots into rows, wraps pin tables, fixes list/code-block issues, injects the cover + back page). |
| `anywair-brand.css` | The brand print stylesheet — cover page, TOC, callouts, phone-screenshot sizing, diagram/pin tables, A4 setup, footer page numbers. |
| `insert-toc.lua` | Pandoc filter that auto-builds the clickable Table of Contents after the cover. |
| `assets/` | Cover/logo images used by the CSS cover (`logos/anywair-logo.svg`, `images/zc-cover.png`). |
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
- **WeasyPrint** is the PDF engine that reads `anywair-brand.css` and paints the pages.

---

## 2. Build (do NOT run against the source folder)

`brand.py` rewrites `.md` files **in place**, so always run it on a **copy** of the
`Zone Controller Stack` folder, then copy the finished PDFs back.

```bash
# From repo root. TMP is a throwaway copy of the manual folder.
TMP="$(mktemp -d)/Zone Controller Stack"
cp -R "docs/Zone Controller Stack" "$TMP"

# 1) Rewrite the Markdown into print-ready form (cover, icons, screenshot rows, tables…).
python3 "$TMP/pdf-toolkit/brand.py" "$TMP"

# WeasyPrint on macOS can't find Homebrew's libgobject unless this is set:
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib"

# 2a) Build the Install Guide (run from the folder root).
( cd "$TMP" && pandoc "Zoneconnex Install Guide.md" \
    -o "Zoneconnex Install Guide.pdf" \
    --pdf-engine=weasyprint \
    --css=pdf-toolkit/anywair-brand.css \
    --lua-filter=pdf-toolkit/insert-toc.lua \
    --standalone )

# 2b) Build the MIA manual (run from the MIA subfolder; toolkit is one level up).
( cd "$TMP/MIA Mobile App" && pandoc "MIA App User Manual.md" \
    -o "MIA App User Manual.pdf" \
    --pdf-engine=weasyprint \
    --css=../pdf-toolkit/anywair-brand.css \
    --lua-filter=../pdf-toolkit/insert-toc.lua \
    --standalone )

# 3) Copy the finished PDFs back next to the source.
cp "$TMP/Zoneconnex Install Guide.pdf" "docs/Zone Controller Stack/"
cp "$TMP/MIA Mobile App/MIA App User Manual.pdf" "docs/Zone Controller Stack/MIA Mobile App/"
```

Eyeball each PDF (cover, TOC, footer page numbers, phone-screenshot rows, pin
tables) before handing it to the client. To preview a page as an image without
opening Preview: `qlmanage -t -s 1100 -o /tmp "some.pdf"`.

---

## 3. What `brand.py` does (so you can predict the output)

Run automatically by the command above. Each pass is applied to the manual pages:

1. **`fix_require`** — Docusaurus `<img src={require("./x.png").default}>` → plain `<img src="x.png">` (Pandoc can't resolve `require`).
2. **`normalize_and_tag_icons`** — removes the `![max300px](…)` / `![max800px](…)` alt-text size hack, and tags known inline UI glyphs (plus, minus, chevron, tick, power, …) with `{.icon}` so they sit inline at text height.
3. **`wrap_diagram_tables`** — wraps pin/connector tables (blank or image-only header row) in `::: diagram-table :::` so they drop the teal header bar and shrink to ~95mm.
4. **`group_screenshots`** — tags phone screenshots `{.phone}` and packs consecutive ones into `<div class="img-row">` **rows of 3**; a lone screenshot becomes a `{.phone}` single. All screenshots render at a fixed 55mm.
5. **`fix_orphan_code_blocks`** — flattens deep (4+ space) list bullets so Pandoc doesn't mis-parse a bullet that follows an image block as an overflowing code block.
6. **cover + back page** — drops the doc's first `# H1` and injects the branded cover, then appends the copyright back page.

To tweak the icon list, screenshot columns, or cover text, edit the constants near
the top/bottom of `brand.py` (`ICON_NAMES`, `per_row=3`, `COVER_INSTALL`, `COVER_MIA`).

---

## 4. Authoring reference — classes the CSS provides

You normally don't hand-write these (brand.py adds them), but for reference:

- `{.phone}` — phone-screenshot sizing (fixed 55mm). Rows: wrap figures in `<div class="img-row">`.
- `{.icon}` — inline button glyph at text height.
- `{.small}` (55mm) / `{.medium}` (90mm) / `{.large}` (full width) — generic image sizes.
- `::: diagram-table … :::` — compact wiring/pin table, white header, ~95mm wide.
- Callouts: blockquote starting `**Please note:**` (teal) / `**Warning:**` (amber) / `**Danger:**` (red).
- Every `# H1` starts a new page automatically; `<div class="page-break"></div>` forces one elsewhere.

---

## 5. Editing the design

1. Edit `anywair-brand.css` (styling) or `brand.py` (structure) here in `pdf-toolkit/`.
2. Re-run the build in section 2.
3. Commit the regenerated PDFs alongside your changes.
