#!/usr/bin/env python3
# Maqueta del rediseño de rectaalpecho.com (portada + artículo). Genera index.html y articulo.html.
import json, html

POSTS = [
 ("peloteros-cubanos-80","«Los de antes eran mejores»: el mito que confunde una liga vacía con una generación inferior","2026-09-11","mitos","La liga sí era mejor. Los peloteros no. Comparar generaciones sin mirar la liga en la que jugaban lleva a conclusiones equivocadas.","https://rectaalpecho.com/wp-content/uploads/2026/09/ChatGPT-Image-Sep-6-2026-08_06_32-PM.png"),
 ("irse-o-quedarse","La decisión que nadie firma","2026-09-08","fugas","Irse o quedarse: la decisión más dura del pelotero cubano, contada por los que la tomaron en un sentido y en el otro.","https://rectaalpecho.com/wp-content/uploads/2026/09/ChatGPT-Image-Sep-6-2026-08_00_08-PM.png"),
 ("braudilio-vinent","Braudilio Vinent rechazó los millones, se quedó en Cuba y esto es lo que recibió","2026-09-07","glorias","El Meteoro de La Maya le dijo que no a los scouts y le regaló cada victoria a la Revolución. Hoy, a los setenta, enseña sus medallas a la cámara.","https://rectaalpecho.com/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-06-at-7.47.01-PM.jpeg"),
 ("mito-del-aluminio","El mito del aluminio: la pelota «muerta» que metía 400 pies","2026-09-07","mitos","En 1999, con los mismos jugadores y el mismo picheo, pasaron a la madera: el líder dio 10 jonrones. Con aluminio daban más de 30.","https://rectaalpecho.com/wp-content/uploads/2026/09/ChatGPT-Image-Sep-6-2026-08_11_48-PM.png"),
 ("shohei-ohtani","Ohtani, Ruth y Bonds: los números que desmontan el mito del «mejor de la historia»","2026-09-06","mitos","WAR de por vida: Ruth 182.6, Bonds 162.8, Ohtani 55.7. Y Martín Dihigo ya fue de dos vías.","https://rectaalpecho.com/wp-content/uploads/2026/09/ChatGPT-Image-Sep-6-2026-07_50_47-PM.png"),
 ("lazaro-valle","Su presencia está en Cooperstown. En Cuba, su pensión le alcanza para un paquete de pollo y un inhalador","2026-09-04","glorias","Lanzó un juego perfecto tirando 100 millas y El Duque lo llama el mejor pitcher que vio en Cuba.","https://rectaalpecho.com/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-06-at-10.13.37-AM.jpeg"),
 ("antonio-scull","Un scout entró de noche al hotel con un portafolio: «Aquí tienes $50,000, y dos millones te esperan». Antonio Scull dijo que no","2026-09-01","dijeronno","El primera base de Industriales y del Equipo Cuba de Atlanta 96 cuenta, desde San Miguel del Padrón, las ofertas que rechazó.","https://rectaalpecho.com/wp-content/uploads/2026/09/Antonio-Scull.jpeg"),
 ("gabriel-pierre","Los Orioles le dijeron «vas a ser millonario». Cuba lo citó a una oficina de la Seguridad del Estado por estudiar la Biblia","2026-08-30","dijeronno","La tercera base de la Aplanadora Santiaguera, el físico de Grandes Ligas fabricado con picadillo de soya.","https://rectaalpecho.com/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-06-at-10.11.04-AM-scaled.jpeg"),
 ("lazaro-junco","Lázaro Junco se sentó con Recta al Pecho antes de morir. Esto fue lo que quiso dejar dicho","2026-08-28","glorias","El primer cubano en pasar los 400 jonrones abrió las puertas de su casa en Matanzas meses antes de morir.","https://rectaalpecho.com/wp-content/uploads/2026/09/Lazaro-Junco.jpeg"),
 ("osvaldo-fernandez","Se quitó el cinto del Equipo Cuba, se lo dio a un compañero y saltó un muro con cristales","2026-08-25","fugas","Cuatro meses escondido en Curazao, con miedo de que la Seguridad del Estado lo devolviera amarrado.","https://rectaalpecho.com/wp-content/uploads/2026/08/Osvaldo-Fernandez-scaled.jpeg"),
 ("german-mesa","«Juega para el público»: el mito de Germán Mesa, el mejor torpedero que Cuba nunca midió","2026-08-23","mitos","Paret lo supera en todas las columnas. Mesa es el más popular por geografía televisiva.","https://rectaalpecho.com/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-06-at-10.06.52-AM.jpeg"),
 ("jorge-soler","A Jorge Soler lo sacaron del terreno que tenía a una cuadra de su casa","2026-08-21","fugas","Fue Jugador Más Valioso de una Serie Mundial. Antes, Cuba lo suspendió sin fecha y lo botó del único terreno de su pueblo.","https://rectaalpecho.com/wp-content/uploads/2026/09/Jorge-Soler-scaled.jpeg"),
 ("yadel-marti","Tiró 0.00 en el primer Clásico Mundial. Hoy reparte paquetes en Miami","2026-08-18","borrados","Lo borraron del Cerro Pelado por permitir dos carreras contra Estados Unidos.","https://rectaalpecho.com/wp-content/uploads/2026/09/Yadel-Marti-scaled.jpeg"),
 ("juan-carlos-millan","Cuba le prometió un carro en 1992 y nunca se lo dio. En Estados Unidos ha tenido siete","2026-08-16","borrados","Llegó a 100 jonrones más rápido que casi nadie y nunca lo llevaron al equipo Cuba.","https://rectaalpecho.com/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-06-at-10.11.42-AM-scaled.jpeg"),
 ("eduardo-paret","Le quitaron cuatro años por una llamada de teléfono. Todavía no sabe quién dio la orden","2026-08-14","borrados","Según los números, el mejor campocorto que ha dado la Serie Nacional. Lo sacaron sin prueba y sin juicio.","https://rectaalpecho.com/wp-content/uploads/2026/09/Eduardo-Paret-scaled.jpeg"),
 ("mito-de-los-invencibles","El mito de los invencibles: aquella Cuba no dominaba a las Grandes Ligas —dominaba a los estudiantes","2026-08-12","mitos","Profesionales de tiempo completo presentados como amateurs contra universitarios de 19 a 21 años.","https://rectaalpecho.com/wp-content/uploads/2026/09/ChatGPT-Image-Sep-6-2026-08_19_12-PM.png"),
 ("livan-hernandez-2","Los asientos de bicicleta que cambiaron la historia del béisbol cubano","2026-08-11","fugas","Liván habló del anillo, de Bonds, del hermano y de la noche en que un equipo entero le viró la espalda.","https://rectaalpecho.com/wp-content/uploads/2026/08/Livan-scaled.jpeg"),
 ("linares-o-gurriel","¿Linares o Gurriel? El mito de la superestrella que nunca se probó — y el campeón que sí","2026-08-09","mitos","Linares bateó .368 con aluminio y .246 en Japón. Gurriel fue campeón de bateo en Grandes Ligas a los 37.","https://rectaalpecho.com/wp-content/uploads/2026/09/WhatsApp-Image-2026-09-06-at-10.09.20-AM-scaled.jpeg"),
 ("agustin-marquetti","El hombre que paralizó a Cuba con un batazo se iba del estadio en bicicleta","2026-08-07","borrados","«Si yo estuviera en Cuba, hace nueve años estuviera muerto.»","https://rectaalpecho.com/wp-content/uploads/2026/09/Marquetti-scaled.jpeg"),
 ("el-ultimo-out-de-rey-vicente-anglada","El último out de Rey Vicente Anglada","2026-07-10","borrados","Una Bohemia de febrero de 1982, con el cuño de la hemeroteca, y la sanción que nadie firmó.","https://rectaalpecho.com/wp-content/uploads/2026/07/Eliam-y-Rey-Vicente-Anglada.jpeg"),
]
SERIES = {
 "borrados":("Los Borrados","Los que Cuba sacó de las estadísticas y de la televisión."),
 "fugas":("Las Fugas","Cómo escaparon, contado en primera persona."),
 "dijeronno":("Los que dijeron no","Rechazaron los millones. Esto fue lo que recibieron."),
 "glorias":("Las glorias en el piso","Campeones del equipo Cuba que hoy viven olvidados."),
 "mitos":("Mitos y análisis","Lo que repite el fanático, contra los números."),
}
MITOS = [
 ("La pelota de los 80 tenía nivel de Grandes Ligas","Cuba mandaba profesionales disfrazados de amateurs contra universitarios. Contra profesionales de verdad, la cosa cambió.","eoXBslJ-ecw"),
 ("Es el mejor porque yo lo vi","Tus ojos vieron veinte juegos; el anotador los vio todos, y no le va a nadie.","qRSWVf9m864"),
 ("Linares fue el mejor de la historia","Bateó .368 con aluminio. En Japón, contra profesionales: .246.","HAw4DE2KYgk"),
 ("Si en Cuba nadie lo menciona, no fue grande","Tito Fuentes: 13 temporadas en Grandes Ligas, 1,491 hits y el Muro de la Fama de los Gigantes.","QZamWqu-N5E"),
 ("El mejor cubano es uno de Series Nacionales","En Cooperstown hay seis cubanos y ninguno jugó una Serie Nacional.","5I7xajTMsVk"),
 ("Antes se jugaba por amor a la camiseta","Lo que no cobraban como profesionales, lo cobraban por el centro de trabajo.","6vUrT7CeSAs"),
]
LAST = ("E_YTKkq8-Gw","Luis Giraldo Casanova","El régimen cubano le robó la Olimpiada y lo botó a los 33","jueves 29 de octubre")
NEXT = ("Rolando Viera","jueves 5 de noviembre")

