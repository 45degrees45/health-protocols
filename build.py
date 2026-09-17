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


def product_row(p):
    url = amazon_url(p.get('asin'))
    note_html = ''
    if p.get('note'):
        note_html = f' <small style="color:#6b7280">⚠️ {p["note"]}</small>'
    research = p.get('research', '#')
    research_link = f'<a href="{research}">Deep dive →</a>' if research != '#' else '—'
    return f'''      <tr>
        <td><strong>{p["name"]}</strong>{note_html}</td>
        <td>{p["why"]}</td>
        <td>{research_link}</td>
        <td><a href="{url}" class="btn btn-amazon btn-sm">Buy →</a></td>
      </tr>'''


def section_table(section, products_data):
    col = section.get('col_header', 'Why It Helps')
    rows = '\n'.join(product_row(products_data[pid]) for pid in section['products'] if pid in products_data)
    return f'''  <h2 class="section-title">{section["title"]}</h2>
  <table class="product-table">
    <thead>
      <tr><th>Product</th><th>{col}</th><th>Research</th><th>Amazon</th></tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>'''


def tldr_items(items):
    return '\n'.join(f'      <li>{item}</li>' for item in items)


def build_page(slug, person, products_data):
    sections_html = '\n\n'.join(section_table(s, products_data) for s in person['sections'])
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
  <span class="logo">45° Health Protocols</span>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="{slug}-protocol.html">{person["display"]}</a></li>
    <li><a href="research/index.html">Research</a></li>
  </ul>
</nav>

<div class="page-header" style="background:{person["header_color"]};">
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
