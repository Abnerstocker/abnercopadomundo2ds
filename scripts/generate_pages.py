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
  <div class="container">
    <header class="year-header">
      <h1>Copa do Mundo — {year}</h1>
      <div class="meta">Sede: {host} • Placar da final: {final_score}</div>
    </header>
    <main>
      <section class="result">
        <p class="winner"><span class="flag">{flag_champion}</span> <strong>Campeão:</strong> {champion}</p>
        <p class="runner"><span class="flag">{flag_runner}</span> <strong>Vice:</strong> {runner_up}</p>
      </section>

      <section class="notes">
        <h2>Curiosidades</h2>
        <p>{note}</p>
      </section>

      <p><a href="{rel}/index.html">← Voltar</a></p>
    </main>
    <footer class="site-footer">Fonte: compilado manualmente</footer>
  </div>
</body>
</html>
'''

# Map country names (as in JSON) to emoji flag. Add entries as needed.
FLAG_MAP = {
    'Uruguai': '🇺🇾',
    'Argentina': '🇦🇷',
    'Itália': '🇮🇹',
    'Tchecoslováquia': '🇨🇿',
    'Hungria': '🇭🇺',
    'Brasil': '🇧🇷',
    'Alemanha Ocidental': '🇩🇪',
    'Suécia': '🇸🇪',
    'Inglaterra': '🏴',
    'Países Baixos': '🇳🇱',
    'França': '🇫🇷',
    'Alemanha': '🇩🇪',
    'Espanha': '🇪🇸',
    'Croácia': '🇭🇷',
}

def main():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    for item in data:
        year = item['year']
        champion = item.get('champion', '')
        runner = item.get('runner_up', '')
        # page path at root
        out = ROOT / f"{year}.html"
        rel = '.'
        flag_champion = FLAG_MAP.get(champion, '')
        flag_runner = FLAG_MAP.get(runner, '')
        final_score = item.get('final_score', '')
        host = item.get('host', '')
        note = item.get('note', '')
        html = TEMPLATE.format(year=year, champion=champion, runner_up=runner, rel=rel, flag_champion=flag_champion, flag_runner=flag_runner, final_score=final_score, host=host, note=note)
        out.write_text(html, encoding='utf-8')
        print('Wrote', out)

if __name__ == '__main__':
    main()