def e(s): return html.escape(s, quote=True)
def fecha(iso):
    y,m,d = iso.split("-"); meses="ene feb mar abr may jun jul ago sep oct nov dic".split()
    return f"{int(d)} {meses[int(m)-1]} {y}"

CSS = """
:root{--paper:#f6f3ec;--card:#fffdf8;--ink:#141a3a;--navy:#0d174e;--red:#c52323;--mute:#5d6176;--line:#dcd7ca;--chip:#ebe6d9;--inv:#f6f3ec;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0f1226;--card:#171b35;--ink:#ecebe4;--navy:#dfe4ff;--red:#ff6b6b;--mute:#a3a7bd;--line:#2a2f50;--chip:#222747;--inv:#0f1226;color-scheme:dark}}
:root[data-theme="dark"]{--paper:#0f1226;--card:#171b35;--ink:#ecebe4;--navy:#dfe4ff;--red:#ff6b6b;--mute:#a3a7bd;--line:#2a2f50;--chip:#222747;--inv:#0f1226;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 "Source Serif 4",Georgia,serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.cond{font-family:"Barlow Condensed","Arial Narrow",sans-serif}
.ui{font-family:"Barlow",system-ui,sans-serif}
/* topbar */
.top{background:#0d174e;color:#f6f3ec}
.top .wrap{display:flex;align-items:center;gap:18px;min-height:64px}
.brand{display:flex;align-items:center;gap:12px}
.brand img{height:58px;width:auto;display:block}
.brand b{font-family:"Barlow Condensed",sans-serif;font-weight:800;font-size:26px;letter-spacing:.5px;text-transform:uppercase;line-height:1}
.brand small{display:block;font:600 11px/1.3 "Barlow",sans-serif;letter-spacing:2px;text-transform:uppercase;opacity:.85;max-width:120px}
nav.main{margin-left:auto;display:flex;gap:4px;flex-wrap:wrap}
nav.main a{font:600 15px/1 "Barlow",sans-serif;text-transform:uppercase;letter-spacing:1px;padding:10px 12px;border-radius:6px}
nav.main a:hover{background:rgba(255,255,255,.1)}
nav.main a.yt{background:var(--red);color:#fff}
.burger{display:none;margin-left:auto;background:none;border:1px solid rgba(255,255,255,.4);color:#fff;border-radius:6px;padding:8px 10px;font:600 14px "Barlow",sans-serif}
.ticker{background:var(--red);color:#fff;font:600 13px/1 "Barlow",sans-serif;letter-spacing:.5px}
.ticker .wrap{display:flex;gap:18px;align-items:center;height:36px;overflow:hidden;white-space:nowrap}
.ticker b{background:#fff;color:var(--red);padding:5px 8px;border-radius:3px;font-weight:800;letter-spacing:1.5px;font-size:11px}
.ticker span{opacity:.95}
/* hero */
.hero{display:grid;grid-template-columns:7fr 5fr;gap:28px;align-items:stretch;padding-block:28px}
.hero .big{position:relative;border-radius:14px;overflow:hidden;min-height:420px;background:#223;display:flex;align-items:flex-end;color:#fff}
.hero .big img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero .big .txt{position:relative;padding:28px;background:linear-gradient(180deg,rgba(13,23,78,0) 0%,rgba(13,23,78,.85) 55%,rgba(13,23,78,.95) 100%);width:100%}
.kicker{display:inline-block;font:800 12px/1 "Barlow",sans-serif;letter-spacing:2px;text-transform:uppercase;color:#fff;background:var(--red);padding:6px 9px;border-radius:3px}
.hero h1{font:800 40px/1.05 "Barlow Condensed",sans-serif;margin:12px 0 8px;text-wrap:balance}
.hero .big p{margin:0;font-size:16px;opacity:.95;max-width:60ch}
.side{display:grid;gap:14px;align-content:start}
.side h3{margin:0 0 2px;font:800 13px/1 "Barlow",sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--red)}
.mini{display:grid;grid-template-columns:96px 1fr;gap:12px;align-items:center;padding:10px;border:1px solid var(--line);border-radius:10px;background:var(--card)}
.mini img{width:96px;height:72px;object-fit:cover;border-radius:6px}
.mini b{font:700 17px/1.15 "Barlow Condensed",sans-serif;display:block}
.mini small{color:var(--mute);font:500 12px "Barlow",sans-serif;letter-spacing:.5px;text-transform:uppercase}
/* youtube strip */
.yt-strip{background:var(--navy);color:var(--inv);border-radius:14px;padding:22px;display:grid;grid-template-columns:1.3fr 1fr;gap:22px;margin-block:8px 36px}
.yt-strip .play{position:relative;border-radius:10px;overflow:hidden;aspect-ratio:16/9;background:#000;display:block}
.yt-strip .play img{width:100%;height:100%;object-fit:cover;display:block}
.yt-strip .play::after{content:"▶";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:64px;height:64px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font-size:24px;padding-left:4px}
.yt-strip h3{margin:0 0 6px;font:800 13px "Barlow",sans-serif;letter-spacing:2px;text-transform:uppercase;color:#ffb3b3}
.yt-strip h2{margin:0 0 6px;font:800 30px/1.05 "Barlow Condensed",sans-serif}
.yt-strip p{margin:0 0 14px;opacity:.9;font-size:15px}
.next{border-top:1px solid rgba(255,255,255,.2);padding-top:14px;margin-top:14px}
.next b{font:800 22px "Barlow Condensed",sans-serif}
.btn{display:inline-block;font:700 14px/1 "Barlow",sans-serif;letter-spacing:1px;text-transform:uppercase;padding:12px 16px;border-radius:7px;background:var(--red);color:#fff}
.btn.ghost{background:transparent;border:1px solid currentColor;color:inherit}
/* sections */
.sec{margin-block:36px}
.sec-h{display:flex;align-items:baseline;gap:14px;border-bottom:3px solid var(--navy);margin-bottom:16px;padding-bottom:6px}
.sec-h h2{margin:0;font:800 30px/1 "Barlow Condensed",sans-serif;text-transform:uppercase;letter-spacing:.5px}
.sec-h p{margin:0;color:var(--mute);font:500 14px "Barlow",sans-serif}
.sec-h a{margin-left:auto;font:700 13px "Barlow",sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--red);white-space:nowrap}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;min-width:0}
.card img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}
.card .b{padding:12px 14px 16px;display:grid;gap:6px}
.card .b small{font:600 11px "Barlow",sans-serif;letter-spacing:1.5px;text-transform:uppercase;color:var(--red)}
.card h3{margin:0;font:700 19px/1.15 "Barlow Condensed",sans-serif;text-wrap:balance}
.card p{margin:0;font-size:14px;color:var(--mute)}
.card time{font:500 12px "Barlow",sans-serif;color:var(--mute)}
/* mitos */
.mitos{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.mito{background:var(--card);border-left:5px solid var(--red);border-radius:8px;padding:14px 16px;display:grid;gap:6px}
.mito .q{font:800 20px/1.1 "Barlow Condensed",sans-serif}
.mito .q::before{content:"«";color:var(--red)} .mito .q::after{content:"»";color:var(--red)}
.mito p{margin:0;font-size:15px}
.mito a{font:700 12px "Barlow",sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--red)}
/* about band */
.band{background:var(--chip);border-radius:14px;padding:26px;display:grid;grid-template-columns:1.4fr 1fr;gap:26px;align-items:center;margin-block:36px}
.band h2{margin:0 0 8px;font:800 32px/1.05 "Barlow Condensed",sans-serif}
.band p{margin:0 0 12px}
.apps{display:flex;gap:10px;flex-wrap:wrap}
/* footer */
footer{background:#0d174e;color:#f6f3ec;margin-top:40px}
footer .wrap{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:26px;padding-block:34px 44px}
footer h4{margin:0 0 10px;font:800 13px "Barlow",sans-serif;letter-spacing:2px;text-transform:uppercase;color:#ffb3b3}
footer a,footer p{display:block;font:500 15px/1.9 "Barlow",sans-serif;margin:0;opacity:.9}
footer .sponsor{font:500 14px/1.5 "Barlow",sans-serif;opacity:.8;border-top:1px solid rgba(255,255,255,.15);padding-top:14px;margin-top:14px}
/* article */
.art-hero{display:grid;grid-template-columns:1fr;gap:0;justify-items:start;padding-block:30px 10px;max-width:860px;margin:0 auto}
.art-hero h1{font:800 46px/1.03 "Barlow Condensed",sans-serif;margin:12px 0 10px;text-wrap:balance}
.art-hero .dek{font-size:21px;line-height:1.4;color:var(--mute);margin:0 0 18px;font-style:italic}
.meta{display:flex;flex-wrap:wrap;gap:6px 18px;font:600 13px "Barlow",sans-serif;letter-spacing:.5px;text-transform:uppercase;color:var(--mute);align-items:center}
.meta .av{width:34px;height:34px;border-radius:50%;background:var(--navy);display:inline-grid;place-items:center;color:#fff;font:800 14px "Barlow Condensed",sans-serif;margin-right:8px}
.art-img{max-width:1000px;margin:18px auto 0}
.art-img img{width:100%;border-radius:14px;display:block;aspect-ratio:16/9;object-fit:cover}
.art-img figcaption{font:500 13px "Barlow",sans-serif;color:var(--mute);margin-top:8px}
.art{max-width:720px;margin:28px auto 0;font-size:18px;line-height:1.6}
.art p{margin:0 0 18px}
.art h2{font:800 30px/1.1 "Barlow Condensed",sans-serif;margin:34px 0 10px;text-transform:uppercase}
.art h2::after{content:"";display:block;width:48px;height:4px;background:var(--red);margin-top:8px}
.art blockquote{margin:22px 0;padding:6px 0 6px 22px;border-left:5px solid var(--red);font:700 26px/1.25 "Barlow Condensed",sans-serif}
.art blockquote p{margin:0}
.art a{color:var(--red);font-weight:700;border-bottom:2px solid transparent}
.art a:hover{border-color:var(--red)}
.art .lead{font-size:21px;line-height:1.5}
.callout{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:26px 0;display:grid;grid-template-columns:150px 1fr;gap:16px;align-items:center}
.callout img{width:150px;aspect-ratio:16/9;object-fit:cover;border-radius:8px}
.callout b{font:800 20px/1.15 "Barlow Condensed",sans-serif;display:block}
.callout small{font:600 12px "Barlow",sans-serif;letter-spacing:1.5px;text-transform:uppercase;color:var(--red)}
.credit{font:500 14px/1.5 "Barlow",sans-serif;color:var(--mute);border-top:1px solid var(--line);padding-top:14px;margin-top:30px}
.share{display:flex;gap:8px;flex-wrap:wrap;margin:22px 0}
.share a{font:700 13px "Barlow",sans-serif;letter-spacing:1px;text-transform:uppercase;border:1px solid var(--line);padding:9px 12px;border-radius:7px}
.related{max-width:1000px;margin:40px auto 0}
.note{background:#fff3cd;color:#5c4400;font:600 13px "Barlow",sans-serif;text-align:center;padding:8px}
@media (max-width:900px){
 .hero{grid-template-columns:1fr}.hero .big{min-height:340px}.hero h1{font-size:32px}
 .yt-strip,.band{grid-template-columns:1fr}
 .grid{grid-template-columns:repeat(2,minmax(0,1fr))}
 .mitos{grid-template-columns:1fr}
 footer .wrap{grid-template-columns:1fr 1fr}
 nav.main{display:none}.burger{display:block}
 .art-hero h1{font-size:34px}.art{font-size:17px}
 .callout{grid-template-columns:1fr}
}
@media (max-width:560px){.grid{grid-template-columns:1fr}footer .wrap{grid-template-columns:1fr}}
"""

