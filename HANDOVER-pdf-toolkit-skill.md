# Handover: turning the PDF toolkit into a reusable skill

Written 2026-08-06 from the session that refactored `docs/Zone Controller Stack/pdf-toolkit/`
into a four-layer document system. Branch `cleanup/zone-controller-stack`.

**Purpose of this document:** everything the next person (or agent) needs to
package this toolkit as a Claude Code skill and use it in another repo. It is
deliberately blunt about what is genuinely reusable and what is still welded to
this project — the second list is the real work.

---

## 1. What exists right now

`docs/Zone Controller Stack/pdf-toolkit/` builds branded, print-ready PDFs from
Markdown via Pandoc + WeasyPrint. It is now four layers, each with one job:

| Layer | File | Holds | Portable? |
|---|---|---|---|
| **What** | `project.toml` | guide list, cover titles/subtitles/images, model no., per-guide TOC opt-out, PDF-only intro copy, which skin to load | Template it |
| **Structure** | `engine.css` (25 KB) | layout, page furniture, headings, tables, callouts, cover/back geometry, TOC | **Yes, as-is** |
| **Brand** | `anywair-skin.css` (2.8 KB) | palette, typeface, table/callout fills, cover chrome | Copy per OEM |
| **Format** | `page-a4.css`, `page-a5.css`, `_page-template.css` | page size, margins, type scale, image tiers | **Yes, as-is** |

Plus the machinery: `build.sh` (orchestrator), `brand.py` (Markdown→print
transform), `compress.py` (image compression), `insert-toc.lua` (TOC filter).

CSS load order is **engine → skin → page**; later layers win by cascade.

### The key invariant

`engine.css` contains **zero raw colours and zero font names** — every such value
is a `var()` the skin supplies. This is what makes a second brand cheap. Enforce it:

```bash
# must print nothing but the header warning line
grep -nE '#[0-9A-Fa-f]{3,6}|Arial|Courier' engine.css | grep -v '^8:'
```

The 19 tokens a skin must define are listed in the `engine.css` header.

### Proven, not assumed

- **Skin swap works.** Built the User Start Guide with a throwaway skin (two
  `sed` substitutions: teal→purple, Arial→Georgia). Every heading, table header
  and callout changed; layout was untouched. No engine edit.
- **The refactor changed no output.** All six PDFs (3 guides × A4/A5) render
  identically to the pre-refactor baseline — same page counts, word counts, and
  per-image rendered widths.

---

## 2. What is NOT portable yet — read this before scoping

This is the honest list. Anyone who copies `pdf-toolkit/` into a new repo hits
these immediately.

### 2.1 `brand.py` is coupled to *this* content, not just this brand

Despite the manifest, `brand.py` still hardcodes content-specific rules:

| Line(s) | What | Why it's a problem elsewhere |
|---|---|---|
| `fix_require` | unwraps Docusaurus `<img src={require("./x").default}>` | Docusaurus-only. Harmless but dead in a non-Docusaurus repo |
| `rasterize_svgs` | matches path substring `LCD-Screenshots/` | Another project's SVGs live elsewhere and are silently skipped |
| QR handling | matches `onlinedocs-qr-code.png`, `googleplay-qr-code`, `Andriod-anywair-zone-qr-code`, `iOS-…` by filename | Pure Zoneconnex. Any other project's QRs get default sizing and blow up to ~105mm |
| `group_screenshots` | matches path substring `screenshots/` | Ditto — phone-row packing silently does nothing |
| `BACK_PAGE` | hardcoded company name, URLs, phone number | Fujitsu General AU/NZ contact details baked into the constant |

**These are the real work.** They should become manifest patterns, e.g.:

```toml
[patterns]
svg_rasterize = ["LCD-Screenshots/"]
screenshot_rows = ["screenshots/"]
doc_qr   = ["onlinedocs-qr-code.png"]
app_qr   = ["googleplay-qr-code", "-anywair-zone-qr-code"]

[back_page]
company = "General Australia Pty Ltd"
links   = [["www.generalairstage.com.au", "https://..."], ...]
contact = "contact@fujitsugeneral.com.au | 1300 882 201"
```

Until that's done, the toolkit is portable **across brands** but not really
**across content shapes**.

