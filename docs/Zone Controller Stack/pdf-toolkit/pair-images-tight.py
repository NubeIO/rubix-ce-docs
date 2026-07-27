#!/usr/bin/env python3
# ============================================================
# pair-images-tight.py — TIGHT-BUILD-ONLY post-process.
#
# Runs AFTER brand.py, only from build-tight.sh, on the throwaway temp copy.
# brand.py and the normal build never call this, so the current PDFs are
# unaffected.
#
# Purpose: the two LCD "retaining clips" diagrams sit as two consecutive
# standalone images and render STACKED (one per row), wasting most of a page.
# This wraps that specific consecutive pair into a <div class="img-row"> so the
# existing flex .img-row rule (anywair-brand.css) lays them SIDE BY SIDE.
#
# Surgical by design: only the Top-Retaining-Clips + Bottom-Retaining-Clips
# pair is matched. Nothing else is touched.
# ============================================================
import re, sys, pathlib

# The consecutive branded lines we target (see build; brand.py has already
# unwrapped the JSX require() into plain <img ... width="50%" />).
PAIR_RE = re.compile(
    r'^<img\s+src="([^"]*Top-Retaining-Clips[^"]*)"[^>]*/>\s*\n'
    r'^<img\s+src="([^"]*Bottom-Retaining-Clips[^"]*)"[^>]*/>\s*$',
    re.MULTILINE,
)

ROW = (
    '<div class="img-row">\n'
    '  <figure><img src="{a}" /></figure>\n'
    '  <figure><img src="{b}" /></figure>\n'
    '</div>'
)

def main(md_path):
    p = pathlib.Path(md_path)
    text = p.read_text(encoding="utf-8")
    new, n = PAIR_RE.subn(lambda m: ROW.format(a=m.group(1), b=m.group(2)), text)
    if n:
        p.write_text(new, encoding="utf-8")
    print(f"    paired {n} image row(s) in {p.name}")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        main(arg)
