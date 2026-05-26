# liquidsuncreative.com

Static site for `liquidsuncreative.com`, hosted on GitHub Pages. The domain is registered at GoDaddy and pointed here via DNS.

## Layout

```
/
├── CNAME           (liquidsuncreative.com)
├── .nojekyll       (skip Jekyll processing)
├── robots.txt      (allows all crawlers, points to sitemap)
├── sitemap.xml     (hand-maintained — add a <url> per new page)
├── favicon.svg     (LSC sunburst mark)
├── 404.html        (branded not-found page)
└── index.html      (homepage — currently a coming-soon placeholder)
```

## Status

This is the placeholder shipped during the Squarespace → GitHub Pages migration. The full site replaces `index.html` (and adds new pages + sitemap entries) when it's ready.

## Deploys

Push to `main`. GitHub Pages serves from the root. There is no build step — files go live as-is.

## SEO

`index.html` carries `viewport`, `description`, canonical, Open Graph, Twitter Card, and a `ProfessionalService` JSON-LD block (re-homed from `gissentanna.com/matthew/`). Analytics (GA4 / GTM) is intentionally not wired up yet.

TODO once the real site ships: add an `og:image` (1200×630 PNG) for proper social link previews.

## Brand

Colors and typography follow the **LSC Brand Guide**:
- **§4.1 Palette** — Ink `#1B1714` · Linen `#F6F0E0` · Golden `#D0A500` · Gamma `#F85D00` · Dusk `#EB701E`
- **§4.4 Type** — Alata (display, with Sofia Pro fallback) · IBM Plex Mono (technical)

Dark mode follows `prefers-color-scheme` — Linen-on-Ink by day, Ink-on-Linen flipped at night.