### 2.2 Single asset root

`brand.py` has one `TOOLKIT_REL = "pdf-toolkit"` prefix. Guides in a subfolder
(the MIA Mobile App manual is the live example) need paths resolving one level
up. **MIA is deliberately absent from `project.toml` for this reason** — adding
it needs a per-guide asset root, not just a new `[[guides]]` block.

### 2.3 Environment

- **Python 3.11+ required** — `tomllib` is stdlib from 3.11. The pinned venv is 3.12.
- **WeasyPrint needs Homebrew Python on macOS**, not system Python. `build.sh`
  sets `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` and puts the venv first on
  `PATH`. Without this it fails on libgobject.
- Native libs: `brew install pandoc glib pango cairo gdk-pixbuf fontconfig harfbuzz`
- Python deps: `weasyprint`, `pymupdf`, `pillow` (the `.venv/` is 117 MB — **do
  not vendor it into a skill**; make it a setup step).
- `assets/` is 6.4 MB of Anywair logo + cover images — brand-specific, replace it.

---

## 3. Recommended skill design

### Scope it as a *workflow* skill, not a code drop

The toolkit is ~90 KB of code + CSS. A skill shouldn't inline it. Two options:

**Option A — skill teaches, repo carries the toolkit (recommended).**
The skill contains the architecture, the invariants, the verification method,
and the setup steps. It tells the agent to copy `pdf-toolkit/` from a known
source (this repo, or a extracted standalone repo) and adapt it. Keeps the skill
small and lets the toolkit version independently.

**Option B — skill bundles the toolkit.**
Ship `engine.css`, the page files, `_page-template.css`, `build.sh`, `brand.py`,
`compress.py`, `insert-toc.lua` and a `project.toml` template as skill resources.
Self-contained, but you now maintain two copies unless the skill *is* the
upstream.