HEAD = """<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>%s</style></head><body>
<div class="note ui">MAQUETA de rediseño — no es el sitio real. Las imágenes y textos son los publicados en rectaalpecho.com.</div>
<header class="top"><div class="wrap">
 <a class="brand" href="index.html"><img src="https://rectaalpecho.com/wp-content/uploads/2025/12/TEXTO-LOGO-TRANSPARENT.png" alt="Recta al Pecho"><span><small>Deportes · El béisbol es la pasión</small></span></a>
 <nav class="main"><a href="#borrados">Los Borrados</a><a href="#fugas">Las Fugas</a><a href="#dijeronno">Los que dijeron no</a><a href="#glorias">Glorias</a><a href="#mitos">Mitos</a><a href="#about">Quiénes somos</a><a class="yt" href="https://www.youtube.com/@RectaAlPecho">▶ Entrevistas</a></nav>
 <button class="burger">MENÚ</button>
</div></header>
<div class="ticker"><div class="wrap"><b>ESTE JUEVES</b><span>%s · nueva entrevista en YouTube</span><span>•</span><span>Último capítulo: %s</span></div></div>
"""

FOOT = """
<section class="band wrap" id="about">
 <div><h2>Recta al Pecho: deportes con la pelota como pasión</h2>
 <p>Un canal de deportes donde el béisbol es la pasión: entrevistas largas con peloteros de todas las épocas, dentro y fuera de Cuba, historias que el relato oficial borró y artículos que ponen los mitos del fanático frente a los números. Hablan los que lo vivieron.</p>
 <div class="apps"><a class="btn" href="https://www.youtube.com/@RectaAlPecho">Ver las entrevistas</a><a class="btn ghost" href="https://marrerobernalmedia.com/recta/">Instalar la app</a></div></div>
 <div><img src="https://rectaalpecho.com/wp-content/uploads/2026/07/Eliam-y-Rey-Vicente-Anglada.jpeg" alt="" style="width:100%;border-radius:10px;aspect-ratio:4/3;object-fit:cover"></div>
</section>
<footer><div class="wrap">
 <div><h4>Recta al Pecho</h4><p>Canal de deportes donde el béisbol es la pasión. Las historias, de los que las vivieron.</p><p>© 2026 Marrero Bernal Media LLC. Todos los derechos reservados.</p>
 <p class="sponsor">Patrocinado por <a href="https://www.marrerobernal.com" target="_blank" rel="noopener" style="display:inline;text-decoration:underline;opacity:1">Marrero Bernal &amp; Associates</a> — impuestos, seguros, inmigración, notaría y traducciones. <a href="https://www.marrerobernal.com" target="_blank" rel="noopener" style="display:inline;text-decoration:underline;opacity:1">www.marrerobernal.com</a></p></div>
 <div><h4>Series</h4><a href="#borrados">Los Borrados</a><a href="#fugas">Las Fugas</a><a href="#dijeronno">Los que dijeron no</a><a href="#glorias">Las glorias en el piso</a><a href="#mitos">Mitos y análisis</a></div>
 <div><h4>Síguenos</h4><a href="https://www.youtube.com/@RectaAlPecho">YouTube</a><a href="https://www.facebook.com/RectaAlPecho/">Facebook</a><a href="https://www.instagram.com/rectaalpecho/">Instagram</a><a href="https://marrerobernalmedia.com/recta/">App Recta al Pecho</a></div>
 <div><h4>El sitio</h4><a href="#">Quiénes somos</a><a href="#">Contacto</a><a href="#">Política de privacidad</a><a href="#">Términos y condiciones</a></div>
</div></footer>
</body></html>"""

