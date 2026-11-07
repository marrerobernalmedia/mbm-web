#!/usr/bin/env python3
"""Pone al día las vistas ("v") de los videos de elhome/data.js o recta/data.js con un JSON de vidIQ.

Uso: python3 tools/actualizar_vistas.py [--app elhome|recta] <resultado_vidiq.json> [más archivos]
El JSON es la salida de vidiq_get_videos_by_ids ({videos:[{id, viewCount}]}) o una lista [{id, viewCount}].
Solo cambia el número de vistas (nunca lo baja) y deja el resto del archivo igual.
"""
import json, re, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
app = 'elhome'
if '--app' in args:
    i = args.index('--app'); app = args[i + 1]; del args[i:i + 2]
DJ = os.path.join(R, app, 'data.js')
vids = []
for a in args:
    d = json.load(open(a, encoding='utf-8'))
    vids += d.get('videos', d) if isinstance(d, dict) else d
src = open(DJ, encoding='utf-8').read()
cambios = []
for x in vids:
    vid, n = x.get('id'), x.get('viewCount')
    if not vid or not isinstance(n, int):
        continue
    pat = re.compile(r'("' + re.escape(vid) + r'": \{[^{}]*?"v": )(\d+)')
    m = pat.search(src)
    if not m:
        continue
    viejo = int(m.group(2))
    if n > viejo:
        src = src[:m.start(2)] + str(n) + src[m.end(2):]
        cambios.append((vid, viejo, n))
open(DJ, 'w', encoding='utf-8').write(src)
for c in cambios:
    print('%s %s -> %s' % c)
print('videos actualizados:', len(cambios))
