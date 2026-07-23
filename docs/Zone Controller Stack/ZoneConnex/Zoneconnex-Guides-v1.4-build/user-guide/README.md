# Zoneconnex USER Guide v1.4 — TEAL skin

Content: from QS_Zoneconnex_User_Guide_Approved.docx (20 May 2026).
Skin: anywair-brand.css
  --accent       #008996 teal  — headings, TOC, table headers, rules, callout borders
  --cover-border #008996 teal  — cover box border ONLY

## Images — NO RENAMING NEEDED
MD paths match Drive filenames exactly. Download Drive folder "2. User Guide",
unzip, drop ALL files straight into assets/images/ (overwrite the grey placeholders).

Note: the doc uses the ANNOTATED SVG versions (1.1, 2.2, 3.1, 4., 5., 6.1, 7.1., 8.1,
9.1, 10. Scene-Settings-v2). The plain PNGs (2., 3. and 4., 6., 7.-10.) and the
Spare.* files are unused source shots — fine to leave in the folder, they're ignored.

Still needed from your existing working folder (not in Drive):
- assets/logos/anywair-logo.svg        (real anywAiR logo)
- assets/images/ug-cover.png           (cover product render)
- assets/images/googleplay-qr-code.png
- assets/images/iOS-anywair-zone-qr-code.png   (PRODUCTION App Store QR)
- assets/images/google-play-icon.png
- assets/images/Apple-app-download-icon.png
- assets/images/onlinedocs-qr-code.png

## Build
pandoc "Zoneconnex-User-Guide-v1.4.md" --css anywair-brand.css --pdf-engine=weasyprint -f markdown+raw_html --lua-filter=insert-toc.lua -o "Zoneconnex-User-Guide-v1.4.pdf" -V papersize=a4
