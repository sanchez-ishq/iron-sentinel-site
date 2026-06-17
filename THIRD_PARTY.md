# Third-Party Dependency Inventory (SBOM-lite)

Provenance record for all third-party code and assets associated with this
repository, maintained under Iron Sentinel's **Software IP & Open-Source License
Compliance Policy** (internal). Updated whenever a dependency or third-party
asset is added or removed.

**Repo:** `iron-sentinel-site` (static marketing site + SecAI+ study kit)
**Last reviewed:** 2026-06-16

---

## Summary

**No third-party source code is bundled, vendored, or copied into this repository.**

- No package manifests (`package.json`, `requirements.txt`, lockfiles) — nothing is installed.
- No JavaScript or CSS library files; all HTML/CSS is hand-authored, styles inline.
- The Python tools in `training/comptia-secai-plus/lab/` use the **Python standard library only**.

The only third parties involved are (a) services the browser loads at runtime from
the vendor's own CDN, and (b) plain hyperlinks to hosted services. Neither copies
third-party code into this repo.

## Bundled / vendored code

| Component | Version | Source | License | Notes |
|-----------|---------|--------|---------|-------|
| _(none)_ | — | — | — | No third-party code is bundled or vendored. |

## Python tools (`training/comptia-secai-plus/lab/`)

| Module | Imports | License | Notes |
|--------|---------|---------|-------|
| `quiz.py`, `flashcards.py`, `injection_demo.py` | `argparse, glob, json, os, random, re, sys, urllib` (stdlib) | PSF License (Python) | Standard library only — no pip installs, no third-party packages. |

## Third-party assets loaded at runtime (not copied into repo)

| Asset | Loaded from | License / Terms | Use |
|-------|-------------|-----------------|-----|
| **Google Fonts** — DM Sans, DM Serif Display | `fonts.googleapis.com` | Fonts: SIL Open Font License 1.1; API/CSS: Apache-2.0 | Web typography, referenced via `<link>`. Permitted; no copying. |
| **Calendly scheduling widget** | `assets.calendly.com` (`widget.js` / `widget.css`) | Proprietary (Calendly), used per Calendly Terms of Service | Booking embed; vendor-hosted, loaded at runtime. Not redistributed. |

## External service links (hyperlinks only — not code or assets)

| Service | Link | Notes |
|---------|------|-------|
| Stripe Checkout | `buy.stripe.com/...` | Payment links to Stripe-hosted checkout. No Stripe code in repo. |
| Google Drive | `drive.google.com/...` | Delivery folder link. |
| LinkedIn | `linkedin.com/in/...` | Profile link. |

---

## License posture

All third-party assets in use fall on the **permitted-license allowlist** (OFL,
Apache-2.0, PSF) or are vendor-hosted SaaS used under their terms of service. No
copyleft (GPL/AGPL/LGPL), no unlicensed, and no source-available/non-commercial
code is present. Should that change, the new dependency is recorded above and —
if copyleft or unknown — routed to GC for review before use, per policy.

> **Maintenance:** add a row here in the same PR that introduces any new
> dependency, font, embed, or vendored file. The QC gate's *code-provenance*
> check verifies this file is current before a code-bearing change ships.
