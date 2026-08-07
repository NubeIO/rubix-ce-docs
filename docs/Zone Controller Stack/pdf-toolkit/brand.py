#!/usr/bin/env python3
"""
brand.py — prepares the Zoneconnex / MIA manual Markdown for branded PDF output.

This is the converter half of the PDF toolkit. It takes the raw Docusaurus-style
manual Markdown (which is authored for the WEBSITE) and rewrites it into the
print-ready form the brand CSS expects, then Pandoc + WeasyPrint turn that into
the final PDF. See INSTRUCTIONS.md for the full pipeline.

What it does (each pass is idempotent-ish and safe on already-clean input):
  * fix_require            – unwrap Docusaurus `<img src={require("./x").default}>` -> `<img src="x">`
  * normalize_and_tag_icons– drop the `![max800px](..)` size-hack alt text; tag inline UI
                             glyphs with {.icon}, detected automatically by image size
                             (any PNG <= 64x64px); restore the store-badge width cap
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
import sys, io, re, os, struct, urllib.parse, tomllib

# Directory holding the copied manual files (the "Zone Controller Stack" copy).
BUILD = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

# Toolkit folder, relative to BUILD — where the manifest and assets live. Pandoc
# runs from BUILD, so cover/logo src paths are written relative to it.
TOOLKIT_REL = "pdf-toolkit"
MANIFEST_PATH = os.path.join(BUILD, TOOLKIT_REL, "project.toml")
# Page size being built ("a4" / "a5"), passed by build.sh. Only affects how many
# phone screenshots go in a row — see SCREENSHOTS_PER_ROW.
SIZE = (sys.argv[2] if len(sys.argv) > 2 else "a5").lower()

# How many phone screenshots fit in one <div class="img-row">, per page size.
# This is the COUNTERPART to --img-phone in page-<size>.css, and it has to live
# here rather than in CSS: .img-row is display:flex with no wrap, so the count is
# baked into the HTML by group_screenshots() before any stylesheet is applied.
# The two halves must satisfy the row budget:
#     n * --img-phone + (n - 1) * --img-row-gap  <=  --col
# subject to --img-phone >= ~40mm (the screenshot legibility floor).
SCREENSHOTS_PER_ROW = {
    "a4": 3,   # 3*54 + 2*6 = 174mm == --col (174mm)
    "a5": 2,   # 2*46 + 1*6 =  98mm <= --col (122mm).
               # 3-up would need <=36.6mm per phone — under the 40mm floor, so A5
               # genuinely cannot carry three. This is a capacity limit, not a preference.
}
# An unregistered format gets the conservative 2-up rather than inheriting A4's 3,
# which would silently reproduce the overflow this table exists to prevent.
PER_ROW = SCREENSHOTS_PER_ROW.get(SIZE, 2)


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
# Detection is automatic by image size: any PNG <= ICON_MAX_PX in both dimensions
# is treated as an inline glyph. The repo has a clean cutoff (real icons are
# <= 51x51; nothing exists between 52 and 141px), so 64 is a safe threshold and
# new icons "just work" with no list to maintain.
ICON_MAX_PX = 64

# Store badges are far larger than any icon, so the size gate excludes them — but
# they must not fall back to the block rule, so their width cap is preserved.
BADGE_NAMES = ("google-play-icon", "Apple-app-download-icon")


def png_size(abspath):
    """Return (width, height) read from the PNG IHDR chunk, or None if the file is
    missing / not a readable PNG. No third-party dependency."""
    try:
        with open(abspath, "rb") as f:
            data = f.read(24)
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        return struct.unpack(">I", data[16:20])[0], struct.unpack(">I", data[20:24])[0]
    except (OSError, struct.error):
        return None


def _resolve(ref, base_dir):
    """Map a markdown image ref (URL-encoded, relative) to an absolute path on disk."""
    p = urllib.parse.unquote(ref).lstrip("./")
    return os.path.normpath(os.path.join(base_dir, p))


def rasterize_svgs(text, base_dir):
    """Convert LCD-Screenshots SVG images to PNG in the build copy and rewrite refs.

    WeasyPrint will not scale these SVGs up to a CSS width, so LCD screenshots
    written as .svg render at an inconsistent intrinsic size next to the .png ones.
    Rasterizing every LCD-Screenshots SVG to PNG at build time makes them all size
    uniformly via the shared `.lcd` class. Only touches the throwaway build copy;
    the source .md / website .svg refs are unaffected. Requires PyMuPDF (fitz).
    """
    import fitz  # PyMuPDF, already a build dependency
    svg_ref = re.compile(r'(!\[[^\]]*\]\()([^)]*LCD-Screenshots/[^)]+\.svg)(\)(?:\{[^}]*\})?)')

    def repl(m):
        pre, ref, post = m.group(1), m.group(2), m.group(3)
        src = _resolve(ref, base_dir)
        if not os.path.exists(src):
            return m.group(0)  # leave untouched if missing
        # Use a distinct suffix so we never overwrite an existing (possibly
        # differently-annotated) PNG of the same base name.
        png_ref = ref[:-4] + ".from-svg.png"
        dst = _resolve(png_ref, base_dir)
        # render at ~200 dpi for crisp print output
        doc = fitz.open(src)
        pix = doc[0].get_pixmap(dpi=200)
        pix.save(dst)
        doc.close()
        return pre + urlenc(png_ref) + post

    return svg_ref.sub(repl, text)


def normalize_and_tag_icons(text, base_dir):
    # 0) alt-text size TAGS -> real Pandoc attributes. These live inside the alt
    #    text (![lcd](x)) so Docusaurus renders them harmlessly (alt text is
    #    invisible on the website), while here we turn them into the Pandoc
    #    class/width the print CSS needs. Never write bare {.class} / {width=} in
    #    the shared .md — Docusaurus prints those braces as literal text.
    #      ![lcd](x)   -> ![](x){.lcd}                 (fixed-width LCD screenshot)
    #      ![large](x) -> ![](x){.large width=80%}     (wide diagram at 80%)
    text = re.sub(r'!\[lcd\]\(([^)]+)\)(?!\{)',   r'![](\1){.lcd}', text)
    text = re.sub(r'!\[large\]\(([^)]+)\)(?!\{)', r'![](\1){.large width=80%}', text)
    # Content QR codes (e.g. §8 "onlinedocs" QR) are LINKED images and otherwise
    # fall back to the full-width block rule, spilling onto their own page. Tag with
    # {.doc-qr} so the print CSS can cap them small. Alt is stripped in step 2, so
    # match on the filename and re-emit with the class (keep the surrounding link).
    text = re.sub(r'!\[[^\]]*\]\((img/onlinedocs-qr-code\.png)\)(?!\{)',
                  r'![](\1){.doc-qr}', text)
    # App-store QR codes in the §5.1 download table: tag {.app-qr} so the print CSS
    # can shrink them (the 58mm td-img cap makes the table too tall to fit with its
    # heading). Same class-based mechanism as .doc-qr (src-attr selectors don't
    # reliably match through the pandoc->weasyprint pipeline).
    #    (filenames vary between guides: googleplay-qr-code, Andriod-anywair-zone-qr-code,
    #    iOS-anywair-zone-qr-code — match any app-store QR, but NOT the onlinedocs QR
    #    already tagged .doc-qr above.)
    def _appqr(m):
        fn = m.group(1)
        if 'onlinedocs' in fn:
            return m.group(0)
        return '![](%s){.app-qr}' % fn
    text = re.sub(r'!\[[^\]]*\]\((img/[^)]*qr-code\.png)\)(?!\{)', _appqr, text)
    # 1) store badges (Google Play / App Store) live in the same app-download table
    #    as the app QR codes. Tag them {.app-qr} too so EVERY image in that table is
    #    capped to the one consistent size (see .app-qr in the print CSS), instead of
    #    the QR codes and badges rendering at different sizes.
    badge_re = re.compile(
        r'!\[max\d+px\]\(([^)]*(?:%s)\.png)\)(?!\{)' % "|".join(BADGE_NAMES))
    text = badge_re.sub(r'![](\1){.app-qr}', text)
    # 2) strip the remaining size-hack alt text: ![max800px](x) -> ![](x)
    text = re.sub(r'!\[(?:max\d+px)\]\(', '![](', text)
    # 3) tag inline-icon images with {.icon}, detected by pixel size (<= ICON_MAX_PX).
    def icon_repl(m):
        whole, alt, path = m.group(0), m.group(1), m.group(2)
        dims = png_size(_resolve(path, base_dir))
        if dims is None:
            sys.stderr.write("brand.py: could not size image, left untagged: %s\n"
                             % _resolve(path, base_dir))
            return whole
        if dims[0] <= ICON_MAX_PX and dims[1] <= ICON_MAX_PX:
            return '![%s](%s){.icon}' % (alt, path)
        return whole
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+\.png)\)(?!\{)', icon_repl, text)
    return text


# ---- phone screenshots: tag .phone, group consecutive into rows ----
# Row size is per page format — see SCREENSHOTS_PER_ROW at the top of this file.
SCREENSHOT_IMG = re.compile(r'<img\s+src="((?:\./)?[^"]*screenshots/[^"]+\.png)"[^>]*/?>')


def _figure(path):
    return ('<figure>\n<img class="phone" src="%s" alt="anywAiR Zone app screenshot">\n'
            '<figcaption></figcaption>\n</figure>' % urlenc(path))


def group_screenshots(text, per_row=2):
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

<p class="back-links"><a href="https://www.generalairstage.com.au">www.generalairstage.com.au</a> | <a href="https://www.generalairstage.co.nz">www.generalairstage.co.nz</a></p>

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


def wrap_compliance_list(text):
    """Keep the Compliance standards list (AS/NZS ...) together on one page.
    The list is short but sits near a page bottom, so its last item widows onto
    a fresh page. We wrap just this list in a Pandoc fenced div so the print CSS
    (.compliance-list { break-inside: avoid }) can hold it together. Matched by
    the '**Compliance**' lead-in + the RCM sentence, so no other list is touched."""
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].strip().startswith("This product carries the RCM mark"):
            out.append(lines[i])
            i += 1
            # skip blank lines, then wrap the contiguous bullet list that follows
            while i < n and lines[i].strip() == "":
                out.append(lines[i]); i += 1
            if i < n and lines[i].lstrip().startswith("- "):
                out.append("")
                out.append("::: {.compliance-list}")
                while i < n and (lines[i].lstrip().startswith("- ") or lines[i].strip() == ""):
                    out.append(lines[i]); i += 1
                out.append(":::")
                out.append("")
                continue
        else:
            out.append(lines[i]); i += 1
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


def brand(infile, cover, logo_path, mobile=False, subtitle=None,
          title_override=None, intro=None):
    if not os.path.exists(infile):
        print("skipped (not found):", infile)
        return
    with io.open(infile, encoding="utf-8") as f:
        text = f.read()
    text = fix_require(text)
    # Strip the emoji variation selector (U+FE0F). Browsers render ⚠️/ℹ️ as a single
    # colour glyph, but WeasyPrint renders the trailing U+FE0F as a stray bullet /
    # pilcrow next to the callout emoji. Removing it leaves the plain ⚠ / ℹ symbol.
    text = text.replace("️", "")
    text = rasterize_svgs(text, os.path.dirname(infile))
    if mobile:
        text = normalize_and_tag_icons(text, os.path.dirname(infile))
        text = wrap_diagram_tables(text)
        text = wrap_compliance_list(text)
        text = group_screenshots(text, per_row=PER_ROW)
        text = fix_orphan_code_blocks(text)
    lines = text.split("\n")
    # The first top-level H1 is the document title. The branded cover page shows it,
    # but the approved v1.4 layout ALSO repeats it as a styled title block at the top
    # of the first content page (title + subtitle, then an optional intro). So instead
    # of dropping the H1, convert it into <h1 class="doc-title"> + <p class="doc-subtitle">.
    #   title_override: PDF title text when it should differ from the .md's H1
    #     (the .md is also the website, so we don't rename the H1 there).
    #   intro: PDF-ONLY prose injected right after the title (e.g. the User guide
    #     "Welcome" block). MUST NOT live in the .md — that is the live website page.
    out = []
    handled = False
    for ln in lines:
        if not handled and ln.strip().startswith("# "):
            handled = True
            title = title_override or ln.strip()[2:].strip()
            block = '<h1 class="doc-title">%s</h1>' % title
            if subtitle:
                block += '\n<p class="doc-subtitle">%s</p>' % subtitle
            if intro:
                block += '\n\n' + intro.strip()
            out.append(block)
            continue
        out.append(ln)
    body = "\n".join(out).lstrip("\n")
    result = cover + "\n\n" + body + BACK_PAGE.format(logo=logo_path)
    with io.open(infile, "w", encoding="utf-8") as f:
        f.write(result)
    print("branded:", infile)


# --- COVER TEMPLATE ---------------------------------------------------------
# One template for every guide. The four hand-written cover blocks this replaced
# differed only in the values now supplied by project.toml: cover_class, title,
# cover_sub, cover_image and the model line. Paths are relative to the build-copy
# root, which is where pandoc runs.
COVER_TEMPLATE = """<div class="cover{cover_class}">
<div class="cover-inner">
<img class="cover-logo" src="{logo}">
<h1 class="cover-title">{title}</h1>
<div class="cover-divider"></div>
<p class="cover-sub">{cover_sub}</p>
<div class="cover-divider"></div>
<img class="cover-product" src="{cover_image}"{cover_image_style}>
{model_line}</div>
</div>"""


def render_cover(guide, brand):
    """Build a cover HTML block from a project.toml [[guides]] entry."""
    cls = guide.get("cover_class", "")
    model = brand.get("model", "")
    style = guide.get("cover_image_style", "")
    return COVER_TEMPLATE.format(
        cover_class=(" " + cls) if cls else "",
        logo=urlenc(TOOLKIT_REL + "/" + brand["logo"]),
        title=guide["title"],
        cover_sub=guide.get("cover_sub", guide.get("subtitle", "")),
        cover_image=urlenc(TOOLKIT_REL + "/" + guide["cover_image"]),
        cover_image_style=(' style="%s"' % style) if style else "",
        model_line=('<p class="cover-model">Model: %s</p>\n' % model) if model else "",
    )


def flatten_transparent_pngs(build_dir):
    """Composite every transparent PNG in the build copy onto a WHITE background.

    Many product renders / screenshots / icons are transparent RGBA. WeasyPrint (and
    the downstream image compressor) can composite those onto BLACK, producing the
    "product on a black box" bug — especially on the covers and any image landing on
    a dark area. Flattening onto white here, in the throwaway build copy, fixes every
    such image at once and can never recur. Source files (also served on the website)
    are left untouched. Uses the soft-mask via alpha_composite (the known-good method).
    """
    from PIL import Image
    n = 0
    for root, _dirs, files in os.walk(build_dir):
        for fn in files:
            if not fn.lower().endswith(".png"):
                continue
            p = os.path.join(root, fn)
            try:
                im = Image.open(p)
            except Exception:
                continue
            if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
                im = im.convert("RGBA")
                if im.getchannel("A").getextrema()[0] < 255:  # actually transparent
                    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
                    Image.alpha_composite(bg, im).convert("RGB").save(p)
                    n += 1
    print("flattened %d transparent PNG(s) onto white" % n)


if __name__ == "__main__":
    # Everything product-specific comes from project.toml. Nothing below names a
    # document, a brand or an asset — see README.md ("Reusing the toolkit").
    if not os.path.exists(MANIFEST_PATH):
        sys.exit("error: no project.toml at %s" % MANIFEST_PATH)
    with open(MANIFEST_PATH, "rb") as f:
        manifest = tomllib.load(f)
    brand_cfg = manifest["brand"]
    logo_rel = urlenc(TOOLKIT_REL + "/" + brand_cfg["logo"])

    # Flatten transparent PNGs FIRST so covers and all referenced images are safe.
    flatten_transparent_pngs(BUILD)

    for guide in manifest["guides"]:
        brand(os.path.join(BUILD, guide["file"]),
              render_cover(guide, brand_cfg),
              logo_rel,
              mobile=guide.get("mobile", True),
              subtitle=guide.get("subtitle"),
              title_override=guide.get("title_override"),
              intro=guide.get("intro"))
