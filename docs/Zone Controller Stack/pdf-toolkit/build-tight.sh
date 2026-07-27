#!/usr/bin/env bash
# ============================================================
# build-tight.sh — TIGHTER print-density Zoneconnex PDF build.
#
# Same 1.4 content as build.sh, but uses anywair-print-tight.css so the
# vertical white space is moderately compressed, and writes to NEW files
# with a " (print)" suffix. The current PDFs and build.sh are NEVER touched.
#
# Usage (run from the repo root OR this folder):
#   pdf-toolkit/build-tight.sh                 # default: the two named guides
#   pdf-toolkit/build-tight.sh "Zoneconnex Quick Start Guide"   # one guide
#
# Output example:  pdfs/Zoneconnex Quick Start Guide (print).pdf
#
# Passes (identical to build.sh except CSS + output name):
#   1. copies "Zone Controller Stack" to a throwaway temp dir
#   2. runs brand.py on the copy
#   3. pandoc + weasyprint with anywair-brand.css THEN anywair-print-tight.css
#   4. compresses images (PyMuPDF)
#   5. copies the finished PDF into docs/Zone Controller Stack/pdfs/ as "<name> (print).pdf"
# ============================================================
set -euo pipefail

# --- locate the toolkit + source folder regardless of CWD -------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"      # .../pdf-toolkit
SRC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"                          # .../Zone Controller Stack
VENV="$SCRIPT_DIR/.venv/bin"
PY="$VENV/python"

SUFFIX=" (print)"

# --- args: optional list of guide basenames --------------------------------
GUIDES=("$@")
if [[ ${#GUIDES[@]} -eq 0 ]]; then
  GUIDES=("Zoneconnex INSTALL & USER MANUAL" "Zoneconnex Quick Start Guide")
fi

# --- 1) throwaway copy ------------------------------------------------------
TMP="$(mktemp -d)/Zone Controller Stack"
cp -R "$SRC_DIR" "$TMP"

# --- 2) brand.py on the copy ------------------------------------------------
"$PY" "$TMP/pdf-toolkit/brand.py" "$TMP"

# --- 2b) tight-only: pair the stacked retaining-clip diagrams side-by-side ----
#         (post-process, runs ONLY here — brand.py / normal build untouched)
"$PY" "$SCRIPT_DIR/pair-images-tight.py" "$TMP"/*.md

# --- weasyprint needs Homebrew's libgobject; venv bin first on PATH ----------
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib"
export PATH="$VENV:/opt/homebrew/bin:$PATH"

for g in "${GUIDES[@]}"; do
  echo "==> building (tight): $g$SUFFIX"
  # 3) pandoc: brand CSS first, TIGHT print-density CSS second (cascade wins)
  ( cd "$TMP" && pandoc "$g.md" -o "$g$SUFFIX.pdf" \
      --pdf-engine=weasyprint \
      --css=pdf-toolkit/anywair-brand.css \
      --css=pdf-toolkit/anywair-print-tight.css \
      --standalone )
  # 4) compress images
  "$PY" "$SCRIPT_DIR/compress.py" "$TMP/$g$SUFFIX.pdf"
  # 5) copy back next to the source, as a NEW file
  cp "$TMP/$g$SUFFIX.pdf" "$SRC_DIR/pdfs/$g$SUFFIX.pdf"
  echo "    -> $SRC_DIR/pdfs/$g$SUFFIX.pdf"
done

echo "done."
