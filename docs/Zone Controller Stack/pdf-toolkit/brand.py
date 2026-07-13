#!/usr/bin/env python3
"""
brand.py — prepares the Zoneconnex / MIA manual Markdown for branded PDF output.

This is the converter half of the PDF toolkit. It takes the raw Docusaurus-style
manual Markdown (which is authored for the WEBSITE) and rewrites it into the
print-ready form the brand CSS expects, then Pandoc + WeasyPrint turn that into
the final PDF. See INSTRUCTIONS.md for the full pipeline.

What it does (each pass is idempotent-ish and safe on already-clean input):
  * fix_require            – unwrap Docusaurus `<img src={require("./x").default}>` -> `<img src="x">`
  * normalize_and_tag_icons– drop the `![max300px](..)` size-hack alt text; tag known
                             inline UI glyphs (plus/minus/chevron/tick/…) with {.icon}
  * wrap_diagram_tables    – wrap pin/connector tables (blank/image header) in
                             `::: diagram-table` so they lose the teal header + shrink
  * group_screenshots      – tag phone screenshots {.phone} and pack consecutive ones
                             into <div class="img-row"> rows of 3
  * fix_orphan_code_blocks – flatten deep (4+ space) list bullets so Pandoc doesn't
                             mis-parse them as overflowing code blocks
  * cover + back page      – inject the branded cover and copyright back page

IMPORTANT: run this on a COPY of the manual folder, never the source. It rewrites
the .md files in place. The documented pipeline copies the folder to a temp dir first.

Usage:
    python3 brand.py [BUILD_DIR]

BUILD_DIR is the copy of the "Zone Controller Stack" folder to process.
Defaults to the current working directory.
"""
import sys, io, re, os

# Directory holding the copied manual files (the "Zone Controller Stack" copy).
BUILD = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()


def urlenc(path):
    # encode spaces for Pandoc/HTML; leave slashes/dots intact
    return path.replace(" ", "%20")


def fix_require(text):
    # Docusaurus JSX <img src={require("./path").default} width="X%" /> -> plain <img src="path" ...>
    def repl(m):
        path = m.group(1)
        path = path.lstrip("./")            # drop leading ./
        path = path.replace("\\ ", " ")     # unescape spaces
        rest = m.group(2) or ""
        return 'src="%s"%s' % (path, rest)
    text = re.sub(r'src=\{require\("([^"]+)"\)\.default\}(\s+width="[^"]*")?',
                  repl, text)
    return text


# ---- inline UI icons: shrink to text height with {.icon} ----
ICON_NAMES = {
    "circle-plus", "circle-minus", "chevron-up", "chevron-down", "tick",
    "power", "rotate-ccw", "arrow-left", "user-cog", "plus", "play",
    "pause", "horizontal-dots", "apple-icon-30pix",
}


def normalize_and_tag_icons(text):
    # 1) strip the homemade size-hack alt text: ![max300px](x) / ![max800px](x) -> ![](x)
    text = re.sub(r'!\[(?:max\d+px)\]\(', '![](', text)
    # 2) tag known inline-icon images with {.icon}, regardless of directory prefix
    #    (raw MIA uses "img/NAME.png"; Install Guide uses "MIA%20Mobile%20App/img/NAME.png")
    def icon_repl(m):
        whole, alt, path = m.group(0), m.group(1), m.group(2)
        name = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        if name in ICON_NAMES:
            return '![%s](%s){.icon}' % (alt, path)
        return whole
    text = re.sub(r'!\[([^\]]*)\]\(([^)]*\bimg/[A-Za-z0-9._%-]+\.png)\)(?!\{)', icon_repl, text)
    return text


# ---- phone screenshots: tag .phone, group consecutive into rows of 3 ----
SCREENSHOT_IMG = re.compile(r'<img\s+src="((?:\./)?[^"]*screenshots/[^"]+\.png)"[^>]*/?>')


def _figure(path):
    return ('<figure>\n<img class="phone" src="%s" alt="anywAiR Zone app screenshot">\n'
            '<figcaption></figcaption>\n</figure>' % urlenc(path))


def group_screenshots(text, per_row=3):
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        m = SCREENSHOT_IMG.search(lines[i])
        if m and lines[i].strip().startswith("<img") and "screenshots/" in lines[i]:
            # collect a run of consecutive screenshot-only lines (blank lines allowed between)
            run = []
            j = i
            while j < n:
                mj = SCREENSHOT_IMG.search(lines[j])
                if mj and lines[j].strip().startswith("<img") and "screenshots/" in lines[j]:
                    run.append(mj.group(1))
                    j += 1
                elif lines[j].strip() == "":
                    k = j + 1
                    while k < n and lines[k].strip() == "":
                        k += 1
                    if k < n:
                        mk = SCREENSHOT_IMG.search(lines[k])
                        if mk and lines[k].strip().startswith("<img") and "screenshots/" in lines[k]:
                            j = k
                            continue
                    break
                else:
                    break
            if len(run) == 1:
                out.append("![](%s){.phone}" % urlenc(run[0]))
            else:
                for c in range(0, len(run), per_row):
                    chunk = run[c:c + per_row]
                    out.append('<div class="img-row">')
                    for p in chunk:
                        out.append(_figure(p))
                    out.append('</div>')
                    out.append("")
            i = j
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


