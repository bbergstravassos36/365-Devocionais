"""Confere a distribuição estática sem dependências externas."""
import json
import re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
dist = root / 'dist'
for name in ['index.html', 'app.js', 'style.css', 'devocionais.json', 'fontes.json', 'icon.svg', 'landscape.svg', 'manifest.webmanifest']:
    assert (dist / name).is_file(), f'Arquivo ausente: {name}'
readings = json.loads((dist / 'devocionais.json').read_text(encoding='utf-8'))
assert len(readings) == 365
for day, item in enumerate(readings, 1):
    assert item['id'] == day
    assert item['title'] and item['ref']
    assert len(item['sections']) == 10
    assert all(s['title'] and s['paragraphs'] for s in item['sections'])
manifest = json.loads((dist / 'manifest.webmanifest').read_text(encoding='utf-8'))
assert manifest['start_url'] == './', 'O início deve respeitar a subpasta'
for icon in manifest['icons']:
    assert (dist / icon['src']).is_file()
html = (dist / 'index.html').read_text(encoding='utf-8')
for asset in re.findall(r'(?:src|href)="([^"]+)"', html):
    if asset.startswith(('http:', 'https:', '#')):
        continue
    assert not asset.startswith('/'), f'Caminho incompatível com subpastas: {asset}'
    assert (dist / asset).is_file(), f'Recurso ausente: {asset}'
script = (dist / 'app.js').read_text(encoding='utf-8')
assert '/bible/1608/' in script and '.ARA' in script
assert '/bible/129/' not in script and 'NVI' not in script
assert not (root / '.openai').exists()
print('OK: arquivos completos, 365 leituras, 3.650 seções, links ARA e caminhos relativos.')
