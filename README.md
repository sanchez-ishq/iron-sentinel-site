# Iron Sentinel — Website (deploy repo)

Public static site for **ironsentinelhq.com**. This repo contains **only public pages** —
no internal business docs, sales scripts, memory, or credentials. Hand-coded static HTML.

## Pages → routes
| File | Route |
|---|---|
| `index.html` | `/` |
| `download.html` | `/download` (free NIST template lead magnet) |
| `download-success.html` | `/download-success` (Full Kit Stripe redirect) |
| `soc2.html` | `/soc2` (SOC 2 Readiness Pack — $147) |
| `soc2-success.html` | `/soc2-success` (Stripe redirect) |
| `hipaa.html` | `/hipaa` (HIPAA Compliance Pack — $147) |
| `hipaa-success.html` | `/hipaa-success` (Stripe redirect) |

## Pending link placeholders (fill before go-live)
- `soc2.html` → `STRIPE_SOC2_PAYMENT_LINK`
- `soc2-success.html` → `GDRIVE_SOC2_LINK`
- `hipaa.html` → `STRIPE_HIPAA_PAYMENT_LINK`
- `hipaa-success.html` → `GDRIVE_HIPAA_LINK`
These are filled by the Stripe + Drive automation, then committed and pushed.

## One-time host connection (free, headless deploys after)
**Recommended host: Cloudflare Pages** (free, automatic clean URLs `/soc2`, instant deploys on push).

1. Create a GitHub repo (e.g. `iron-sentinel-site`) at github.com/new.
2. Locally, add the remote and push:
   ```
   git remote add origin https://github.com/<you>/iron-sentinel-site.git
   git push -u origin main
   ```
   (Push needs a GitHub credential — a fine-grained PAT scoped to this one repo.)
3. In Cloudflare Pages → "Connect to Git" → pick the repo → Framework preset: **None**,
   build command: *(none)*, output dir: `/`. Deploy.
4. Add the custom domain `ironsentinelhq.com` in Cloudflare Pages.

After step 1–2 are wired, every future change = `git commit` + `git push` → live in ~30s.
No more manual file uploads.

## Alternative free hosts
- **Netlify** — drag-and-drop this folder, or Git connect. Clean URLs by default.
- **GitHub Pages** — free, but `/soc2`-style clean URLs need extra config; CF Pages is simpler.

© 2026 Iron Sentinel LLC.
