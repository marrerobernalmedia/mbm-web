#!/usr/bin/env python3
"""Añade al historial del tablero "Seguidores de la Red MBM" las cifras de root/seguidores.js.

Uso: python3 tools/seguidores_historial.py [--yt-fuente "YouTube Studio"] [--meta-fuente "Pepe (API de Meta)"]
- YouTube: una fila por canal con la fecha "actualizado" (reemplaza la de esa misma fecha).
- Facebook / Instagram: fila nueva solo si la cifra cambió respecto de la última guardada.
Escribe tools/seguidores_historial.json (lista de {fecha, red, cuenta, seguidores, fuente}, ordenada).
"""
import json, re, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SJ = os.path.join(R, 'root', 'seguidores.js')
HJ = os.path.join(R, 'tools', 'seguidores_historial.json')
args = sys.argv[1:]
def opt(n, d):
    return args[args.index(n) + 1] if n in args else d
ytf = opt('--yt-fuente', 'YouTube Studio')
mf = opt('--meta-fuente', 'Pepe (API de Meta)')
src = open(SJ, encoding='utf-8').read()
m = re.search(r'window\.SEGUIDORES\s*=\s*(\{.*?\n\});', src, re.S)
S = json.loads(m.group(1))
fecha = S['actualizado']
H = json.load(open(HJ, encoding='utf-8'))
def ultimo(red, cuenta):
    xs = [r for r in H if r['red'] == red and r['cuenta'] == cuenta]
    return max(xs, key=lambda r: r['fecha']) if xs else None
nuevas = 0
for k, v in S['yt'].items():
    H = [r for r in H if not (r['red'] == 'YouTube' and r['cuenta'] == k and r['fecha'] == fecha)]
    H.append({'fecha': fecha, 'red': 'YouTube', 'cuenta': k, 'seguidores': int(v), 'fuente': ytf}); nuevas += 1
for red, blk in (('Facebook', 'fb'), ('Instagram', 'ig')):
    for k, v in S[blk].items():
        u = ultimo(red, k)
        if u is None or (u['seguidores'] != int(v) and u['fecha'] <= fecha):
            H = [r for r in H if not (r['red'] == red and r['cuenta'] == k and r['fecha'] == fecha)]
            H.append({'fecha': fecha, 'red': red, 'cuenta': k, 'seguidores': int(v), 'fuente': mf}); nuevas += 1
H.sort(key=lambda r: (r['fecha'], r['red'], r['cuenta']))
json.dump(H, open(HJ, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(f'historial: {len(H)} filas ({nuevas} escritas para {fecha}) -> {HJ}')
