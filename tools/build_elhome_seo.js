#!/usr/bin/env node
// Genera páginas estáticas indexables de www.elhomedelarisa.com a partir de elhome/data.js:
//   /humorista/<slug>/   una por humorista (todas sus presentaciones)
//   /show/<slug>/        una por show
//   /humoristas/ y /shows/  índices
// y reescribe elhome/sitemap.xml. Correr desde la raíz del repo después de cada cambio de data.js:
//   node tools/build_elhome_seo.js
const fs = require("fs"), path = require("path");
const root = path.resolve(__dirname, ".."), out = path.join(root, "elhome");
global.window = {}; require(path.join(out, "data.js")); require(path.join(out, "ajustes.js"));
window.AJUSTAR(window.APPDATA);
const D = window.APPDATA, V = D.vid, SITE = "https://www.elhomedelarisa.com";
const today = new Date().toISOString().slice(0, 10);

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const slug = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const live = id => V[id] && V[id].k !== "proximo" && V[id].k !== "futuro";
const soon = id => V[id] && (V[id].k === "proximo" || V[id].k === "futuro");
const fEst = f => f ? new Date(f + "T12:00:00").toLocaleDateString("es", { weekday: "long", day: "numeric", month: "long" }) : "muy pronto";
const pcard = id => { const v = V[id]; return `<a class="v" href="${wurl(id)}" target="_blank" rel="noopener"><img src="${thumb(id)}" alt="${esc(v.t)}" loading="lazy"><h3>${esc(window.TITULO_LIMPIO(D, id))}</h3><small style="color:var(--bulb)">Estreno ${esc(fEst(v.f))}${v.n ? " · " + esc(v.n) : ""} · ver el tráiler</small></a>`; };
const upSec = ids => { const l = ids.filter(soon).sort((a, b) => (V[a].f || "9").localeCompare(V[b].f || "9")); return l.length ? `<h2>Próximo estreno</h2><div class="grid">${l.map(pcard).join("")}</div>` : ""; };
const thumb = id => V[id] && V[id].img ? abs(V[id].img) : `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
const wurl = id => (V[id] && V[id].url) || `https://www.youtube.com/watch?v=${id}`;
const abs = u => !u ? "" : /^https?:/.test(u) ? u : `${SITE}/${u.replace(/^\//, "")}`;
const fmt = n => n >= 1e6 ? (n / 1e6).toFixed(1).replace(".0", "") + "M" : n >= 1e3 ? Math.round(n / 1e3) + "K" : String(n || 0);
const showOf = {}; D.shows.forEach(s => (s.v || []).forEach(i => { if (!showOf[i]) showOf[i] = s; }));
const sname = s => s.short || s.name;

