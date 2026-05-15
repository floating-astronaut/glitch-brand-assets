# Changelog — `glitch-brand-assets`

Auto-regenerated from `git log` by `/home/support/bin/changelog-regen`,
called before every push by `/home/support/bin/git-sync-all` (cron `*/15 * * * *`).

**Purpose:** traceability. If a push broke something, scan dates + short SHAs
here; then `git show <sha>` to see the diff, `git revert <sha>` to undo.

**Format:** UTC dates, newest first. Each entry: `time — subject (sha) — N files`.
Body text (if present) shown as indented sub-bullets.

---

## 2026-05-16

- **02:45 UTC** — brand: refresh canonical Cyber Cobra mascot (2026-05 variant) (`6a54941`) — 15 files
    Operator uploaded a higher-fidelity cobra render — better detail on
    the circuit-trace tessellation, cleaner ouroboros shape. This is the
    canonical source for Trade / Edge / Grow going forward.
      mascot/raw/cobra-mascot-2026-05.png       new source (512x512 RGB)
      mascot/raw/cobra-mascot-transparent.png   re-keyed RGBA version
      mascot/web/mascot-{64,256,512,1024}.png   regenerated sizes
      favicon/favicon.ico + favicon-{16,32,48}  new multi-res icons
      favicon/apple-touch-icon.png              180x180
      favicon/icon-{192,512}.png                PWA sizes
      og/og-image.png                           1200x630 social card with

## 2026-04-22

- **10:01 UTC** — feat(og): GitHub social preview images for 17 public repos (`8e61d08`) — 18 files
    1280×640 PNGs generated via generate_repo_social.py, one per public
    repo in glitch-exec-labs. Per-product-line accent colors (Grow green,
    Trade amber, Edge blue) over the shared cobra mascot + Glitch wordmark.
    Upload path per repo: github.com/<org>/<repo>/settings → Social preview.

## 2026-04-20

- **22:54 UTC** — Update docs after public repo renames (`b33c3b8`) — 1 file
- **22:37 UTC** — Polish branding for Glitch Executor Labs public positioning (`1294dfb`) — 1 file

## 2026-04-16

- **03:42 UTC** — Initial brand assets: cyber cobra mascot + variants (`8a6d611`) — 18 files
    - Source: 1200x1200 cobra mascot in ouroboros coil
    - Generated: 5 mascot sizes, 3 favicons + ico, apple-touch-icon, 2 PWA icons, OG image
    - Brand guidelines: color palette, typography, lockup rules
    - generate.py: regenerate all variants from source
    The cobra ties into the existing Glitch trading bot lineage
    (Viper, Cobra, Mamba, Anaconda, Hydra, Taipan, Indian King Cobra,
    Terciopelo) and the ouroboros-snake-strategy flagship repo.
    Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
