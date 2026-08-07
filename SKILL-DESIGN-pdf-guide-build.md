# Design: a brand-agnostic, content-agnostic PDF guide skill

Target: a skill that builds branded print PDFs from Markdown for **any brand**
and **any content shape** — not just Zoneconnex/anywAiR. This document is the
spec for that skill, plus the refactor that has to land underneath it.

Written 2026-08-06. Supersedes the staged plan in `HANDOVER-pdf-toolkit-skill.md`
§6, which treated content-generalisation as a follow-up. Here it is the core.

---

## 1. The insight that makes this possible

Every content-coupled rule in `brand.py` today reduces to **one** of four shapes:

| Shape | Today (hardcoded) | Generalised |
|---|---|---|
| *images matching a pattern get a CSS class* | `onlinedocs-qr-code.png` → `.doc-qr`; `*qr-code.png` → `.app-qr`; badge names → `.app-qr`; `![lcd](x)` → `.lcd` | one ordered rule list |
| *images matching a pattern get grouped into rows* | `screenshots/` → packed N-per-row | one pattern + per-format N |
| *vector images matching a pattern get rasterised* | `LCD-Screenshots/*.svg` → PNG @200dpi | one pattern + dpi |
| *a text landmark wraps the block that follows* | "This product carries the RCM mark" → `::: compliance-list` | landmark → fence rules |

Plus two pure-value blocks: the **cover** (already templated) and the **back
page** (still hardcoded HTML).

There is nothing structurally Zoneconnex about the toolkit. It's four
generalisable rule families wearing one project's clothes. That's why this is
worth doing properly rather than forking per client.

**One genuinely universal rule stays in code:** inline-icon detection by pixel
size (`<= 64px` → `.icon`). It's content-independent, so it stays as-is.

---

## 2. Target manifest

`project.toml` grows from "which guides" to "which guides + how this content
behaves". Everything below is currently hardcoded in `brand.py`.

```toml
[project]
name        = "Zone Controller Stack"   # log output only
source_dir  = ".."                      # relative to toolkit; where the .md live
markdown_flavour = "docusaurus"         # "docusaurus" | "plain"

[brand]
engine = "engine.css"
css    = "anywair-skin.css"
logo   = "assets/logos/anywair-logo.svg"
model  = "UTY-ZCAW1"

# ---- BACK PAGE ------------------------------------------------------
# Was hardcoded HTML in brand.py. Every field optional; omitted = line dropped.
[back_page]
copyright_heading = "Copyright & Trademarks"
copyright_text = [
  "Copyright© 2026 GENERAL Australia & New Zealand. All rights reserved. ...",
  "App Store is a service mark of Apple Inc. © 2019. ...",
]
company = "General Australia Pty Ltd"
links   = [
  { text = "www.generalairstage.com.au", url = "https://www.generalairstage.com.au" },
  { text = "www.generalairstage.co.nz",  url = "https://www.generalairstage.co.nz" },
]
contact = "contact@fujitsugeneral.com.au | 1300 882 201"

# ---- IMAGE CLASS RULES ---------------------------------------------
# Ordered: FIRST match wins, so specific rules precede general ones.
# `match` is a regex against the image path/ref. `class` is the CSS class applied.
[[images.rules]]
match = "onlinedocs-qr-code\\.png$"
class = "doc-qr"
note  = "standalone docs QR — must precede the app-qr catch-all"

[[images.rules]]
match = "qr-code\\.png$"
class = "app-qr"

[[images.rules]]
match = "(google-play-icon|Apple-app-download-icon)\\.png$"
class = "app-qr"
note  = "store badges share the QR table; same cap keeps the table uniform"

# Alt-text tags: ![lcd](x) -> ![](x){.lcd}. Authored in alt text because the
# .md is ALSO a live website page and bare {.class} renders as literal text.
[images.alt_tags]
lcd   = { class = "lcd" }
large = { class = "large", width = "80%" }

# Strip size-hack alt text like ![max800px](x) -> ![](x)
[images]
strip_alt_pattern = "^max\\d+px$"
icon_max_px = 64          # images <= this in BOTH dimensions get {.icon}

# ---- SCREENSHOT ROWS ------------------------------------------------
[images.rows]
match     = "screenshots/.*\\.png$"
class     = "phone"
per_row   = { a4 = 3, a5 = 2 }   # counterpart to --img-phone in the page file
default_per_row = 2              # unregistered formats get the safe value

# ---- SVG RASTERISATION ----------------------------------------------
[[images.rasterize]]
match = "LCD-Screenshots/.*\\.svg$"
dpi   = 200
note  = "WeasyPrint won't scale these SVGs to a CSS width"

# ---- KEEP-TOGETHER BLOCKS -------------------------------------------
# A text landmark, then wrap the block that follows in a Pandoc fenced div.
[[blocks]]
landmark = "^This product carries the RCM mark"
wraps    = "list"          # "list" | "table"
class    = "compliance-list"

[[blocks]]
detect   = "empty-header-table"   # structural, not text-matched
wraps    = "table"
class    = "diagram-table"

# ---- GUIDES ---------------------------------------------------------
[[guides]]
file        = "Zoneconnex INSTALL & USER MANUAL.md"
title       = "Zoneconnex<br>Install &amp; User Manual"
subtitle    = "Install & User Manual"
cover_sub   = "INSTALL & USER MANUAL"
cover_image = "assets/images/zc-cover.png"
toc         = true
# asset_root = "pdf-toolkit"   # override for guides in a subfolder (see §3.2)
```

