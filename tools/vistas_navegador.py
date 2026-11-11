#!/usr/bin/env python3
"""Vistas de TODOS los videos de las apps, leídas gratis en YouTube desde el navegador (sin vidIQ).

Paso 1 — sacar el código para el navegador (una pestaña en https://www.youtube.com/...):
    python3 tools/vistas_navegador.py js elhome     (o recta)
  Imprime un JavaScript que lee "viewCount" de la página pública de cada video y devuelve
  "N|id:vistas,id:vistas,…". Se ejecuta con la herramienta javascript del navegador interno.

Paso 2 — aplicar el resultado:
    python3 tools/vistas_navegador.py aplicar elhome /ruta/resultado.txt
  (el archivo lleva el texto devuelto, con o sin comillas). Usa tools/actualizar_vistas.py:
  solo cambia los números "v" y nunca los baja.
"""
import json, os, re, subprocess, sys, tempfile
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ids(app):
    src = open(os.path.join(R, app, 'data.js'), encoding='utf-8').read()
    d = json.loads(src[src.index('window.APPDATA = ') + 17:].rstrip().rstrip(';'))
    return [i for i, v in d['vid'].items() if re.fullmatch(r'[\w-]{11}', i) and not v.get('url')]

def js(app):
    return ('const ids=%s; const out=[]; let i=0; const one=async()=>{ while(i<ids.length){ const id=ids[i++]; '
            'try{ const t=await fetch("https://www.youtube.com/watch?v="+id,{credentials:"omit"}).then(r=>r.text()); '
            'const m=t.match(/"viewCount":"(\\d+)"/); if(m) out.push(id+":"+m[1]); }catch(e){} } }; '
            'await Promise.all([one(),one(),one(),one(),one(),one()]); out.length+"|"+out.join(",")') % json.dumps(ids(app))

def aplicar(app, archivo):
    t = open(archivo, encoding='utf-8').read()
    pares = re.findall(r'([\w-]{11}):(\d+)', t)
    total = len(ids(app))
    print('leídos %d de %d' % (len(pares), total))
    if len(pares) < total * 0.6:
        sys.exit('Muy pocos videos leídos: no se aplica nada.')
    f = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8')
    json.dump([{'id': i, 'viewCount': int(n)} for i, n in pares], f); f.close()
    subprocess.run([sys.executable, os.path.join(R, 'tools', 'actualizar_vistas.py'), '--app', app, f.name], check=True)

if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'js': print(js(sys.argv[2]))
    elif len(sys.argv) >= 4 and sys.argv[1] == 'aplicar': aplicar(sys.argv[2], sys.argv[3])
    else: sys.exit(__doc__)
