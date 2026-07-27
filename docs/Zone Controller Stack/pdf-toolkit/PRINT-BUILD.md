# Tight Print Build — Zoneconnex Guides

A **separate, print-optimised** PDF build that compresses the vertical white
space of the guides for physical printing, while keeping the approved v1.4
content. It produces **new files** named `<guide> (print).pdf` and **never
touches** the current PDFs, `build.sh`, `brand.py`, or any `.md` source.

For the standard (website-parity) build and everything `brand.py` does, see
[`INSTRUCTIONS.md`](./INSTRUCTIONS.md). This file covers only the tight variant.

> **The `.md` is ALSO the live website.** None of the print work edits it. All
> layout rules live in the tight CSS + a tight-only post-process, so the website
> pages and the standard PDFs are unaffected.

---

## Build command

```bash
# from the repo root OR from this "Zone Controller Stack" folder:
pdf-toolkit/build-tight.sh                                   # the named guides
pdf-toolkit/build-tight.sh "Zoneconnex User Start Guide"     # just one
pdf-toolkit/build-tight.sh "Zoneconnex Quick Start Guide" "Zoneconnex INSTALL & USER MANUAL" "Zoneconnex User Start Guide"
```

Output lands next to the source PDFs, e.g.
`pdfs/Zoneconnex Quick Start Guide (print).pdf`. Like `build.sh`, it runs on a
throwaway `mktemp` copy, so no source file is mutated.

Result (current page counts): Quick Start **21 → 13**, User Start **15 → 9**,
Install & User Manual **39 → 38** (the manual is image-dominated, so spacing
alone reclaims little there — see [Known limits](#known-limits)).

---

## The files

| File | Purpose |
|------|---------|
| `build-tight.sh` | Clone of `build.sh`. Loads `anywair-print-tight.css` as the 2nd `--css` and writes `<name> (print).pdf`. Runs `pair-images-tight.py` after `brand.py`. No TOC. |
| `anywair-print-tight.css` | Tighter density layer, loaded **after** `anywair-brand.css` so it wins by cascade. Holds all the layout rules below. |
| `pair-images-tight.py` | Tight-only post-process (after `brand.py`): rows specific stacked diagrams side-by-side. |

Nothing here is loaded by the standard `build.sh` — the two builds are fully
independent.

---

## Layout rules this build enforces

These are the print rules we agreed on. All are in `anywair-print-tight.css`
unless noted.

### Compression (moderate)
- Numbered `# H1` sections no longer force a fresh page — they flow inline with
  a small gap (`margin-top: 10pt`) instead of the base 18pt fresh-page pad.
- Tighter heading / figure / paragraph / list / table spacing.
- Image **sizing** matches the standard print layer (82mm / lcd 90mm); only the
  spacing around images is tightened, not the images themselves.

### Protected rules (never sacrificed for density)
1. **No orphan headings.** A numbered `H1`/`H2` never strands at a page bottom.
   It keeps `break-after: avoid`, **and** the first block after it gets
   `break-before: avoid` — so the heading glues to whatever follows, whether
   that's a paragraph, a **callout/blockquote**, a list, or a table. (This is
   why "3. Set Up Your Account and Home" no longer separates from its info box.)
2. **Caption labels stay with their image.** A bold label paragraph that
   introduces a diagram — e.g. `**Zoneconnex Top View:**` followed by the image
   — is glued to that image (`p:has(> strong:only-child):has(+ p > img)`), so it
   can't strand at a page bottom with the diagram pushed to the next page.
3. **Images stay with their captions.** `figure`/`figcaption` break rules are
   inherited from `anywair-brand.css` and deliberately **not** overridden.
4. **Comfortable margins.** The `@page` margins (22/18mm) are left untouched.

### Space-saving pairing
- The two LCD **retaining-clip** diagrams (Top / Bottom) were stacked one per
  row, wasting a page. `pair-images-tight.py` wraps that specific consecutive
  pair into a `<div class="img-row">` so the existing flex `.img-row` rule lays
  them **side-by-side**. It matches only those filenames — surgical by design.

---

## Known limits

- **Image-heavy pages don't shrink from spacing alone.** The Install & User
  Manual is dominated by large diagrams (component renders, wiring views) with
  empty bands around them, so tightening spacing reclaims only ~1 page. The
  lever there is **image sizing / more side-by-side pairing**, not spacing.
- **`build-tight.sh` default guide list.** With no arguments it builds only the
  guides listed in its `GUIDES` default. Pass guide names explicitly to build a
  specific set (see command above).

---

## Making further tweaks

1. Edit **only** these tight files: `anywair-print-tight.css` (rules/spacing),
   `pair-images-tight.py` (which images to row up), or `build-tight.sh`.
2. Never edit `build.sh`, `brand.py`, `anywair-brand.css`, `anywair-print.css`,
   or any `.md` — those drive the website and the standard PDFs.
3. Rebuild with the command above and eyeball the affected pages.
4. Commit the regenerated `(print).pdf` files alongside the CSS/script change.