### Design rules for the manifest

- **Ordered rule lists, first match wins.** The current code encodes precedence
  as an `if 'onlinedocs' in fn: return` guard inside a callback. Ordering makes
  it declarative and inspectable.
- **Every rule carries an optional `note`.** These notes are the only record of
  *why* a rule exists; losing them is how the next person breaks it.
- **Omitted section = pass disabled.** A project with no QR codes writes no
  `[[images.rules]]` and that pass no-ops. No dead Zoneconnex regex running
  against someone else's content.

---

## 3. Refactor required underneath

### 3.1 `brand.py` becomes a rule interpreter

Each hardcoded pass becomes a generic one driven by the manifest:

| Current function | Becomes |
|---|---|
| `fix_require` | conditional on `markdown_flavour = "docusaurus"` |
| `rasterize_svgs` | loops `[[images.rasterize]]` |
| `normalize_and_tag_icons` | loops `[images.alt_tags]` + `[[images.rules]]`, keeps pixel-size icon detection |
| `group_screenshots` | driven by `[images.rows]` |
| `wrap_compliance_list` | one case of a generic landmark→fence pass over `[[blocks]]` |
| `wrap_diagram_tables` | one case of the same, with `detect = "empty-header-table"` |
| `BACK_PAGE` constant | rendered from `[back_page]` |

Net effect: `brand.py` keeps its *mechanisms* (which are genuinely reusable and
hard-won) and loses its *policies* (which are per-project).

### 3.2 Per-guide asset roots

Replace the single `TOOLKIT_REL = "pdf-toolkit"` with a per-guide value that
defaults to the toolkit folder. This is what unblocks the MIA Mobile App manual,
which lives in a subfolder and needs paths resolving one level up. **Add MIA as
the proof the mechanism works** — it's the only real second case available.

### 3.3 Extract to a standalone repo

Do this first. It settles "which copy is canonical" before two copies exist, and
gives the skill something stable to point at.

