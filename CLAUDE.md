# CLAUDE.md — iron-sentinel-site

Guidance for Claude Code working in this repo.

## What this is
A **static HTML marketing/landing site** for Iron Sentinel (a GRC / security & compliance advisory firm). No build step, no framework — plain `.html` files served as-is.

Top-level pages: `index.html`, plus offer/landing pages (`ai.html`, `hipaa.html`, `soc2.html`, `soc2-checklist.html`, `download.html`) and their `*-success.html` counterparts, `robots.txt`, `logo.png`. The `training/` directory holds the **CompTIA SecAI+ study kit** (modules, question banks, flashcards, and a local `lab/`) — study material, not part of the website.

## Hosting & deployment
- **Host: Cloudflare Pages**, project **`iron-sentinel-site`** (`iron-sentinel-site.pages.dev`), connected to this GitHub repo.
- **Deploys on push to the default branch** (`main`) — Cloudflare Pages auto-publishes the static files. No manual build/deploy.
- Plan: Cloudflare **Free**.

## Domain & DNS (as of 2026-06-15)
- **DNS is hosted on Cloudflare** (nameservers `alberto.ns.cloudflare.com` / `lisa.ns.cloudflare.com`). The registrar is **Name.com** (registrar only — make DNS changes in **Cloudflare**, not Name.com).
- **Both the apex and www serve the site over HTTPS:**
  - `ironsentinelhq.com` → proxied CNAME → `iron-sentinel-site.pages.dev`
  - `www.ironsentinelhq.com` → proxied CNAME → `iron-sentinel-site.pages.dev`
  - Both are registered as **Pages custom domains**; Cloudflare issues the TLS cert; `http` auto-redirects to `https`.
- Canonical host is currently **not forced** — apex and www both serve. (Optional future: a Cloudflare Redirect Rule to make one canonical.)

## Email — DO NOT BREAK
The domain uses **Google Workspace** email. These records live in the Cloudflare DNS zone and **must be preserved** on any DNS change:
- **MX (5):** `aspmx.l.google.com` (priority 1), `alt1`/`alt2.aspmx.l.google.com` (5), `alt3`/`alt4.aspmx.l.google.com` (10)
- **TXT:** SPF `v=spf1 include:_spf.google.com ~all`, and a `google-site-verification=...` record

## Gotchas / history
- The site was **migrated off an old Netlify setup** to Cloudflare Pages. If you see references to `*.netlify.app` or IP `75.2.60.5`, that's stale.
- A bare-domain `https` apex previously didn't work because DNS was on Name.com (whose URL-forwarding has no apex SSL). It was fixed by moving DNS to Cloudflare and serving the apex directly via Pages. Don't revert DNS to Name.com URL-forwarding — it can't do `https` on the apex.
- Operational identifiers (Cloudflare account/zone IDs, API tokens) are intentionally **kept out of this repo** (public). They live in private/local notes.

## Conventions
- Edit the relevant `.html` file directly; keep changes consistent with the existing markup/voice.
- Pushing to `main` deploys to production — branch for changes and open a PR rather than committing straight to `main`.
- Keep compliance claims accurate and disclaimers intact (this is a security/compliance firm's site).
