#!/usr/bin/env python3
"""Pone al día los títulos ("t") de elhome/data.js y recta/data.js con el título vigente en YouTube.

Las miniaturas se actualizan solas (la app las pide a i.ytimg.com), pero los títulos están
copiados en data.js. Este script los refresca sin gastar créditos de vidIQ: usa el oEmbed
público de YouTube (https://www.youtube.com/oembed), que da el título actual de cada video.

Uso:
  python3 tools/actualizar_titulos.py [--app elhome|recta|todas] [--aplicar]
Sin --aplicar solo enseña los cambios. Con --aplicar cambia SOLO el campo "t" de cada entrada
(el resto del archivo queda igual) y guarda en tools/titulos_youtube.json el título crudo de
YouTube de cada video. Después, si cambió elhome/data.js: node tools/build_elhome_seo.js

Reglas:
- La app muestra el humorista aparte, así que el título se limpia: se quitan "LRECS #NN" y lo que
  va detrás ("| HUMORISTA"), las colas "| El Home de la Risa", " 🎭 HUMORISTA" y el prefijo
  "HUMORISTA 🎭 " / "HUMORISTA - " / "HUMORISTA: ".
- Si el título de YouTube no cambió desde la última corrida (titulos_youtube.json), no se toca
  la app: así se respetan los títulos retocados a mano.
- Primera vez de un video (sin registro): solo se cambia si el título de la app NO es un recorte
  del de YouTube (mayúsculas, tildes, signos y nombres no cuentan). En Recta, la primera vez solo
  se registra el título; a partir de ahí, cualquier cambio en YouTube pasa a la app.
- Los videos que aún no salieron (privados/programados) no dan título y se saltan.
"""
import json, os, re, subprocess, sys, unicodedata, urllib.request, concurrent.futures as cf

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(R, 'tools', 'titulos_youtube.json')
EMO = r'[\U0001F000-\U0001FAFF☀-➿️‍⭐⭕]'


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return ' '.join(re.findall(r'[a-z0-9ñ]+', s))


SHOWS = ['la risa es cosa seria', 'el home de la risa', 'welcome to apagonia', 'recta al pecho',
         'la cosa es de risa', 'apagonia hoy', 'mlb en espanol', 'lrecs', 'marrero bernal media']
NOMBRES = set()


def cargar_nombres(vids, comics):
    for x in list(vids.values()):
        for n in (x.get('c') or []) + ([x['p']] if x.get('p') else []):
            NOMBRES.add(norm(n))
    for c in comics or []:
        NOMBRES.add(norm(c.get('name', '')))
    for n in ['rigo ferrera', 'rigoberto ferrera', 'la llave', 'miguel moreno', 'kamilo kabello', 'wattage',
              'manrufo', 'orlando manrufo', 'habanero', 'rigo', 'pepe rillo', 'baudilio', 'el bera', 'doimeadios', 'el rubio', 'mayito', 'genaro']:
        NOMBRES.add(n)
    NOMBRES.discard('')


def es_etiqueta(seg):
    """True si el trozo es solo nombres de humoristas o de shows (\"MENTEPOLLO, RIGO y LA LLAVE\")."""
    if not norm(seg):
        return True
    trozos = [norm(t) for t in re.split(r'\s+y\s+|\s+Y\s+|,|&', seg) if norm(t)]
    return all(t in NOMBRES or t in SHOWS or re.fullmatch(r'lrecs \d+', t) for t in trozos)


SEP = r'(?:\s*\|\s*|\s*' + EMO + r'+\s*|\.\s+|\s+[-–—]\s+|:\s+)'


