#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'worldcups.json'

TEMPLATE = '''<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Copa do Mundo — {year}</title>
  <link rel="stylesheet" href="{rel}/styles.css">
</head>
<body>
  <header>
    <h1>Copa do Mundo — {year}</h1>
  </header>
  <main>
    <p><strong>Campeão:</strong> {champion}</p>
    <p><strong>Vice:</strong> {runner_up}</p>
    <p><a href="{rel}/index.html">Voltar</a></p>
  </main>
  <footer>Fonte: compilado manualmente</footer>
</body>
</html>
'''

def main():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    for item in data:
        year = item['year']
        champion = item.get('champion', '')
        runner = item.get('runner_up', '')
        # page path at root
        out = ROOT / f"{year}.html"
        rel = '.'
        html = TEMPLATE.format(year=year, champion=champion, runner_up=runner, rel=rel)
        out.write_text(html, encoding='utf-8')
        print('Wrote', out)

if __name__ == '__main__':
    main()