bypost = {p[0]:p for p in POSTS}
def card(p):
    s,t,d,c,x,img = p
    return f'<a class="card" href="articulo.html"><img src="{img}" alt="" loading="lazy"><div class="b"><small>{e(SERIES[c][0])}</small><h3>{e(t)}</h3><p>{e(x)}</p><time>{fecha(d)}</time></div></a>'

def home():
    h = HEAD % ("Recta al Pecho — Deportes: el béisbol es la pasión", CSS, e(NEXT[0]), e(LAST[1]))
    lead = bypost["irse-o-quedarse"]; others = ["braudilio-vinent","peloteros-cubanos-80","antonio-scull"]
    h += '<main class="wrap">'
    h += f'''<section class="hero"><a class="big" href="articulo.html"><img src="{lead[5]}" alt=""><div class="txt"><span class="kicker">{e(SERIES[lead[3]][0])}</span><h1>{e(lead[1])}</h1><p>{e(lead[4])}</p></div></a>
<aside class="side"><h3>Lo último</h3>''' + "".join(f'<a class="mini" href="articulo.html"><img src="{bypost[o][5]}" alt=""><span><small>{e(SERIES[bypost[o][3]][0])}</small><b>{e(bypost[o][1])}</b></span></a>' for o in others) + '</aside></section>'
    h += f'''<section class="yt-strip"><a class="play" href="https://youtu.be/{LAST[0]}"><img src="https://i.ytimg.com/vi/{LAST[0]}/maxresdefault.jpg" alt=""></a>
<div><h3>Último capítulo en YouTube</h3><h2>{e(LAST[1])}: {e(LAST[2])}</h2><p>Estrenado el {LAST[3]}. Entrevista completa en el canal.</p><a class="btn" href="https://youtu.be/{LAST[0]}">Ver la entrevista</a>
<div class="next"><h3>Próximo estreno</h3><b>{e(NEXT[0])}</b> · {NEXT[1]}<br><span class="ui" style="font-size:14px;opacity:.85">Activa los avisos en la app y te llega al teléfono el día del estreno.</span></div></div></section>'''
    for key in ["borrados","fugas","dijeronno","glorias"]:
        ps = [p for p in POSTS if p[3]==key][:4]
        h += f'<section class="sec" id="{key}"><div class="sec-h"><h2>{e(SERIES[key][0])}</h2><p>{e(SERIES[key][1])}</p><a href="#">Ver todos →</a></div><div class="grid">' + "".join(card(p) for p in ps) + '</div></section>'
    h += '<section class="sec" id="mitos"><div class="sec-h"><h2>Mitos de la pelota cubana</h2><p>Lo que repite el fanático, contra los números.</p><a href="#">Todos los mitos →</a></div><div class="mitos">'
    h += "".join(f'<div class="mito"><div class="q">{e(q)}</div><p>{e(a)}</p><a href="https://youtu.be/{v}">Escúchalo de su boca →</a></div>' for q,a,v in MITOS) + '</div>'
    ps = [p for p in POSTS if p[3]=="mitos"][:4]
    h += '<div class="grid" style="margin-top:18px">' + "".join(card(p) for p in ps) + '</div></section></main>'
    h += FOOT
    open("index.html","w",encoding="utf-8").write(h)

