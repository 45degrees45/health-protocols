#!/usr/bin/env python3
"""Generate protocol pages for each person in data/people.json.
Run: python3 build.py
Generated files: {slug}-protocol.html in the project root.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
TAG = '45degrees45-21'


def amazon_url(asin):
    if asin:
        return f'https://www.amazon.in/dp/{asin}?tag={TAG}'
    return f'https://www.amazon.in/?tag={TAG}'


def product_row_div(p):
    url = amazon_url(p.get('asin'))
    asin = p.get('asin', '')
    img_src = f'assets/images/products/{asin}.jpg' if asin else ''
    note_html = ''
    if p.get('note'):
        note_html = f'\n          <small>{p["note"]}</small>'
    research = p.get('research', '#')
    research_link = ''
    if research and research != '#':
        research_link = f'\n        <a href="{research}" class="btn-research">Research</a>'
    return f'''    <div class="product-row">
      <img class="product-img" src="{img_src}" alt="" onerror="this.style.display='none'">
      <div class="product-text">
        <div class="product-name">{p["name"]}{note_html}</div>
        <div class="product-why">{p["why"]}</div>
      </div>
      <div class="product-actions">
        <a href="{url}" class="btn-buy">Order →</a>{research_link}
      </div>
    </div>'''


def section_block(section, products_data):
    rows = '\n'.join(product_row_div(products_data[pid]) for pid in section['products'] if pid in products_data)
    return f'''  <div class="section-label">{section["title"]}</div>
  <div class="product-grid">
{rows}
  </div>'''


def tldr_items(items):
    return '\n'.join(f'      <li>{item}</li>' for item in items)


def build_page(slug, person, products_data):
    sections_html = '\n\n'.join(section_block(s, products_data) for s in person['sections'])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{person["display"]} | 45 Degrees</title>
  <meta name="description" content="{person["subtitle"]} — with research, Amazon links, and personalised notes.">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>

<nav>
  <span class="logo">45° Health</span>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="{slug}-protocol.html">{person["display"]}</a></li>
    <li><a href="research/index.html">Research</a></li>
  </ul>
</nav>

<div class="page-header">
  <h1>{person["display"]}</h1>
  <p>{person["subtitle"]}</p>
</div>

<div class="container">

  <div class="tldr">
    <h3>TL;DR</h3>
    <ul>
{tldr_items(person["tldr"])}
    </ul>
  </div>

{sections_html}

  <div class="share-bar">
    <span>Share this protocol</span>
    <button onclick="navigator.clipboard.writeText(window.location.href); this.textContent='Copied!';" class="btn btn-outline">Copy Link</button>
  </div>

</div>

<footer>
  <p>Built with research and care. Amazon.in affiliate links (ID: {TAG}) — they cost you nothing extra.</p>
</footer>

<script src="assets/tracker.js"></script>
</body>
</html>
'''


def main():
    products_data = json.loads((ROOT / 'data' / 'products.json').read_text())
    people_data = json.loads((ROOT / 'data' / 'people.json').read_text())

    for slug, person in people_data.items():
        html = build_page(slug, person, products_data)
        out = ROOT / f'{slug}-protocol.html'
        out.write_text(html)
        print(f'Built {out.name}')

    print(f'\nDone — {len(people_data)} pages generated.')


if __name__ == '__main__':
    main()
