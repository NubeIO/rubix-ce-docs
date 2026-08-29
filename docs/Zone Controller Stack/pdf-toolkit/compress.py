#!/usr/bin/env python3
"""compress.py — shrink the images inside a built PDF, in place.

Called by build.sh as the final step. For every image in the PDF: composite any
transparency onto WHITE (avoids black-box product shots), cap the long edge at
~1800px, and re-encode as JPEG q82 when that is smaller than the original.

Uses PyMuPDF's Page.replace_image (v1.28+). Saves to a sibling temp file then
os.replace()s over the original, because MuPDF refuses a non-incremental save
onto the file it has open.

    python compress.py "path/to/file.pdf"
"""
import sys
import io
import os
import fitz
from PIL import Image

CAP = 1800        # max long-edge px
QUALITY = 82      # JPEG quality


def compress(path):
    out = path[:-4] + ".compressed.pdf"
    doc = fitz.open(path)

    # map each image xref -> a page that references it (Page.replace_image needs a page)
    xref_page = {}
    for pno in range(len(doc)):
        for img in doc[pno].get_images(full=True):
            xref_page.setdefault(img[0], pno)

    n = 0
    for xref, pno in xref_page.items():
        info = doc.extract_image(xref)
        if not info:
            continue
        raw = info["image"]
        try:
            im = Image.open(io.BytesIO(raw))
        except Exception:
            continue
        # composite transparency onto white
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            im = im.convert("RGBA")
            bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
            im = Image.alpha_composite(bg, im).convert("RGB")
        else:
            im = im.convert("RGB")
        # cap long edge
        w, h = im.size
        scale = min(1.0, CAP / max(w, h))
        if scale < 1.0:
            im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=QUALITY, optimize=True)
        new = buf.getvalue()
        if len(new) < len(raw):
            try:
                doc[pno].replace_image(xref, stream=new)
                n += 1
            except Exception as e:
                print("  skip xref", xref, e)

    doc.save(out, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(out, path)
    print("    compressed %d image(s) -> %.2f MB" % (n, os.path.getsize(path) / 1e6))


if __name__ == "__main__":
    compress(sys.argv[1])