def article():
    body = open("/tmp/claude-0/-home-claude/ee77ae5d-17df-5541-bc0e-84adf0de4135/scratchpad/irse-o-quedarse.html",encoding="utf-8").read()
    body = body.replace('<article class="recta-article">','').replace('</article>','')
    body = body.replace('<p class="recta-video-title">','<p class="ui" style="font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:13px;color:var(--red);margin:30px 0 8px">').replace('<div class="recta-video">','<div style="border-radius:12px;overflow:hidden;aspect-ratio:16/9">').replace('<p class="recta-credit">','<p class="credit">')
    body = body.replace('<p>En Cuba, la decisión más grande','<p class="lead">En Cuba, la decisión más grande',1)
    # callout después de la sección "Lo que costaba irse"
    callout = f'<div class="callout"><img src="https://i.ytimg.com/vi/LhgEUVHLH2g/hqdefault.jpg" alt=""><div><small>Escúchalo de su boca</small><b>Yordanys Pérez: se fue en lancha por el mánager, 8 turnos en Triple A y a la calle</b><a href="https://youtu.be/LhgEUVHLH2g">Ver la entrevista →</a></div></div>'
    body = body.replace('<h2>Lo que costaba quedarse</h2>', callout + '<h2>Lo que costaba quedarse</h2>')
    p = bypost["irse-o-quedarse"]
    h = HEAD % ("La decisión que nadie firma — Recta al Pecho", CSS, e(NEXT[0]), e(LAST[1]))
    h += f'''<main class="wrap"><header class="art-hero"><span class="kicker">{e(SERIES[p[3]][0])}</span><h1>{e(p[1])}</h1><p class="dek">{e(p[4])}</p>
<div class="meta"><span><span class="av">EM</span>Eliam Marrero Bernal</span><span>{fecha(p[2])}</span><span>Lectura: 6 min</span></div></header>
<figure class="art-img"><img src="{p[5]}" alt=""><figcaption>La maleta, la gorra y la bandera: la decisión que no cabe en un contrato.</figcaption></figure>
<article class="art">{body}
<div class="share"><a href="#">Compartir en Facebook</a><a href="#">WhatsApp</a><a href="#">X</a><a href="#">Copiar enlace</a></div></article>
<section class="related"><div class="sec-h"><h2>Sigue leyendo</h2><p>Las historias que se citan en este artículo.</p></div><div class="grid">''' + "".join(card(bypost[s]) for s in ["antonio-scull","gabriel-pierre","braudilio-vinent","agustin-marquetti"]) + '</div></section></main>'
    h += FOOT
    open("articulo.html","w",encoding="utf-8").write(h)

home(); article()
print("ok")