BACK_PAGE = """

<div class="back-page">

<h3 class="copyright-heading">Copyright &amp; Trademarks</h3>

<p class="copyright-text">Copyright© 2026 GENERAL Australia &amp; New Zealand. All rights reserved. Actual products' colours may be different from the colours shown.</p>

<p class="copyright-text">App Store is a service mark of Apple Inc. © 2019. Google Play and the Google Play logo are trademarks of Google LLC. All other trademarks and tradenames are the property of their respective owners.</p>

<div class="copyright-rule"></div>

<img class="back-logo" src="{logo}">

<p class="back-company">General Australia Pty Ltd</p>

<p class="back-links">www.generalairstage.com.au | www.generalairstage.co.nz</p>

<p class="back-contact">contact@fujitsugeneral.com.au | 1300 882 201</p>

</div>
"""


def fix_orphan_code_blocks(text):
    """In the source, sub-bullets (indented 4+ spaces) sit inside ordered-list
    items but are separated by raw-HTML image blocks. Pandoc terminates the list
    at each HTML block, so a following 4-space-indented bullet is mis-parsed as an
    indented CODE block (monospace, gray bg, overflows the page). We flatten the
    print layout: de-indent every deep list bullet to a normal top-level bullet,
    and blank out whitespace-only lines. Images already sit at column 0."""
    out = []
    marker = re.compile(r'^( +)([-*] |\d+\.\s)(.*)$')
    for ln in text.split("\n"):
        if ln.strip() == "":
            out.append("")
            continue
        m = marker.match(ln)
        if m and len(m.group(1)) >= 3:
            out.append("- " + m.group(3))
        else:
            out.append(ln)
    return "\n".join(out)


def wrap_diagram_tables(text):
    """Pin/connector tables in the raw source are plain markdown tables with an
    empty (or image-only) header row and pin labels below. Without the
    ::: diagram-table fence they get default styling: the header cells render as a
    big TEAL block and the table stretches full-width (huge image). Wrapping each
    in ::: diagram-table ::: shrinks the table to ~95mm and whites out the header."""
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    def is_row(s): return s.lstrip().startswith("|") and s.rstrip().endswith("|")
    def cells(s): return [c.strip() for c in s.strip().strip("|").split("|")]
    def is_imgcell(c): return ("![" in c) or ("<img" in c)
    while i < n:
        if is_row(lines[i]) and i + 1 < n and is_row(lines[i + 1]) and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i + 1]):
            start = i
            j = i
            while j < n and is_row(lines[j]):
                j += 1
            block = lines[start:j]
            header = cells(block[0])
            body = block[2:]
            header_no_text = all(c == "" or is_imgcell(c) for c in header)
            has_img = any(is_imgcell(c) for c in header) or any(is_imgcell(r) for r in body)
            already_wrapped = start > 0 and lines[start - 1].strip().startswith("::: diagram-table")
            if header_no_text and has_img and not already_wrapped:
                out.append("::: diagram-table")
                out.extend(block)
                out.append(":::")
            else:
                out.extend(block)
            i = j
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def brand(infile, cover, logo_path, mobile=False):
    with io.open(infile, encoding="utf-8") as f:
        text = f.read()
    text = fix_require(text)
    if mobile:
        text = normalize_and_tag_icons(text)
        text = wrap_diagram_tables(text)
        text = group_screenshots(text, per_row=3)
        text = fix_orphan_code_blocks(text)
    lines = text.split("\n")
    # drop the first top-level H1 title line — the cover replaces it
    out = []
    dropped = False
    for ln in lines:
        if not dropped and ln.strip().startswith("# "):
            dropped = True
            continue
        out.append(ln)
    body = "\n".join(out).lstrip("\n")
    result = cover + "\n\n" + body + BACK_PAGE.format(logo=logo_path)
    with io.open(infile, "w", encoding="utf-8") as f:
        f.write(result)
    print("branded:", infile)


# --- Install Guide (runs from the ZC-copy root; toolkit assets under pdf-toolkit/assets/) ---
COVER_INSTALL = """<div class="cover">
<div class="cover-inner">
<img class="cover-logo" src="pdf-toolkit/assets/logos/anywair-logo.svg">
<h1 class="cover-title">Zoneconnex<br>Install &amp; User Manual</h1>
<div class="cover-divider"></div>
<p class="cover-sub">INSTALL & USER MANUAL</p>
<div class="cover-divider"></div>
<img class="cover-product" src="pdf-toolkit/assets/images/zc-cover.png">
<p class="cover-model">Model: UTY-ZCAW1</p>
</div>
</div>"""

# --- MIA (runs from MIA Mobile App/; toolkit assets one level up) ---
COVER_MIA = """<div class="cover">
<div class="cover-inner">
<img class="cover-logo" src="../pdf-toolkit/assets/logos/anywair-logo.svg">
<h1 class="cover-title">anywAiR&reg; Zone<br>Mobile App User Manual</h1>
<div class="cover-divider"></div>
<p class="cover-sub">MOBILE APP USER MANUAL</p>
<div class="cover-divider"></div>
<img class="cover-product" src="screenshots/112.png" style="max-height:95mm;width:auto;">
<p class="cover-model">Model: UTY-ZCAW1</p>
</div>
</div>"""


if __name__ == "__main__":
    brand(os.path.join(BUILD, "Zoneconnex Install Guide.md"),
          COVER_INSTALL, "pdf-toolkit/assets/logos/anywair-logo.svg", mobile=True)
    brand(os.path.join(BUILD, "MIA Mobile App", "MIA App User Manual.md"),
          COVER_MIA, "../pdf-toolkit/assets/logos/anywair-logo.svg", mobile=True)