def limpiar(t, c=None):
    t = re.sub(r'\s+', ' ', t.replace('&vert;', '|')).strip()
    # "… LRECS #82 | DANI QUINTERO", "… | LRECS #66", "… 💡LRECS #88"
    t = re.sub(r'[\s.|·,]*' + EMO + r'*\s*LRECS\s*#\s*\d+.*$', '', t)
    for _ in range(4):
        # cola: "| El Home de la Risa", " 🎭 MAYITO", ". Bacallao", "😂 MENTEPOLLO, RIGO y BACALLAO"
        m = re.search(SEP + r'([^|\U0001F000-\U0001FAFF]{1,60})$', t)
        if m and es_etiqueta(m.group(1)):
            t = t[:m.start()].rstrip()
            continue
        # prefijo: "VOLTÍMETRO 💡 ", "CABO PANTERA - ", "VISTI CÁRDENAS | ", "EL RUBIO: "
        m = re.match(r'^([^|:\U0001F000-\U0001FAFF]{1,40}?)' + SEP, t)
        if m and es_etiqueta(m.group(1)):
            t = t[m.end():]
            continue
        # prefijo sin separador en MAYÚSCULAS: "DANI QUINTERO Ni se te ocurra…"
        hecho = False
        for n in sorted(NOMBRES, key=len, reverse=True):
            k = len(n.split())
            pal = t.split(' ')
            if len(pal) > k + 2 and norm(' '.join(pal[:k])) == n and ' '.join(pal[:k]).upper() == ' '.join(pal[:k]):
                t = ' '.join(pal[k:]); hecho = True; break
        if not hecho:
            break
    t = re.sub(r'(\s*' + EMO + r')+$', '', t)
    t = re.sub(r'^(' + EMO + r'\s*)+', '', t)
    t = re.sub(r'[\s|,·\-–—]+$', '', t).strip().rstrip('.').strip()
    t = t.replace('“', '"').replace('”', '"')
    if t.count('"') % 2:
        t = t.replace('"', '')
    t = re.sub(r'\s*🎭\s*', ': ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:1].upper() + t[1:] if t else t


def sin_nombres(s):
    n = ' ' + norm(s) + ' '
    for x in sorted(NOMBRES, key=len, reverse=True):
        n = n.replace(' ' + x + ' ', ' ')
    return ' '.join(n.split())


def solo_recorte(viejo, nuevo):
    """El título de la app es un recorte del de YouTube (o al revés): no hace falta cambiarlo."""
    a, b = sin_nombres(viejo), sin_nombres(nuevo)
    if not a or not b:
        return False
    if a in b or b in a:
        return True
    pa, pb = a.split(), set(b.split())
    return sum(w in pb for w in pa) / len(pa) >= 0.85


def oembed(i):
    u = 'https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=' + i
    try:
        with urllib.request.urlopen(u, timeout=20) as r:
            return i, json.load(r).get('title')
    except Exception:
        return i, None


def leer(app):
    js = 'const w={};new Function("window",require("fs").readFileSync(%r,"utf8"))(w);' \
         'console.log(JSON.stringify(w.APPDATA))' % os.path.join(R, app, 'data.js')
    return json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, check=True).stdout)


def main():
    a = sys.argv[1:]
    aplicar = '--aplicar' in a
    app = a[a.index('--app') + 1] if '--app' in a else 'todas'
    apps = ['elhome', 'recta'] if app == 'todas' else [app]
    snap = json.load(open(SNAP, encoding='utf-8')) if os.path.exists(SNAP) else {}
    total = 0
    datos = {ap: leer(ap) for ap in apps}
    for d in datos.values():
        cargar_nombres(d['vid'], d.get('comics'))
    for ap in apps:
        vid = datos[ap]['vid']
        ids = [i for i in vid if re.fullmatch(r'[A-Za-z0-9_-]{11}', i)]
        with cf.ThreadPoolExecutor(8) as ex:
            yt = dict(ex.map(oembed, ids))
        p = os.path.join(R, ap, 'data.js')
        src = open(p, encoding='utf-8').read()
        cambios, sin = [], 0
        for i in ids:
            raw = yt.get(i)
            if not raw:
                sin += 1
                continue
            viejo = vid[i].get('t', '')
            nuevo = limpiar(raw)
            antes = snap.get(i)
            snap[i] = raw
            if antes == raw or not nuevo or nuevo == viejo:
                continue
            # Primera vez: Recta tiene títulos de redacción propia; solo se registra el de YouTube.
            if antes is None and (ap == 'recta' or raw == viejo or solo_recorte(viejo, nuevo)):
                continue
            pat = re.compile(r'("' + re.escape(i) + r'": ?\{[^{}]*?"t": ?)("(?:[^"\\]|\\.)*")')
            m = pat.search(src)
            if not m:
                continue
            src = src[:m.start(2)] + json.dumps(nuevo, ensure_ascii=False) + src[m.end(2):]
            cambios.append((i, viejo, nuevo))
        for i, v, n in cambios:
            print('%s %s\n   antes: %s\n   ahora: %s' % (ap, i, v, n))
        print('%s: %d títulos cambiados, %d sin título público (no salieron aún)' % (ap, len(cambios), sin))
        total += len(cambios)
        if aplicar:
            open(p, 'w', encoding='utf-8').write(src)
    if aplicar:
        json.dump(snap, open(SNAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    print('total:', total, '(aplicado)' if aplicar else '(prueba; usa --aplicar)')


if __name__ == '__main__':
    main()
