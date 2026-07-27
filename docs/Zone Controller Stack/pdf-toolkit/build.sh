#!/usr/bin/env bash
# ============================================================
# build.sh — canonical Zoneconnex / MIA PDF build.
#
# Produces the PRINT-DENSITY PDFs (title + intro flow together, no page
# stranded before every H1, tighter images/spacing). The Table of Contents
# is OPTIONAL — off by default, add --toc to include it.
#
# Usage (run from the repo root OR this folder):
#   pdf-toolkit/build.sh                 # all guides, dense, no TOC
#   pdf-toolkit/build.sh --toc           # all guides, dense, WITH a TOC page
#   pdf-toolkit/build.sh "Zoneconnex Quick Start Guide"      # one guide
#   pdf-toolkit/build.sh --toc "Zoneconnex INSTALL & USER MANUAL"
#
# What it does (see INSTRUCTIONS.md for the passes brand.py runs):
#   1. copies "Zone Controller Stack" to a throwaway temp dir
#   2. runs brand.py on the copy (flatten transparent PNGs, rasterize SVGs,
#      strip U+FE0F, alt-tag -> attributes, cover + back page)
#   3. pandoc + weasyprint with anywair-brand.css THEN anywair-print.css
#      (print layer wins by cascade order); insert-toc.lua only with --toc
#   4. compresses images (PyMuPDF: cap 1800px, JPEG q82, white-composite)
#   5. copies the finished PDF into docs/Zone Controller Stack/pdfs/
# ============================================================
set -euo pipefail

# --- locate the toolkit + source folder regardless of CWD -------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"      # .../pdf-toolkit
SRC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"                          # .../Zone Controller Stack
VENV="$SCRIPT_DIR/.venv/bin"
PY="$VENV/python"

# --- args: --toc flag + optional list of guide basenames --------------------
WANT_TOC=0
GUIDES=()
for a in "$@"; do
  if [[ "$a" == "--toc" ]]; then WANT_TOC=1; else GUIDES+=("$a"); fi
done
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
  echo "==> building: $g  (toc=$WANT_TOC)"
  # 3) pandoc: brand CSS first, print-density CSS second (cascade wins)
  ( cd "$TMP" && pandoc "$g.md" -o "$g.pdf" \
      --pdf-engine=weasyprint \
      --css=pdf-toolkit/anywair-brand.css \
      --css=pdf-toolkit/anywair-print.css \
      ${TOC_ARGS[@]+"${TOC_ARGS[@]}"} \
      --standalone )
  # 4) compress images
  "$PY" "$SCRIPT_DIR/compress.py" "$TMP/$g.pdf"
  # 5) copy back next to the source
  cp "$TMP/$g.pdf" "$SRC_DIR/pdfs/$g.pdf"
  echo "    -> $SRC_DIR/pdfs/$g.pdf"
done

echo "done."
