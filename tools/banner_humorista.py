#!/usr/bin/env python3
"""Pone la miniatura propia de un humorista en su ficha de El Home (app y web).
Uso: python3 tools/banner_humorista.py "<Nombre en data.js>" <slug> <imagen>
Recorta a 16:9, guarda elhome/banners/<slug>.jpg (800x450) y cambia "banner" en elhome/data.js.
Después: node tools/build_elhome_seo.js, subir la versión de sw.js y publicar."""
import sys, os
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nombre, slug, img = sys.argv[1:4]
im = Image.open(img).convert('RGB'); w, h = im.size
if w * 9 > h * 16: nw = h * 16 // 9; im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
elif w * 9 < h * 16: nh = w * 9 // 16; im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
im.resize((800, 450), Image.LANCZOS).save(os.path.join(R, 'elhome', 'banners', slug + '.jpg'), quality=88, optimize=True)
p = os.path.join(R, 'elhome', 'data.js'); s = open(p, encoding='utf-8').read()
import re
pat = re.compile(r'(\{"name": "' + re.escape(nombre) + r'", "banner": )(null|"[^"]*")')
assert len(pat.findall(s)) == 1, 'no encuentro la ficha de ' + nombre
open(p, 'w', encoding='utf-8').write(pat.sub(lambda m: m.group(1) + '"banners/' + slug + '.jpg"', s))
print('ok', nombre)