const CSS = `:root{--bg:#0c0a0d;--card:#17141a;--line:#2a2530;--fg:#f4efe6;--mute:#a59fae;--lime:#9be22d;--bulb:#f7d774;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 "Inter",system-ui,sans-serif}
a{color:inherit;text-decoration:none}.wrap{max-width:1100px;margin:0 auto;padding-inline:max(16px,env(safe-area-inset-left,0px)) max(16px,env(safe-area-inset-right,0px))}
header{border-bottom:1px solid var(--line);padding-block:14px}header .wrap{display:flex;align-items:center;gap:12px}header img{width:44px;height:44px}
header b{font:400 22px "Bowlby One",Impact,sans-serif;letter-spacing:.01em}header span{display:block;color:var(--mute);font-size:12px}
header .go{margin-left:auto;background:var(--lime);color:#111;font-weight:800;font-size:14px;padding:10px 16px;border-radius:999px;white-space:nowrap}
.hero{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:24px;align-items:center;margin:28px 0}
.hero img{width:100%;border-radius:16px;aspect-ratio:16/9;object-fit:cover;background:var(--card)}
h1{font:400 clamp(30px,5vw,46px)/1.05 "Bowlby One",Impact,sans-serif;margin:0 0 10px;text-wrap:balance}
.lead{color:var(--mute);margin:0 0 16px;max-width:62ch}.btns{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:11px 18px;border-radius:999px;font-weight:700;font-size:15px}.b1{background:#e2262f;color:#fff}.b2{border:1px solid var(--line)}
h2{font:400 24px "Bowlby One",Impact,sans-serif;margin:34px 0 14px}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.v img{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:12px;background:var(--card)}.v h3{font-size:15px;margin:8px 0 4px;line-height:1.3}.v small{color:var(--mute);font-size:12.5px}
.chips{display:flex;flex-wrap:wrap;gap:8px}.chip{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:8px 14px;font-weight:600;font-size:14px}
.cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}.card img{width:100%;aspect-ratio:16/9;object-fit:cover}.card div{padding:12px 14px}.card b{display:block}.card small{color:var(--mute)}
footer{margin-top:50px;border-top:1px solid var(--line);padding-block:24px;color:var(--mute);font-size:14px}footer a{color:var(--fg);margin-right:14px}
@media(max-width:900px){.grid,.cards{grid-template-columns:repeat(2,minmax(0,1fr))}.hero{grid-template-columns:1fr}}`;

function page({ url, title, desc, image, h1, body, ld }) {
  return `<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>${esc(title)}</title><meta name="description" content="${esc(desc)}"><link rel="canonical" href="${url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="El Home de la Risa"><meta property="og:locale" content="es_US"><meta property="og:url" content="${url}"><meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(desc)}"><meta property="og:image" content="${esc(image)}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/icons/icon-192.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bowlby+One&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>${CSS}</style>
<script type="application/ld+json">${JSON.stringify(ld)}</script></head><body>
<header><div class="wrap"><a href="/"><img src="/brand/elhome-ico.png" alt="El Home de la Risa"></a><a href="/"><b>El Home de la Risa</b><span>La casa del humor cubano</span></a><a class="go" href="/">Abrir El Home</a></div></header>
<main class="wrap">${body}</main>
<footer><div class="wrap"><a href="/">Inicio</a><a href="/shows/">Shows</a><a href="/humoristas/">Humoristas</a><a href="https://marrerobernalmedia.com/apk/elhome.apk">Descargar la app (Android)</a><p>© ${today.slice(0, 4)} Marrero Bernal Media LLC. Todos los derechos reservados.</p></div></footer>
</body></html>`;
}
const vcard = id => { const v = V[id], s = showOf[id]; return `<a class="v" href="${wurl(id)}" target="_blank" rel="noopener"><img src="${thumb(id)}" alt="${esc(v.t)}" loading="lazy"><h3>${esc(window.TITULO_LIMPIO(D, id))}</h3><small>${esc(s ? sname(s) : "")}${v.n ? " " + esc(v.n) : ""}${v.v ? " · " + fmt(v.v) + " vistas" : ""}</small></a>`; };
// Fechas para el dato estructurado de Google: elhome/fechas.json (publishedAt real de YouTube) o, si no, la fecha de estreno "f" a las 8:00 AM de Las Vegas.
const PUB = (() => { try { return JSON.parse(fs.readFileSync(path.join(out, "fechas.json"), "utf8")); } catch (e) { return {}; } })();
const lvOff = f => { const n = new Intl.DateTimeFormat("en-US", { timeZone: "America/Los_Angeles", timeZoneName: "shortOffset" }).formatToParts(new Date(f + "T16:00:00Z")).find(x => x.type === "timeZoneName").value.replace("GMT", ""); const m = n.match(/^([+-])(\d+)(?::(\d+))?$/); return m ? `${m[1]}${m[2].padStart(2, "0")}:${(m[3] || "00").padStart(2, "0")}` : "-08:00"; };
const upDate = id => PUB[id] || (/^\d{4}-\d{2}-\d{2}$/.test(V[id].f || "") ? `${V[id].f}T08:00:00${lvOff(V[id].f)}` : null);
const vDesc = id => { const v = V[id], s = showOf[id], c = (v.c || []).join(", "); return `${v.t}${c ? " — " + c : ""}${s ? ". " + sname(s) : ""}${v.n ? " " + v.n : ""}. Humor cubano en El Home de la Risa.`; };
const videoLD = ids => ids.filter(id => upDate(id) && !V[id].url).slice(0, 30).map((id, i) => ({ "@type": "ListItem", position: i + 1, item: { "@type": "VideoObject", name: V[id].t, description: vDesc(id), thumbnailUrl: thumb(id), uploadDate: upDate(id), embedUrl: `https://www.youtube.com/embed/${id}`, url: `https://www.youtube.com/watch?v=${id}` } }));
const write = (rel, html) => { const p = path.join(out, rel, "index.html"); fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, html); };

