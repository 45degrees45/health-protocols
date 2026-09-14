# Amazon Health Links — Design Spec
**Date:** 2026-09-14
**GitHub Pages URL:** https://45degrees45.github.io/health-protocols/

---

## Overview

A GitHub Pages website that publishes personal health + environmental product protocols with full research backing, designed for sharing across Reddit, Instagram, and WhatsApp. Products are sourced from Amazon (via Amazon Associates affiliate links). Content is also exported as downloadable PDFs per protocol.

---

## Goals

- Share 15–40 curated health + environmental Amazon products across 3 distinct protocols
- Back every product with research summaries and deep-dive pages
- Enable one-tap sharing via WhatsApp (link + PDF) and Instagram (caption + link)
- Post each protocol to the most relevant Reddit community
- Host everything free on GitHub Pages with no server required

---

## Protocols

| Protocol | Audience | Reddit Target |
|---|---|---|
| My Protocol | Personal daily stack | r/Supplements, r/Nootropics, r/biohacking |
| Mum Protocol | Adapted for mother's needs | r/Supplements, r/HealthHacks |
| Vegan Protocol | Plant-based alternatives only | r/vegan, r/PlantBasedDiet, r/Nootropics |

---

## Repo Structure

```
health-protocols/
│
├── index.html                  ← homepage, links to all 3 protocols + research hub
├── my-protocol.html            ← personal protocol page
├── mum-protocol.html           ← mother's protocol page
├── vegan-protocol.html         ← vegan protocol page
│
├── research/
│   ├── index.html              ← research hub listing all product deep-dives
│   └── [product-name].html    ← one page per product (15–40 pages)
│
├── social/
│   ├── ig-captions.md         ← copy-paste Instagram captions per protocol
│   └── whatsapp-messages.md   ← copy-paste WhatsApp messages per protocol
│
├── pdfs/
│   ├── my-protocol.pdf
│   ├── mum-protocol.pdf
│   └── vegan-protocol.pdf
│
├── assets/
│   └── style.css              ← clean, minimal shared styling
│
└── docs/
    └── superpowers/specs/     ← this file lives here
```

---

## Page Layouts

### Protocol Pages (my-protocol.html, mum-protocol.html, vegan-protocol.html)

Each protocol page contains these sections in order:

1. **Header** — protocol name + one-line tagline
2. **TL;DR box** — 3–5 bullet summary (highlighted, visible immediately on load)
3. **Why This Protocol** — 1 paragraph of personal reasoning/context
4. **Product Table** — columns: Product Name | Why I Use It | Amazon Link (affiliate button)
5. **YouTube Videos** — thumbnails or titled links to relevant videos
6. **Deep Research** — links to individual `/research/[product].html` pages
7. **Download PDF** — button linking to `/pdfs/[protocol].pdf`
8. **Footer** — WhatsApp share button + copy link button

### Research Pages (/research/[product-name].html)

Each product gets a standalone deep-dive page:

1. **What It Is** — brief plain-English description
2. **The Science** — studies, mechanisms, key findings (cited)
3. **My Reasons** — personal experience or rationale
4. **TL;DR** — 2–3 sentence summary box
5. **YouTube Links** — relevant videos on this specific product
6. **Amazon Link** — affiliate buy button
7. **Used In** — badges showing which protocols include this product (My / Mum / Vegan)

### Homepage (index.html)

- Title + tagline
- 3 protocol cards (image, name, short description, link)
- Link to Research Hub
- Brief "About This Site" paragraph

### Research Hub (/research/index.html)

- Grid of all products (name, category, which protocols)
- Filter by: Health / Environmental / All protocols

---

## Social Assets

### /social/ig-captions.md

One caption per protocol. Format:
```
[1-2 emoji] [Hook line about the protocol]
Full research + Amazon links below 👇
https://45degrees45.github.io/health-protocols/[protocol].html
#health #supplements #biohacking [relevant tags]
```

### /social/whatsapp-messages.md

One message per protocol. Format:
```
Hey! Here's the [protocol name] with full research and Amazon links:
[URL]

PDF to save offline:
[PDF URL]
```

---

## PDF Generation

- One PDF per protocol, generated from the protocol HTML page
- Tool: browser print-to-PDF or a simple Python script using `weasyprint`
- PDFs stored in `/pdfs/` and committed to the repo
- Regenerated whenever protocol content changes

---

## Amazon Associates

- Site registered under: https://45degrees45.github.io/health-protocols/
- All product links use Amazon Associates affiliate tags
- Each product link format: `https://www.amazon.com/dp/[ASIN]?tag=[associate-tag]`

---

## Implementation Phases

### Phase 1 — Repo + Site Scaffold
- Create GitHub repo `health-protocols` under `45degreesolutions`
- Set up GitHub Pages
- Build HTML/CSS scaffold (homepage + 3 protocol pages + research hub shell)

### Phase 2 — Product Research
- For each of the 15–40 products: find Amazon link, gather research, collect YouTube videos
- Populate each `/research/[product].html` page

### Phase 3 — Protocol Content
- Fill in all 3 protocol pages with product tables, TL;DRs, YouTube links
- Cross-link to research pages

### Phase 4 — Social Assets + PDFs
- Write IG captions and WhatsApp messages in `/social/`
- Generate 3 PDFs

### Phase 5 — Reddit Posts
- Draft one post per protocol targeted at the correct subreddit
- Post with link to the relevant protocol page

---

## Success Criteria

- All 3 protocol pages live and accessible at their GitHub Pages URLs
- Each product has a research page with science + YouTube links
- PDFs downloadable from each protocol page
- Social copy ready to paste for IG and WhatsApp
- Amazon Associates links working with affiliate tag
