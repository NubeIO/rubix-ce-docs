# Copilot instructions — anywAiR / Zoneconnex documentation

You are helping author **product documentation in Markdown** that exports to a
branded, print-ready PDF via Pandoc + WeasyPrint. You write and edit Markdown
content only. You do **not** edit the brand skin or the build pipeline.

## Golden rules

- **Australian English** in all content (e.g. colour, centre, optimise).
- **Never invent content, steps, specs, or structure.** If something is missing
  or unclear, insert a Markdown comment `<!-- TODO: confirm X with Bryn/Jonathan -->`
  instead of guessing. Do not pad sections with placeholder prose.
- **Do not edit** `anywair-brand.css` or `insert-toc.lua`. All branding,
  spacing, page breaks, footers, and the cover/back layout live in the CSS.
  If a visual change is needed, raise it — don't add inline styles.
- This skin matches an **approved Fujitsu/anywAiR style**. Match it exactly;
  do not modernise it.

## Heading discipline (the TOC depends on this)

The clickable Table of Contents is auto-built from H1 and H2 only.

- `#` = major numbered section → appears as a bold H1 entry in the TOC
- `##` = subsection → appears as an indented H2 entry in the TOC
- `###` = minor heading → black bold, **not** in the TOC
- **Never skip levels** (no `#` straight to `###`). Keep numbering consistent.

## Cover page (raw HTML block, top of file, not indented)

Always keep `class="cover-title"` on the title so the TOC ignores it.

```html
<div class="cover">
  <div class="cover-inner">
    <img class="cover-logo" src="assets/logos/anywair-logo.svg">
    <h1 class="cover-title">Quick Start Guide<br>Zoneconnex</h1>
    <div class="cover-divider"></div>
    <p class="cover-sub">INSTALLATION GUIDE</p>
    <div class="cover-divider"></div>
    <img class="cover-product" src="assets/images/zc-cover.png">
    <p class="cover-model">Model: UTY-ZCAW1</p>
  </div>
</div>
```

## Back page (raw HTML block, end of file, not indented)

```html
<div class="back-page">
  <img class="back-logo" src="assets/logos/anywair-logo.svg">
  <p class="back-company">General Australia Pty Ltd</p>
  <p class="back-links">www.generalairstage.com.au | www.generalairstage.co.nz</p>
  <p class="back-contact">contact@fujitsugeneral.com.au | 1300 882 201</p>
</div>
```

## Document order

Cover block → (auto TOC inserts here) → body (`#` / `##` sections) → back page.

## Images

- Images live in **`assets/`** and are **linked, never embedded**. Never inline
  base64 image data.
- Use a figure so the image + caption stay together as one block:

  ```html
  <figure>
    <img src="assets/images/step-03-wifi.png" alt="Wi-Fi setup screen">
    <figcaption>Figure 3 — Wi-Fi setup screen</figcaption>
  </figure>
  ```

- Quality: 300dpi PNG minimum; SVG for all diagrams/logos. Export screenshots at 2x.
- A heading immediately followed by its image stays glued automatically — keep
  the image directly after the heading, nothing in between.

## Callouts (exactly three types — blockquote syntax)

```markdown
> **Please note:** informational text here.
> **Warning:** caution text here.
> **Danger:** safety-critical text here.
```

Don't invent new callout styles.

## Manual page break

Force a break only when you genuinely need one:

```html
<div class="page-break"></div>
```

Each `#` section is intended to start on a fresh page — use the page-break div
before a new `#` if breaks aren't already being handled in the skin.

## Tables

Standard Markdown pipe tables. The skin styles them (teal header, repeating
header row across page breaks). Keep cells concise; don't hand-format widths.

## File naming

`[product-code]-[doc-type]-[language]-v[version].[ext]` — lowercase, no spaces,
no special characters (e.g. `zoneconnex-user-guide-au-v1.0.md`).

## Build command (do not change)

```bash
pandoc INPUT.md \
  --css anywair-brand.css \
  --pdf-engine=weasyprint \
  -f markdown+raw_html \
  --lua-filter=insert-toc.lua \
  -o OUTPUT.pdf \
  -V papersize=a4
```