const FEM = new Set(["Yamira Díaz"]);
// Otros nombres artísticos (sus páginas viejas son noindex y mandan aquí): van en el título, la descripción y el dato estructurado de la ficha principal
const AKA = { "Manrufo": ["Mariconchi", "Genaro Pomposo"], "Dani Quintero": ["Kamilo Kabello"], "Newito": ["Wattage"] };
const akaTxt = n => AKA[n] ? ` (${AKA[n].join(", ")})` : "";
const urls = [{ loc: `${SITE}/`, pr: "1.0", cf: "daily" }];
// limpia generaciones anteriores
for (const d of ["humorista", "show"]) fs.rmSync(path.join(out, d), { recursive: true, force: true });

// Humoristas
const comics = D.comics.map(c => ({ ...c, up: (c.all || []).filter(soon), ids: (c.all || []).filter(live).sort((a, b) => (V[b].v || 0) - (V[a].v || 0)) })).filter(c => c.ids.length || c.up.length);
for (const c of comics) {
  const s = slug(c.name), url = `${SITE}/humorista/${s}/`, shows = [...new Set(c.ids.map(id => showOf[id]).filter(Boolean).map(sname))];
  const total = c.ids.reduce((a, id) => a + (V[id].v || 0), 0);
  const first = c.ids[0] || c.up[0];
  const desc = !c.ids.length ? `${c.name}, humorista cubana en La Risa es Cosa Seria: estreno el ${fEst(V[c.up[0]].f)}. Mira el tráiler y activa la campanita en El Home de la Risa, la casa del humor cubano.` : `${c.name}${akaTxt(c.name)}, humorista cubano: todas sus presentaciones en ${shows.slice(0, 3).join(", ") || "El Home de la Risa"}. ${c.ids.length} videos${total ? " con " + fmt(total) + " vistas" : ""}, juntos en El Home de la Risa, la casa del humor cubano.`;
  const image = abs(c.banner) || thumb(first);
  write(`humorista/${s}`, page({ url, title: `${c.name}${akaTxt(c.name)} — ${FEM.has(c.name) ? "humorista cubana" : "humorista cubano"}: todos sus videos | El Home de la Risa`, desc, image,
    body: `<section class="hero"><img src="${esc(image)}" alt="${esc(c.name)}"><div><h1>${esc(c.name)}</h1><p class="lead">${esc(desc)}</p><div class="btns"><a class="btn b1" href="${wurl(first)}" target="_blank" rel="noopener">${c.ids.length ? "▶ Ver su video más visto" : "▶ Ver el tráiler"}</a><a class="btn b2" href="/?humorista=${encodeURIComponent(c.name)}">Abrir en El Home</a></div></div></section>
${upSec(c.up)}${c.ids.length ? `<h2>Todas sus presentaciones</h2><div class="grid">${c.ids.map(vcard).join("")}</div>` : ""}
<h2>Más humoristas</h2><div class="chips">${comics.filter(o => o !== c).slice(0, 24).map(o => `<a class="chip" href="/humorista/${slug(o.name)}/">${esc(o.name)}</a>`).join("")}</div>`,
    ld: { "@context": "https://schema.org", "@graph": [
      { "@type": "Person", "@id": url + "#persona", name: c.name, ...(AKA[c.name] ? { alternateName: AKA[c.name] } : {}), jobTitle: "Humorista", nationality: "Cuba", url, image },
      { "@type": "ItemList", name: `Videos de ${c.name}`, itemListElement: videoLD(c.ids.length ? c.ids : c.up) },
      { "@type": "BreadcrumbList", itemListElement: [{ "@type": "ListItem", position: 1, name: "El Home de la Risa", item: SITE + "/" }, { "@type": "ListItem", position: 2, name: "Humoristas", item: SITE + "/humoristas/" }, { "@type": "ListItem", position: 3, name: c.name, item: url }] }] } }));
  urls.push({ loc: url, pr: "0.8", cf: "weekly" });
}
// Nombres artísticos unidos a otra ficha: su página vieja manda a la ficha principal
for (const [from, to] of [["Kamilo Kabello", "Dani Quintero"], ["Wattage", "Newito"], ["Mariconchi", "Manrufo"], ["Genaro Pomposo", "Manrufo"]]) {
  const u = `${SITE}/humorista/${slug(to)}/`;
  write(`humorista/${slug(from)}`, `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>${esc(from)} — ${esc(to)}</title><link rel="canonical" href="${u}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url=${u}"></head><body><a href="${u}">${esc(to)}</a></body></html>`);
}
// Shows
const shows = D.shows.map(s => ({ ...s, ids: (s.v || []).filter(live) })).filter(s => s.ids.length);
for (const sh of shows) {
  const s = slug(sh.id === "lrecs" ? sh.name : sname(sh)), url = `${SITE}/show/${s}/`;
  const byDate = sh.asc ? sh.ids.slice() : sh.ids.slice().sort((a, b) => (V[b].f || "").localeCompare(V[a].f || ""));
  const cast = [...new Set(sh.ids.flatMap(id => V[id].c || []))].slice(0, 12);
  const desc = `${sh.name}: ${sh.tag || "humor cubano"} ${sh.ids.length} episodios${cast.length ? " con " + cast.slice(0, 5).join(", ") : ""}. En El Home de la Risa.`.replace(/\.\s*(\d)/, ". $1");
  const image = abs(sh.banner) || thumb(byDate[0]);
  write(`show/${s}`, page({ url, title: `${sh.name} — todos los episodios | El Home de la Risa`, desc, image,
    body: `<section class="hero"><img src="${esc(image)}" alt="${esc(sh.name)}"><div><h1>${esc(sh.name)}</h1><p class="lead">${esc(desc)}</p><div class="btns"><a class="btn b1" href="${wurl(byDate[0])}" target="_blank" rel="noopener">▶ Ver el último episodio</a><a class="btn b2" href="/?show=${sh.id}">Abrir en El Home</a>${sh.sub ? `<a class="btn b2" href="${esc(sh.sub)}" target="_blank" rel="noopener">Suscribirme en YouTube</a>` : ""}</div></div></section>
${cast.length ? `<h2>Humoristas</h2><div class="chips">${cast.map(n => { const o = comics.find(c => c.name === n || (c.aka || []).includes(n)); return o ? `<a class="chip" href="/humorista/${slug(o.name)}/">${esc(n)}</a>` : `<span class="chip">${esc(n)}</span>`; }).join("")}</div>` : ""}
${upSec(sh.v || [])}<h2>Episodios</h2><div class="grid">${byDate.map(vcard).join("")}</div>`,
    ld: { "@context": "https://schema.org", "@graph": [
      { "@type": "TVSeries", "@id": url + "#serie", name: sh.name, description: sh.tag, url, image, inLanguage: "es", genre: "Comedia", productionCompany: { "@type": "Organization", name: "Marrero Bernal Media LLC", url: "https://marrerobernalmedia.com/" }, actor: cast.map(n => ({ "@type": "Person", name: n })) },
      { "@type": "ItemList", name: `Episodios de ${sh.name}`, itemListElement: videoLD(byDate) },
      { "@type": "BreadcrumbList", itemListElement: [{ "@type": "ListItem", position: 1, name: "El Home de la Risa", item: SITE + "/" }, { "@type": "ListItem", position: 2, name: "Shows", item: SITE + "/shows/" }, { "@type": "ListItem", position: 3, name: sh.name, item: url }] }] } }));
  urls.push({ loc: url, pr: "0.8", cf: "weekly" });
}
// Shows renombrados: la URL vieja manda a la nueva
for (const [from, to] of [["Noticias de Ayer", "Manual del Cubano"]]) {
  const u = `${SITE}/show/${slug(to)}/`;
  write(`show/${slug(from)}`, `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>${esc(from)} — ${esc(to)}</title><link rel="canonical" href="${u}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url=${u}"></head><body><a href="${u}">${esc(to)}</a></body></html>`);
}
// Índices
write("humoristas", page({ url: `${SITE}/humoristas/`, title: "Humoristas cubanos — todos sus videos | El Home de la Risa", desc: `Los ${comics.length} humoristas de El Home de la Risa, cada uno con todas sus presentaciones: ${comics.slice(0, 8).map(c => c.name).join(", ")} y más.`, image: `${SITE}/og.jpg`,
  body: `<h1 style="margin-top:28px">Humoristas</h1><p class="lead">Cada humorista con todas sus presentaciones, de la primera a la última.</p><div class="cards">${comics.map(c => `<a class="card" href="/humorista/${slug(c.name)}/"><img src="${esc(abs(c.banner) || thumb(c.ids[0] || c.up[0]))}" alt="${esc(c.name)}" loading="lazy"><div><b>${esc(c.name)}</b><small>${c.ids.length ? c.ids.length + " videos" : "Estreno el " + esc(fEst(V[c.up[0]].f))}</small></div></a>`).join("")}</div>`,
  ld: { "@context": "https://schema.org", "@type": "CollectionPage", name: "Humoristas de El Home de la Risa", url: `${SITE}/humoristas/` } }));
