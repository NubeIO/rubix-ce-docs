# Zoneconnex INSTALL Guide v1.4 — TEAL skin, RED cover border

Content: from QS_Zoneconnex_Install_Guide_Approved.docx (20 May 2026).
Skin: anywair-brand.css
  --accent       #008996 teal  — headings, TOC, table headers, rules, callout borders
  --cover-border #E61E23 red   — cover box border ONLY (sampled from Claire's approved Canva cover)

## Images — NO RENAMING NEEDED
MD paths match Drive filenames exactly. Download Drive folder "1. Install Guide",
unzip, drop ALL files straight into assets/images/ (overwrite the grey placeholders).

Still needed from your existing working folder (not in Drive):
- assets/logos/anywair-logo.svg        (real anywAiR logo)
- assets/images/ig-cover.png           (cover product render, Figma PNG @2x)
- assets/images/googleplay-qr-code.png
- assets/images/iOS-anywair-zone-qr-code.png   (PRODUCTION App Store QR, not TestFlight)
- assets/images/google-play-icon.png
- assets/images/Apple-app-download-icon.png
- assets/images/onlinedocs-qr-code.png

## Build
pandoc "Zoneconnex-Install-Guide-v1.4.md" --css anywair-brand.css --pdf-engine=weasyprint -f markdown+raw_html --lua-filter=insert-toc.lua -o "Zoneconnex-Install-Guide-v1.4.pdf" -V papersize=a4
