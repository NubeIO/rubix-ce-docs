#!/usr/bin/env bash
# ============================================================
# build.sh — canonical Zoneconnex / MIA PDF build.
#
# Page size is a first-class argument. A5 is the print deliverable and is
# BUILT at A5 — nothing is ever shrunk to reach a format. A4 is screen /
# desk reference only. Every output filename ends in -A4 or -A5.
#
# The Table of Contents is OPTIONAL — off by default, add --toc.
#
# Usage (run from the repo root OR this folder):
#   pdf-toolkit/build.sh                       # all guides, A5, no TOC
#   pdf-toolkit/build.sh --a4                  # all guides, A4
#   pdf-toolkit/build.sh --toc                 # A5 with a TOC page
#   pdf-toolkit/build.sh --a4 "Zoneconnex Quick Start Guide"    # one guide
#   pdf-toolkit/build.sh --size a5 --toc "Zoneconnex INSTALL & USER MANUAL"
#
# CSS layer order (cascade matters):
#   anywair-brand.css   engine + skin
#   page-<size>.css     page size, margins, type scale, image scale
# Page size comes from the CSS @page rule only — there is deliberately no
# -V papersize flag, so the two can never disagree.
#
# What it does (see INSTRUCTIONS.md for the passes brand.py runs):
#   1. copies "Zone Controller Stack" to a throwaway temp dir
#   2. runs brand.py on the copy (flatten transparent PNGs, rasterize SVGs,
#      strip U+FE0F, alt-tag -> attributes, cover + back page)
#   3. pandoc + weasyprint with anywair-brand.css THEN page-<size>.css
#      (page layer wins by cascade order); insert-toc.lua only with --toc
#   4. compresses images (PyMuPDF: cap 1800px, JPEG q82, white-composite)
#   5. copies the finished PDF into docs/Zone Controller Stack/pdfs/
# ============================================================
set -euo pipefail

# --- locate the toolkit + source folder regardless of CWD -------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"      # .../pdf-toolkit
SRC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"                          # .../Zone Controller Stack
VENV="$SCRIPT_DIR/.venv/bin"
PY="$VENV/python"

# --- args: --toc, page size, optional list of guide basenames ---------------
WANT_TOC=0
SIZE="a5"          # A5 is the print deliverable and the default
GUIDES=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --toc)  WANT_TOC=1 ;;
    --a4)   SIZE="a4" ;;
    --a5)   SIZE="a5" ;;
    --size) shift; SIZE="$(printf '%s' "${1:-}" | tr '[:upper:]' '[:lower:]')" ;;
    *)      GUIDES+=("$1") ;;
  esac
  shift
done

PAGE_CSS="$SCRIPT_DIR/page-$SIZE.css"
if [[ ! -f "$PAGE_CSS" ]]; then
  echo "error: unknown page size '$SIZE' (no page-$SIZE.css)" >&2
  echo "available:" >&2
  for f in "$SCRIPT_DIR"/page-*.css; do
    b="$(basename "$f")"; b="${b#page-}"; echo "  ${b%.css}" >&2
  done
  exit 1
fi
SUFFIX="-$(printf '%s' "$SIZE" | tr '[:lower:]' '[:upper:]')"   # -A4 / -A5

if [[ ${#GUIDES[@]} -eq 0 ]]; then
  GUIDES=("Zoneconnex INSTALL & USER MANUAL" "Zoneconnex Quick Start Guide" "Zoneconnex User Start Guide")
fi

# --- 1) throwaway copy ------------------------------------------------------
TMP="$(mktemp -d)/Zone Controller Stack"
cp -R "$SRC_DIR" "$TMP"

# --- 2) brand.py on the copy ------------------------------------------------
"$PY" "$TMP/pdf-toolkit/brand.py" "$TMP"

# --- weasyprint needs Homebrew's libgobject; venv bin first on PATH ----------
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib"
export PATH="$VENV:/opt/homebrew/bin:$PATH"

TOC_ARGS=()
if [[ $WANT_TOC -eq 1 ]]; then TOC_ARGS=(--lua-filter=pdf-toolkit/insert-toc.lua); fi

for g in "${GUIDES[@]}"; do
  out="$g$SUFFIX"
  echo "==> building: $g  (size=$SIZE, toc=$WANT_TOC)"
  # 3) pandoc: brand CSS first, page-size CSS second (cascade wins)
  ( cd "$TMP" && pandoc "$g.md" -o "$out.pdf" \
      --pdf-engine=weasyprint \
      -f markdown+raw_html \
      --css=pdf-toolkit/anywair-brand.css \
      --css="pdf-toolkit/page-$SIZE.css" \
      ${TOC_ARGS[@]+"${TOC_ARGS[@]}"} \
      --standalone )
  # 4) compress images
  "$PY" "$SCRIPT_DIR/compress.py" "$TMP/$out.pdf"
  # 5) copy back next to the source
  cp "$TMP/$out.pdf" "$SRC_DIR/pdfs/$out.pdf"
  echo "    -> $SRC_DIR/pdfs/$out.pdf"
done

echo "done."