Either way, **do not bundle** `.venv/`, `assets/`, or `anywair-skin.css` (that's
one OEM's brand — ship it as an example, clearly labelled).

### Suggested skill layout

```
pdf-guide-build/
  SKILL.md                     # when to use, the 4-layer model, the invariant
  references/
    architecture.md            # layer responsibilities, load order, token list
    porting.md                 # §2 of this doc — what to unpick per new repo
    verification.md            # baseline/diff method below
  assets/
    project.toml.template
    _page-template.css
    example-skin.css
```

### What SKILL.md must say

1. **When to trigger** — building/branding print PDFs from Markdown; adding an
   OEM skin; adding a page format; debugging image sizing in a PDF build.
2. **The four layers and load order** (table above).
3. **The invariant** — engine has no colours/fonts; adding a brand = new skin
   file + one `project.toml` line; if a brand can't be expressed in tokens, *add
   a token*, don't fork the engine.
4. **The verification protocol** (§4) — non-negotiable before/after any change.
5. **The ground truth in §5** — these were each learned from a regression.

---

## 4. Verification protocol — put this in the skill verbatim

Every change to the toolkit must be diffed against a baseline. **Page count
alone is not sufficient** — it missed regressions that image widths caught.

```bash
# 1. baseline BEFORE touching anything
./pdf-toolkit/build.sh --a4 --toc && cp pdfs/*-A4.pdf /tmp/baseline/
./pdf-toolkit/build.sh --a5 --toc && cp pdfs/*-A5.pdf /tmp/baseline/

# 2. make changes, rebuild both formats

# 3. diff metrics: pages, words, per-image rendered widths
```

Metrics script (PyMuPDF; the venv has it — poppler CLI is *not* installed):

```python
import sys, fitz, collections
for path in sys.argv[1:]:
    d = fitz.open(path)
    words = sum(len(p.get_text().split()) for p in d)
    widths = [round((b["bbox"][2]-b["bbox"][0])/72*25.4)
              for p in d for b in p.get_image_info()]
    print(f"{path.split('/')[-1]}\n  pages={len(d)} words={words} images={len(widths)}")
    print("  widths(mm):", dict(sorted(collections.Counter(widths).items())))
    print(f"  under-40mm: {len([w for w in widths if w < 40])}\n")
```

Also check no blank pages and no image overflowing its page box. Then `sort`
both metric dumps and `diff` — sorting matters, or shell glob order creates
phantom differences.

**A pure refactor must produce a zero diff.** If it doesn't, that's a bug in the
refactor, not a design question.

Note: PDFs are **not** byte-reproducible (embedded timestamps/object IDs), so
`git diff` always shows all six as modified after any rebuild. Judge by rendered
metrics, never by file bytes.

---

## 5. Ground truth — verified, do not re-derive

Each of these was learned from a regression.

- **Percentage image widths only work when the containing block is the text
  column.** Inside `<td>`/`<th>` and inside `.img-row` flex rows, a percentage
  resolves against the cell/flex item and collapses images to 16–28mm, under the
  ~40mm legibility floor. So `--img-cell`, `--img-phone`, `--img-qr`,
  `--img-app-qr` are **absolute lengths** per page file. Don't "tidy" them into
  percentages.
- **`.cover` is full-bleed.** Its `@page` has zero margin. The text column is
  pinned via `body > *:not(.cover):not(.back-page)`, *not* on `body` — a
  body-level width pushes the cover border off the sheet.
- **A4 and A5 share image-tier percentages** (38/58/88/78%) so an image reads at
  the same visual weight on both. A4 previously used 32/47/47/52%, which made
  images look half-size against the bigger sheet. Change a tier in one page file,
  change it in the other.
- **A5 is not A4 × 0.707.** Its type scale matches the effective printed size of
  the approved originals. Deriving one format from another reproduces the
  oversized-text problem the page layer exists to remove.
- **Screenshot row count is a capacity limit.** A5 cannot carry 3 phones/row:
  3-up needs ≤36.6mm each, under the 40mm floor. `SCREENSHOTS_PER_ROW` in
  `brand.py` is the counterpart to `--img-phone` — keep them in step.
- **Density lives in the page files** (`--h1-break`, `--p-margin`, `--orphans`, …).
  A build that looks too loose or sparse: check those first.
- **Floors that never scale:** 9pt body, 10mm margins, +3mm gutter on the bound
  edge, ~40mm images. When a format hits a floor the answer is **more pages**,
  never smaller type.
- **Source `.md` files are also live website pages.** PDF-only content (covers,
  intros, `{.class}` attributes) must stay out of the `.md` and live in
  `project.toml` / `brand.py` / CSS.

---

## 6. Suggested build order for the skill

1. **Extract the toolkit to a standalone repo** — resolves "which copy is
   canonical" before it becomes a problem.
2. **Unpick §2.1** — move the hardcoded path/filename patterns and the back-page
   contact block into `project.toml`. Biggest single portability win.
3. **Add a per-guide asset root** (§2.2), then add MIA as the proof it works.
4. **Write SKILL.md + references** from §§1, 3, 4, 5 of this document.
5. **Validate on a genuinely different repo** — a non-Docusaurus one, different
   brand, different content shape. That's the only real test.

Step 2 is where the effort is. Steps 1, 4, 5 are mostly mechanical.

---

## 7. State at handover

- Committed: `b957f05` — A4 image tiers matched to A5 (the change that *did*
  alter the PDFs: manual 42→52 pp, quick start 13→18, user start 9→10).
- **Uncommitted:** the whole four-layer refactor — `project.toml`, `engine.css`,
  `anywair-skin.css` (new); `build.sh`, `brand.py`, `README.md`,
  `INSTRUCTIONS.md`, `page-a4.css`, `page-a5.css`, `_page-template.css`,
  `src/css/custom.css` (modified); `anywair-brand.css` (deleted); six rebuilt
  PDFs (rendering unchanged, bytes differ).
- `HANDOVER-page-size.md` deleted, content folded into README + INSTRUCTIONS.
- `HANDOVER-cleanup.md` **kept** — unrelated unfinished task (file/asset hygiene,
  ~40 MB duplicated `Zoneconnex-Guides-v1.4-build/`, open decisions on which old
  PDFs to delete). Not superseded by any of this.
- `npm run build` passes. Website unaffected.

### Still open, needs the team

- Manual §6.5 "Insert Alerts List" placeholder.
- USG p5/p6/p7 images (@bja).
- Whether the enlarged A4 needs re-approval — it supersedes the previously
  approved A4 density.