write("shows", page({ url: `${SITE}/shows/`, title: "Shows de humor cubano | El Home de la Risa", desc: `Todos los shows de El Home de la Risa: ${shows.map(s => s.name).join(", ")}.`, image: `${SITE}/og.jpg`,
  body: `<h1 style="margin-top:28px">Shows</h1><p class="lead">Todos los programas de la casa del humor cubano.</p><div class="cards">${shows.map(s => `<a class="card" href="/show/${slug(s.id === "lrecs" ? s.name : sname(s))}/"><img src="${esc(abs(s.banner) || thumb(s.ids[0]))}" alt="${esc(s.name)}" loading="lazy"><div><b>${esc(s.name)}</b><small>${s.ids.length} episodios</small></div></a>`).join("")}</div>`,
  ld: { "@context": "https://schema.org", "@type": "CollectionPage", name: "Shows de El Home de la Risa", url: `${SITE}/shows/` } }));
urls.splice(1, 0, { loc: `${SITE}/shows/`, pr: "0.9", cf: "weekly" }, { loc: `${SITE}/humoristas/`, pr: "0.9", cf: "weekly" });

fs.writeFileSync(path.join(out, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `  <url><loc>${u.loc}</loc><lastmod>${today}</lastmod><changefreq>${u.cf}</changefreq><priority>${u.pr}</priority></url>`).join("\n")}\n</urlset>\n`);
console.log(`humoristas ${comics.length}, shows ${shows.length}, sitemap ${urls.length} URLs`);
