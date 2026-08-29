## Summary

The three Zoneconnex guides (plus the MIA app manual) now have **Markdown as the
single source of truth**, with a `pdf-toolkit/` that builds branded print PDFs at
both A4 and A5 from those same files. The superseded `Zoneconnex-Guides-v1.4-build/`
tree (39 MB, 76 files) has been removed.

The approved `.docx` content is preserved exactly — page counts were verified
against the previous outputs at every step:

| Guide | A4 | A5 |
|---|---|---|
| Zoneconnex INSTALL & USER MANUAL | 52 | 63 |
| Zoneconnex Quick Start Guide | 18 | 19 |
| Zoneconnex User Start Guide | 10 | 11 |
| MIA App User Manual | 100 | 135 |

The three Zoneconnex guides match their pre-existing page counts exactly. The MIA
manual is new to the toolkit.

Before deleting the v1.4 tree, every image in it was content-verified by SHA-256
rather than by filename: 63 of 66 matched a file elsewhere in the repo byte for
byte, and the 3 that did not are the same photographs at lower resolution
(RGBA 2000×1500 vs the live RGB 5500×4125; mean per-channel difference 0.01–0.03
once composited and resized). Nothing needed preserving.

## What to review

- **The guide `.md` content** under `docs/Zone Controller Stack/` — this is the
  part that matters. It is now what the website serves *and* what the PDFs are
  built from, so an error here shows up in both.
- **That the Docusaurus site builds.** Verified: `npm run build` passes. The
  broken-link warnings in that output are pre-existing and in unrelated docs
  (`docs/tutorials/`, `docs/rubix-ce/`), not introduced here.

## What to skim

`pdf-toolkit/` internals — the CSS layers, `brand.py` passes and build script.
It is a fair amount of machinery and reviewing it line by line is unlikely to be
a good use of anyone's time. Happy to walk through it on a call instead.

## Note for authors

The PDF build expects a few markdown conventions, all documented in
`pdf-toolkit/AUTHORING.md`:

- Raw HTML must start **flush left** — indented HTML is parsed as a code block
- Callouts are `<div class="callout-info|callout-warning|callout-danger">`
- Images take `{.small}`, `{.medium}`, `{.large}`; inline icons are auto-detected
- **No manual page breaks before an H1** — the page layer handles section flow

These only affect the PDF build. The website renders the same files either way,
so a guide that ignores them still publishes — it just prints wrong.

## Engine note

`pdf-toolkit/` carries a **pinned copy of a generic document engine** — see
`pdf-toolkit/ENGINE-VERSION` for the version and its source. It builds
standalone: no external dependency, no network fetch, nothing to install beyond
pandoc and the Python packages already used here.

Improvements flow engine → this repo, never the other way, so this project cannot
silently fork the engine. `ENGINE-VERSION` also records the known differences
from the pinned version, including one upstream fix this copy does not yet carry
(harmless here — it only affects guides whose sole H1 is the title).
