#!/usr/bin/env bash
# ============================================================
# build.sh — canonical branded PDF build.
#
# Product-specific facts (which guides exist, their cover text, images, model
# number, which get a TOC, which skin to use) all live in project.toml. This
# script names no document and no brand.
#
# Page size is a first-class argument. A5 is the print deliverable and is
# BUILT at A5 — nothing is ever shrunk to reach a format. A4 is screen /
# desk reference only. Every output filename ends in -A4 or -A5.
#
# The Table of Contents is OPTIONAL — off by default, add --toc. The two short
# guides are excluded from it by name (see NO_TOC_GUIDES below), so in practice
# only the INSTALL & USER MANUAL ever gets a Contents page.
#
# Usage (run from the repo root OR this folder):
#   pdf-toolkit/build.sh                       # all guides, A5, no TOC
#   pdf-toolkit/build.sh --a4                  # all guides, A4
#   pdf-toolkit/build.sh --toc                 # A5 with a TOC page
#   pdf-toolkit/build.sh --a4 "Quick Start Guide"    # one guide, by basename
#   pdf-toolkit/build.sh --size a5 --toc "Install & User Manual"
#
# CSS layer order (cascade matters):
#   engine.css          layout + structure, brand-neutral
#   <oem>-skin.css      colour, type, cover chrome   ([brand].css in project.toml)
#   page-<size>.css     page size, margins, type scale, image scale
# Page size comes from the CSS @page rule only — there is deliberately no
# -V papersize flag, so the two can never disagree.
#
# What it does (see INSTRUCTIONS.md for the passes brand.py runs):
#   1. copies the source folder to a throwaway temp dir
#   2. runs brand.py on the copy (flatten transparent PNGs, rasterize SVGs,
#      strip U+FE0F, alt-tag -> attributes, cover + back page)
#   3. pandoc + weasyprint with engine.css, then the skin, then page-<size>.css
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

# Guide list and per-guide settings come from project.toml — the only file that
# knows anything product-specific. Nothing below hardcodes a document name.
MANIFEST="$SCRIPT_DIR/project.toml"
if [[ ! -f "$MANIFEST" ]]; then
  echo "error: no project.toml in $SCRIPT_DIR" >&2
  exit 1
fi

# Stylesheet layer names come from [brand] in the manifest, so a different OEM
# is a manifest edit, not a build.sh edit.
ENGINE_CSS="$("$PY" -c 'import sys,tomllib;print(tomllib.load(open(sys.argv[1],"rb"))["brand"].get("engine","engine.css"))' "$MANIFEST")"
SKIN_CSS="$("$PY" -c 'import sys,tomllib;print(tomllib.load(open(sys.argv[1],"rb"))["brand"]["css"])' "$MANIFEST")"
for css in "$ENGINE_CSS" "$SKIN_CSS"; do
  if [[ ! -f "$SCRIPT_DIR/$css" ]]; then
    echo "error: stylesheet '$css' referenced by project.toml not found in $SCRIPT_DIR" >&2
    exit 1
  fi
done

if [[ ${#GUIDES[@]} -eq 0 ]]; then
  while IFS= read -r line; do GUIDES+=("$line"); done < <(
    "$PY" - "$MANIFEST" <<'PYEOF'
import sys, tomllib
m = tomllib.load(open(sys.argv[1], "rb"))
for g in m["guides"]:
    print(g["file"].removesuffix(".md"))
PYEOF
  )
fi

# --- 1) throwaway copy ------------------------------------------------------
# brand.py rewrites .md in place, so the build always runs on a copy — never
# against the source folder. The copy keeps the source folder's own name.
TMP="$(mktemp -d)/$(basename "$SRC_DIR")"
cp -R "$SRC_DIR" "$TMP"

# --- 2) brand.py on the copy ------------------------------------------------
# $SIZE is passed through: phone screenshots are packed N-per-row in the HTML,
# and N depends on the page width (see SCREENSHOTS_PER_ROW in brand.py).
"$PY" "$TMP/pdf-toolkit/brand.py" "$TMP" "$SIZE"

# --- weasyprint needs Homebrew's libgobject; venv bin first on PATH ----------
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib"
export PATH="$VENV:/opt/homebrew/bin:$PATH"

# Guides that never get a Contents page, even with --toc — the `toc = false`
# entries in project.toml. Short fold-out guides opt out: a TOC costs each of
# them a whole page and earns nothing at that length.
# NOTE guides may share a cover TITLE and be told apart only by subtitle, so the
# manifest matches on FILENAME, never on anything shown on the cover.
NO_TOC_GUIDES=()
while IFS= read -r line; do NO_TOC_GUIDES+=("$line"); done < <(
  "$PY" - "$MANIFEST" <<'PYEOF'
import sys, tomllib
m = tomllib.load(open(sys.argv[1], "rb"))
for g in m["guides"]:
    if not g.get("toc", False):
        print(g["file"].removesuffix(".md"))
PYEOF
)

for g in "${GUIDES[@]}"; do
  # Output is always a flat name in pdfs/, even for a guide in a subfolder.
  out="$(basename "$g")$SUFFIX"
  # TOC is decided per guide: the global --toc flag, minus the opt-outs above.
  guide_toc=$WANT_TOC
  for skip in "${NO_TOC_GUIDES[@]}"; do
    if [[ "$g" == "$skip" ]]; then guide_toc=0; fi
  done
  echo "==> building: $g  (size=$SIZE, toc=$guide_toc)"
  # Guides may live in a subfolder. Pandoc runs in the guide's OWN directory so
  # that its relative image refs (img/…, screenshots/…) resolve against its own
  # assets — a root-relative build picks up same-named files from the root's
  # img/ instead. CSS and lua paths climb back out by the same depth, matching
  # toolkit_prefix() in brand.py.
  guide_dir="$(dirname "$g")"
  guide_base="$(basename "$g")"
  UP=""
  if [[ "$guide_dir" != "." ]]; then
    depth=$(printf '%s' "$guide_dir" | awk -F/ '{print NF}')
    for ((d = 0; d < depth; d++)); do UP="../$UP"; done
  fi
  TOC_ARGS=()
  if [[ $guide_toc -eq 1 ]]; then TOC_ARGS=(--lua-filter="${UP}pdf-toolkit/insert-toc.lua"); fi
  # 3) pandoc: brand CSS first, page-size CSS second (cascade wins)
  ( cd "$TMP/$guide_dir" && pandoc "$guide_base.md" -o "$guide_base.pdf" \
      --pdf-engine=weasyprint \
      -f markdown+raw_html \
      --css="${UP}pdf-toolkit/$ENGINE_CSS" \
      --css="${UP}pdf-toolkit/$SKIN_CSS" \
      --css="${UP}pdf-toolkit/page-$SIZE.css" \
      ${TOC_ARGS[@]+"${TOC_ARGS[@]}"} \
      --standalone )
  # 4) compress images
  "$PY" "$SCRIPT_DIR/compress.py" "$TMP/$guide_dir/$guide_base.pdf"
  # 5) copy back next to the source, under the -A4/-A5 output name
  cp "$TMP/$guide_dir/$guide_base.pdf" "$SRC_DIR/pdfs/$out.pdf"
  echo "    -> $SRC_DIR/pdfs/$out.pdf"
done

echo "done."