Ship: `engine.css`, `page-*.css`, `_page-template.css`, `build.sh`, `brand.py`,
`compress.py`, `insert-toc.lua`, `project.toml.template`, one example skin.
**Never ship:** `.venv/` (117 MB), `assets/` (6.4 MB, brand-specific),
`anywair-skin.css` as a default (it's one OEM — ship as a clearly-labelled example).

---

## 4. Skill structure

```
pdf-guide-build/
  SKILL.md                      # trigger, 4-layer model, invariants, workflow
  references/
    architecture.md             # layers, load order, 19-token contract
    manifest.md                 # every project.toml key, with examples
    new-brand.md                # add an OEM skin: the 20-minute path
    new-project.md              # adopt in a fresh repo: the full path
    verification.md             # baseline/diff protocol (non-negotiable)
    ground-truth.md             # the 8 hard-won facts
  assets/
    project.toml.template
    skin.css.template           # 19 tokens, commented, no brand values
    _page-template.css
```

### SKILL.md must state, in order

1. **When to trigger** — building/branding print PDFs from Markdown; adding an
   OEM skin; adding a page format; debugging image sizing in a PDF build.
2. **The four layers + load order** (engine → skin → page; manifest drives all).
3. **The invariants** (§5 below) — these are what keep it reusable.
4. **Route by task**: add a brand → `new-brand.md`. New repo → `new-project.md`.
   Change a size → `verification.md` first.
5. **Never skip verification.** A pure refactor must produce a zero metrics diff.

---

## 5. Invariants the skill must enforce

These are the rules that stop the system degrading back into a fork-per-client.

1. **`engine.css` contains zero raw colours and zero font names.** Enforceable:
   ```bash
   grep -nE '#[0-9A-Fa-f]{3,6}|Arial|Courier|Georgia' engine.css | grep -v 'is a bug'
   ```
   Must print nothing. A raw value here silently pins one OEM's brand into the
   shared layer.
2. **A skin defines all 19 tokens** (listed in the `engine.css` header) and
   nothing structural. If a brand can't be expressed in tokens, **add a token** —
   don't fork the engine.
3. **`brand.py` and `build.sh` name no document, brand, or content pattern.**
   Everything project-specific is in `project.toml`.
4. **A5 is built at A5.** Nothing is ever shrunk to reach a format.
5. **Floors never scale:** 9pt body, 10mm margins, +3mm gutter on the bound edge,
   ~40mm images. Hitting a floor means *more pages*, never smaller type.
6. **Source `.md` are also live website pages** (in a Docusaurus repo). PDF-only
   content — covers, intros, `{.class}` attributes — stays out of the `.md`.

---

## 6. Verification protocol — verbatim in the skill

Page count alone is insufficient; it missed regressions that image widths caught.

```bash
# baseline BEFORE any change, both formats
./build.sh --a4 --toc && cp pdfs/*-A4.pdf /tmp/baseline/
./build.sh --a5 --toc && cp pdfs/*-A5.pdf /tmp/baseline/
# ...change...  then rebuild both and diff metrics
```

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

Also assert: no blank pages, no image overflowing its page box.

Two traps:
- **`sort` both dumps before `diff`** — shell glob order otherwise creates
  phantom differences.
- **PDFs are not byte-reproducible** (embedded timestamps/IDs). `git diff` shows
  every rebuilt PDF as modified. Judge by rendered metrics, never file bytes.

**A pure refactor must produce a zero diff.** If it doesn't, it's a bug in the
refactor, not a design question.

---

## 7. Acceptance test — the only thing that proves it

The skill is done when **all three** pass:

1. **Brand swap.** New skin file + one `project.toml` line re-brands every
   document. No engine edit. *(Already proven — purple/serif test skin.)*
2. **Content swap.** A repo with different image conventions (no QRs, different
   screenshot folder, no compliance list) builds correctly with only manifest
   edits. No `brand.py` edit. **Not yet proven — this is the real test.**
3. **Regression.** Rebuilding Zoneconnex through the generalised toolkit
   produces a zero metrics diff against the current six PDFs.

Test 2 is the one that distinguishes a real skill from a demo. Until something
genuinely different has been built with it, "works for any brand and content"
is a claim, not a fact.

---

## 8. Effort and sequencing

| Step | Work | Blocking? |
|---|---|---|
| 1. Extract to standalone repo | mechanical | yes — do first |
| 2. Back-page → manifest | small, self-contained | no |
| 3. Image rules → manifest | **the bulk of it** | yes |
| 4. Blocks → manifest | medium | no |
| 5. Per-guide asset roots + add MIA | small | no |
| 6. Write SKILL.md + references | mechanical, from this doc | after 3 |
| 7. Acceptance test 2 on a real second project | needs a real repo | yes — final gate |

Step 3 is the substance. Steps 1, 6 are mechanical. Step 7 needs a second
project to exist; without it, ship the skill marked "validated on one project".

---

## 9. Current state

Committed: `b957f05` (A4 image tiers matched to A5 — the change that altered the
PDFs: manual 42→52 pp, quick start 13→18, user start 9→10).

Uncommitted: the four-layer refactor — `project.toml`, `engine.css`,
`anywair-skin.css` (new); `build.sh`, `brand.py`, `README.md`, `INSTRUCTIONS.md`,
`page-a4.css`, `page-a5.css`, `_page-template.css`, `src/css/custom.css`
(modified); `anywair-brand.css` (deleted); six rebuilt PDFs (rendering
unchanged). `npm run build` passes.

This design builds on that refactor — it does not replace it. Layers 2–4
(engine/skin/page) are done and proven; §3 here generalises layer 1 (the manifest).
