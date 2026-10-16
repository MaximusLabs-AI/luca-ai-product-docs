# Luca AI product documentation · Version 1

Fumadocs (Next.js static export) site, modelled on the EasyWebinar product-docs beta. 49 pages, 101 documented capabilities.

**Rule:** v1 documents only what MaximusLabs is certain Luca has today (85 available, 16 available with a stated limited scope), each with dated evidence. Everything else is in the worksheet for Luca's team (`public/downloads/luca-ai-product-parameters-to-confirm.xlsx`).

## Source of truth
- `source/spec.py` — page map, documented capabilities, facts and sources. Edit here first.
- `source/prose/out-*.json` — page and capability text, written strictly from the spec facts.
- `source/build.py` — assembles `lib/content.json` + downloads and scans for banned claims (autonomy, alerts, forecasting, memory, capital terms, prices, certifications, residency).
- `source/build_worksheet.py` — builds the client worksheet from the 612-parameter inventory in the vault.

## Build
```
python3 source/build.py && node scripts/prepare-site.mjs && npm run build && python3 scripts/verify-export.py
```
For GitHub Pages set `NEXT_PUBLIC_BASE_PATH` and `NEXT_PUBLIC_SITE_URL` first. robots.txt and page metadata are noindex for the review period.
