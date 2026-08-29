# Zoneconnex Guides — Consistency Audit & Flags for Tech Team

**Date:** 2026-07-27
**Reference (look-and-feel source of truth):** `Zoneconnex INSTALL & USER MANUAL.md`
**Audited against it:** `Zoneconnex Quick Start Guide.md` (QSG), `Zoneconnex User Start Guide.md` (User Guide)

## Purpose

The guides are effectively "built from different sources": the same subject often uses
a *different image file, revision, annotation, size, or layout* across documents. This
document catalogs those divergences so the tech team can decide the correct version.
Per instruction: **only shared images/layout that are genuinely the same were unified;
everything that is a different asset or a wording/content difference is FLAGGED, not
changed.**

---

## ✅ Already unified this session (safe — same subject, layout only)

QSG changed to match the manual's presentation, using files confirmed to be the SAME image:

- **§3 Correct/Incorrect clip-release** — now uses the manual's single combined image
  `LCD-Clip-Release-v2.png` above a **text-only** Correct/Incorrect table (was: two
  separate photos crammed in 58 mm table cells).
- **§5.2 Wi-Fi Configuration** — screenshots now stacked one-per-step at the manual's
  size (was: two screenshots side-by-side in a 58 mm table with italic captions).
- **§4.1 / §4.2 diagrams** enlarged; **§4.2 / §4.3 cable photos** rotated to the
  manual's orientation; **§4.4** switched to the manual's zoomed-sticker image.
  *(from earlier in this work session)*

### Resolved 2026-08-20

- **UART diagram — standardised on `ACB-ZC-UART-PAP-04V-S-rev3.png`** (was rev2 in the
  manual, rev3 in the QSG). This was not only a formatting difference: the two revisions
  stated **different cable lengths** — rev2 "Length: 2m", rev3 "Length: 5m\*" — so the two
  guides were shipping conflicting specs for the same part. rev3 also has correctly
  aligned right-hand pin labels and no baked-in whitespace (rev2's canvas was 3508x2480
  for 3106x691 of content — 75% empty, which made the diagram render small and
  visually adrift on manual p18). Manual now points at rev3.
  **Confirm 5m is the correct current spec** — the change was made on that assumption.

---

## 🚩 FLAGGED — different actual assets (NOT changed; tech team to choose the correct one)

These look different because they are **genuinely different image files**, not the same
image in another format/size. Unifying would mean picking a winner and possibly
downgrading a newer asset — an editorial call.

| Subject | Manual uses | Other guide uses | Why flagged |
|---|---|---|---|
| Component views (Front/Top/Bottom) | `ACB-ZC-Components-Markup-*-View.png` | QSG: `…-View-rev3.png` | **Pixels differ** — QSG is a newer rev. Which rev is current? |
| 24 VAC power adaptor | `24VAC-ADAPTOR-rev3.png` | QSG: `24VAC-ADAPTOR-BOLD-2.png` | Different files entirely (807×533 vs 1518×718). |
| UART cable photo | `UART-Cable.png` | QSG: `UART-Cable-photo.jpg` | Same size, **pixels differ** — different photo. |
| LCD cable photo | `LCD-Cable.jpg` | QSG: `LCD-Cable-photo.jpg` | Same size, **pixels differ** — different photo. |
| Android app QR | `Andriod-anywair-zone-qr-code.png` | QSG: `googleplay-qr-code.png` | Different QR files — must confirm both encode the correct Play Store URL. |
| Wi-Fi / LCD screenshots (User Guide) | `*.png` `-v2` annotated (e.g. `Scan-Wi-Fi-v2.png` with **two** labelled callouts) | User Guide: `*.svg` (e.g. `Scan-Wi-Fi.svg` with **one** callout) | **Different annotated versions**, not just PNG-vs-SVG. Applies to Scan-Wi-Fi, Wi-Fi-Connected(-info), Main-Controls, Zone-Control, Schedule-Screen-1/2, Schedule-Settings, Scene-Settings. Which annotation set is correct? |
| Installer-mode screenshots (QSG) | `Tap-Settings-Card.png`, `Installer-Connection-step1/2.png` | QSG: `Tap-Settings-8x-Card.svg`, `Installer-Connection-LeftQR/RightQR.svg` | Different files & annotation. |

---

## 🚩 FLAGGED — content / wording conflicts (tech team decides; NOT changed)

Genuine contradictions, not terseness — one side may be wrong:

1. **Installer-mode icon (contradiction):** Manual says tap the **"System Info"** icon;
   QSG says tap the **"Settings"** icon — same step, different instruction.
2. **Zone terminology (contradiction):** Manual says **"relief zones"**; QSG introduces
   **"Constant Zones"** at the same configuration step.
3. **Product-term spelling:** "Wi-Fi" (manual) vs "Wifi" (QSG heading §5.2).
4. **User-facing labels drift (User Guide vs manual):** "Operation" vs "Power";
   "Zone Enable" vs "Zone On/Off"; "Home Controls" vs "Main Controls";
   "Current Temperature Display" vs "Temperature Display".
5. **Exit-installer wording:** manual lists `Finish Installation` OR `Exit Installer Mode`;
   QSG lists only `Exit Installer Mode`.
6. Minor: en-dash vs em-dash in bullet lists; `LoRa Antenna` vs `LoRa® Antenna`.

---

## 🚩 FLAGGED — path casing / deploy risk (mechanical; in the MANUAL, not changed)

These only work on macOS (case-insensitive) and **will break on the Linux web deploy**:

- Manual references `Touch%20point%20LCD/…` (lowercase "point"); on disk the folder is
  `Touch Point LCD` (capital). e.g. manual lines for `LCD-Stickered-Internal-Zoomed`,
  `Scan-wi-fi-v2.png`.
- Manual references `Scan-wi-fi-v2.png` (lowercase) but on-disk file is `Scan-Wi-Fi-v2.png`.

Recommend the tech team fix the *manual's* references to match the on-disk casing (or
rename files) as a dedicated pass. Left untouched here because it edits the manual.

---

## Note on the "source of truth"

The manual is the agreed look-and-feel reference, but it is **not error-free**: it
contains a **duplicate section number "4.2"** (two different sections both numbered 4.2),
whereas the QSG's 4.1–4.4 sequence is internally correct. Flagging so the numbering fix
isn't lost.
