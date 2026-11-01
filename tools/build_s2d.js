// Genera el sitio en inglés www.straight2dchest.com en la carpeta s2d/
// Uso: node tools/build_s2d.js   (lee recta/data.js para duración, fecha y vistas)
const fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, ".."), OUT = path.join(ROOT, "s2d");
const SITE = "https://www.straight2dchest.com";
const YT_CH = "https://www.youtube.com/@RectaAlPecho";
const S = require("./s2d_data.js");
global.window = {}; require(path.join(ROOT, "recta/data.js"));
const RV = window.APPDATA.vid;
// Fechas y duración de YouTube (vidIQ) para los videos que recta/data.js no trae: Google pide uploadDate en VideoObject
const DT = (() => { try { return require("./s2d_dates.json"); } catch (e) { return {}; } })();

const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const V = S.v.map(([id, c, slug, who, t, sum]) => {
  const r = RV[id] || {};
  const dt = DT[id] || {};
  return { id, c, slug, who, t, sum, d: r.d || "", f: r.f || dt.f || "", iso: dt.dur || "", views: r.v || 0 };
});
const byId = Object.fromEntries(V.map(v => [v.id, v]));
// Noticias en inglés: una por artículo de rectaalpecho.com (tools/s2d_news/*.json). Solo salen las de fecha <= hoy (Las Vegas).
const TODAY = new Date(Date.now() - 8 * 3600e3).toISOString().slice(0, 10);
const NEWS_DIR = path.join(__dirname, "s2d_news");
const NEWS = (fs.existsSync(NEWS_DIR) ? fs.readdirSync(NEWS_DIR).filter(f => f.endsWith(".json")) : [])
  .map(f => JSON.parse(fs.readFileSync(path.join(NEWS_DIR, f), "utf8")))
  .filter(n => n.date <= TODAY)
  .sort((a, b) => b.date.localeCompare(a.date) || b.recta_id - a.recta_id);
const SERIES = [
  { id: "los-borrados", slug: "the-erased", name: "The Erased", tag: "The players Cuba wiped from the record books and from television." },
  { id: "las-fugas", slug: "the-defections", name: "The Defections", tag: "How they got out, told in the first person." },
  { id: "los-que-dijeron-no", slug: "they-said-no", name: "They Said No", tag: "They turned down the millions. This is what they got." },
  { id: "las-glorias-en-el-piso", slug: "forgotten-champions", name: "Forgotten Champions", tag: "Team Cuba champions who live forgotten today." },
  { id: "la-hipocresia-en-el-beisbol", slug: "myths", name: "Myths & Analysis", tag: "What fans keep repeating, against the numbers." }
];
const newsImg = n => n.image || (n.video ? big(n.video) : SITE + "/img/og.jpg");
function ncard(n, P) {
  return `<a class="card" href="${P}news/${n.slug}/">
  <span class="th"><img src="${newsImg(n)}" alt="" loading="lazy" width="480" height="270"></span>
  <span class="who">${esc((SERIES.find(x => x.id === n.series) || {}).name || fdate(n.date))}</span>
  <span class="ttl">${esc(n.title)}</span>
</a>`;
}

// Miniatura en inglés propia (s2d/img/th/<id>.jpg, 1280x720) si existe; si no, la de YouTube.
const hasTh = id => fs.existsSync(path.join(OUT, "img/th", id + ".jpg"));
const hasSm = id => fs.existsSync(path.join(OUT, "img/th_sm", id + ".jpg")); // 336px en inglés bajados de YouTube
const thumb = id => hasTh(id) ? `${SITE}/img/th/${id}.jpg` : hasSm(id) ? `${SITE}/img/th_sm/${id}.jpg` : `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
const big = id => hasTh(id) ? `${SITE}/img/th/${id}.jpg` : `https://i.ytimg.com/vi/${id}/maxresdefault.jpg`;
const isoDur = d => { const p = d.split(":").map(Number); while (p.length < 3) p.unshift(0); return `PT${p[0] ? p[0] + "H" : ""}${p[1]}M${p[2]}S`; };
const human = d => { const p = d.split(":").map(Number); if (p.length === 3) return `${p[0]} h ${p[1]} min`; return `${p[0]} min`; };
const MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const fdate = f => { if (!f) return ""; const [y, m, d] = f.split("-").map(Number); return `${MON[m - 1]} ${d}, ${y}`; };
const BUILD = new Date().toISOString().slice(0, 10);

const css = fs.readFileSync(path.join(__dirname, "s2d_style.css"), "utf8");
const CSSV = require("crypto").createHash("md5").update(css).digest("hex").slice(0, 8); // cambia cuando cambia el CSS (evita la caché vieja)
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, "style.css"), css);

function page({ rel, title, desc, canon, body, og, ld, type, alt_es, noindex }) {
  const P = rel; // prefijo relativo a la raíz ("" o "../")
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
${noindex ? '<meta name="robots" content="noindex">' : `<link rel="canonical" href="${canon}">`}
${rel === "" ? `<link rel="alternate" hreflang="en" href="${SITE}/"><link rel="alternate" hreflang="es" href="https://rectaalpecho.com/">` : ""}${alt_es ? `<link rel="alternate" hreflang="en" href="${canon}"><link rel="alternate" hreflang="es" href="${alt_es}">` : ""}
<meta property="og:type" content="${type || "website"}">
<meta property="og:site_name" content="Straight 2D Chest">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${canon}">
<meta property="og:image" content="${og || SITE + "/img/og.jpg"}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1a3a">
<link rel="icon" type="image/png" href="${P}img/favicon.png">
<link rel="apple-touch-icon" href="${P}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,600;0,700;0,800;1,800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${P}style.css?v=${CSSV}">
${ld ? `<script type="application/ld+json">${JSON.stringify(ld)}</script>` : ""}
</head>
<body>
<header class="top"><div class="wrap top-in">
 <a class="brand" href="${P || "./"}"><img src="${P}img/logo-h.webp" alt="Straight 2D Chest" width="560" height="285"></a>
 <nav>${SERIES.map(x => `<a href="${P}series/${x.slug}/">${x.name.replace(" & Analysis", "")}</a>`).join("")}<a href="${P}#interviews">Interviews</a><a href="${P}about/">About</a><a class="app" href="${P}#app">📲 App</a><a class="sub" href="${YT_CH}?sub_confirmation=1" rel="noopener">Subscribe</a></nav>
 <span class="lang" role="group" aria-label="Language / Idioma"><a href="${alt_es || "https://rectaalpecho.com/"}" hreflang="es" lang="es" title="Español — Recta Al Pecho"><svg viewBox="0 0 30 20" width="22" height="15" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg><b>ES</b></a><a href="${canon}" hreflang="en" class="on" title="English"><svg viewBox="0 0 38 20" width="22" height="15" aria-hidden="true"><rect width="38" height="20" fill="#fff"/><g fill="#b22234"><rect width="38" height="1.54"/><rect y="3.08" width="38" height="1.54"/><rect y="6.15" width="38" height="1.54"/><rect y="9.23" width="38" height="1.54"/><rect y="12.31" width="38" height="1.54"/><rect y="15.38" width="38" height="1.54"/><rect y="18.46" width="38" height="1.54"/></g><rect width="15.2" height="10.77" fill="#3c3b6e"/></svg><b>EN</b></a></span>
</div></header>
<a class="appbar" href="https://marrerobernalmedia.com/recta/?lang=en" rel="noopener"><img src="${P}img/apple-touch-icon.png" alt="" width="36" height="36"><span><b>Straight 2D Chest app</b><small>Free · every interview with English audio</small></span><em>Get the app</em></a>
${body}
<footer class="foot"><div class="wrap foot-in">
 <img src="${P}img/logo-h.webp" alt="" width="280" height="142" loading="lazy">
 <div>
  <p><strong>Straight 2D Chest</strong> is the English edition of <a href="https://rectaalpecho.com/" hreflang="es">Recta Al Pecho</a>, the sports interview show where baseball is the passion.</p>
  <p><a href="${YT_CH}" rel="noopener">YouTube</a> · <a href="${P}about/">About</a> · <a href="https://marrerobernalmedia.com/" rel="noopener">Marrero Bernal Media</a></p>
  <p class="legal">© ${BUILD.slice(0, 4)} Marrero Bernal Media LLC. All rights reserved.</p>
 </div>
</div></footer>
<script>
document.addEventListener("click",function(e){var b=e.target.closest("[data-yt]");if(!b)return;e.preventDefault();
var f=document.createElement("iframe");f.src="https://www.youtube-nocookie.com/embed/"+b.dataset.yt+"?autoplay=1&hl=en&cc_lang_pref=en&rel=0";
f.allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";f.allowFullscreen=true;f.title=b.getAttribute("aria-label")||"Video";b.replaceWith(f);});
</script>
</body>
</html>
`;
}

function card(v, P) {
  return `<a class="card" href="${P}${v.slug}/">
  <span class="th"><img src="${thumb(v.id)}" alt="" loading="lazy" width="480" height="360">${v.d ? `<span class="dur">${v.d}</span>` : ""}</span>
  <span class="who">${esc(v.who)}</span>
  <span class="ttl">${esc(v.t)}</span>
</a>`;
}

const HOWTO = `<div class="howto"><strong>Hear it in English</strong><ol><li>Press play.</li><li>Open <b>⚙ Settings</b> (on the YouTube app: <b>⋮</b>).</li><li>Choose <b>Audio track → English</b>.</li></ol></div>`;

// ── Home (misma estructura que rectaalpecho.com: portada con lo último, último capítulo, series, entrevistas)
{
  const lead = NEWS[0], side = NEWS.slice(1, 4);
  const lastEp = V.filter(v => v.f).sort((x, y) => y.f.localeCompare(x.f))[0];
  const serieOf = n => SERIES.find(x => x.id === n.series);
  const body = `
<main class="wrap">
${lead ? `<section class="r-hero">
 <a class="r-big" href="news/${lead.slug}/"><img src="${newsImg(lead)}" alt="" fetchpriority="high"><div class="txt">${serieOf(lead) ? `<span class="kicker">${esc(serieOf(lead).name)}</span>` : ""}<h1>${esc(lead.title)}</h1><p>${esc(lead.dek)}</p></div></a>
 <aside class="r-side"><h3>Latest</h3>
 ${side.map(n => `<a class="mini" href="news/${n.slug}/"><img src="${newsImg(n)}" alt="" loading="lazy"><span><small>${esc(serieOf(n) ? serieOf(n).name : "Story")}</small><b>${esc(n.title)}</b></span></a>`).join("")}
 </aside>
</section>` : ""}

${lastEp ? `<section class="r-yt">
 <button class="player" data-yt="${lastEp.id}" aria-label="Play: ${esc(lastEp.t)}"><img src="${big(lastEp.id)}" alt="" loading="lazy"><span class="play"></span></button>
 <div><h3>Latest episode on YouTube</h3><h2>${esc(lastEp.who)}: ${esc(lastEp.t)}</h2><p>Premiered ${fdate(lastEp.f)}. Full interview with English audio.</p><a class="btn" href="${lastEp.slug}/">Watch the interview</a>
 <div class="next"><h3>New interview every Thursday</h3><span>Interviews in Spanish carry an English audio track on YouTube — and more and more are recorded in English.</span></div></div>
</section>` : ""}

</main>
<section class="appband" id="app"><div class="wrap appband-in">
 <img src="img/icon-512.png" alt="Straight 2D Chest app" width="120" height="120" loading="lazy">
 <div>
  <small>Free app</small><h2>Get Straight 2D Chest on your phone</h2>
  <p>Every interview with English audio, the series, the myths and the stories — plus an alert when a new episode premieres.</p>
  <div class="app-btns">
   <a class="btn" href="https://marrerobernalmedia.com/recta/?lang=en" rel="noopener">Open the app</a>
   <a class="btn ghost" href="https://marrerobernalmedia.com/apk/recta.apk">Android · Download (APK)</a>
  </div>
  <p class="nota">iPhone: open the app in Safari, tap Share, then “Add to Home Screen”. Android: Chrome menu ⋮ → “Install app”, or download the APK. Coming soon to Google Play and the App Store.</p>
 </div>
</div></section>
<main class="wrap">
${SERIES.map(sr => { const ps = NEWS.filter(n => n.series === sr.id).slice(0, 4); if (!ps.length) return "";
  return `<section class="r-sec" id="${sr.slug}"><div class="sec-h"><h2>${esc(sr.name)}</h2><p>${esc(sr.tag)}</p><a href="series/${sr.slug}/">See all →</a></div><div class="grid">${ps.map(n => ncard(n, "")).join("")}</div></section>`; }).join("\n")}
</main>

<div id="interviews"></div>
<section class="wrap cat"><div class="cat-head"><h2 class="sec">Interviews with English audio</h2><p>Every full interview here has an English audio track on YouTube.</p></div></section>
${S.cats.map(c => {
    const list = V.filter(v => v.c === c.id);
    return `<section class="wrap cat" id="${c.id}">
 <div class="cat-head"><h2 class="sec sm">${esc(c.name)}</h2><p>${esc(c.tag)}</p></div>
 <div class="grid">${list.map(v => card(v, "")).join("")}</div>
</section>`;
  }).join("\n")}



<section class="band"><div class="wrap band-in">
 <div><h2>How the English audio works</h2><p>Most of our interviews are recorded in Spanish. On YouTube, each one carries an English audio track, so you can watch the whole conversation in English. Interviews recorded in English are on the way.</p></div>
 ${HOWTO}
</div></section>
`;
  const ld = { "@context": "https://schema.org", "@type": "WebSite", name: "Straight 2D Chest", alternateName: "Recta Al Pecho (English)", url: SITE + "/", inLanguage: "en", publisher: { "@type": "Organization", name: "Marrero Bernal Media LLC", url: "https://marrerobernalmedia.com/", sameAs: ["https://x.com/MarreroBernalTV"] },
  };
  const org = { "@context": "https://schema.org", "@type": "Organization", name: "Straight 2D Chest", alternateName: "Recta Al Pecho", url: SITE + "/", logo: SITE + "/img/icon-512.png",
    sameAs: ["https://www.youtube.com/@RectaAlPecho", "https://www.facebook.com/RectaAlPecho", "https://rectaalpecho.com/"],
    parentOrganization: { "@type": "Organization", name: "Marrero Bernal Media LLC", url: "https://marrerobernalmedia.com/" } };
  fs.writeFileSync(path.join(OUT, "index.html"), page({ rel: "", title: "Straight 2D Chest — Sports · Baseball Is the Passion", desc: "Sports · Baseball is the passion. Long, uncensored interviews with the people who lived the game — big leaguers, legends and the stories nobody told. The English edition of Recta Al Pecho.", canon: SITE + "/", body, ld: [ld, org] }));
}

// ── Interview pages
for (const v of V) {
  const cat = S.cats.find(c => c.id === v.c);
  const more = V.filter(x => x.c === v.c && x.id !== v.id).slice(0, 4);
  const meta = [v.d && human(v.d), v.f && fdate(v.f), "Spanish with English audio"].filter(Boolean).join(" · ");
  const body = `
<main class="wrap vid">
 <p class="crumb"><a href="../">Home</a> › <a href="../#${cat.id}">${esc(cat.name)}</a></p>
 <div class="vid-grid">
  <div>
   <button class="player" data-yt="${v.id}" aria-label="Play: ${esc(v.t)}"><img src="${big(v.id)}" alt="" width="1280" height="720"><span class="play"></span></button>
   <p class="who">${esc(v.who)}</p>
   <h1>${esc(v.t)}</h1>
   <p class="meta">${meta}</p>
   <p class="sum">${esc(v.sum)}</p>
   <p class="cta"><a class="btn" href="https://www.youtube.com/watch?v=${v.id}" rel="noopener">Watch on YouTube</a><a class="btn ghost" href="${YT_CH}?sub_confirmation=1" rel="noopener">Subscribe</a></p>
  </div>
  <aside>${HOWTO}<div class="es"><strong>¿Prefieres en español?</strong><p>Este video es de <a href="https://rectaalpecho.com/" hreflang="es">Recta Al Pecho</a>. En YouTube, el audio original es el español.</p></div></aside>
 </div>
 ${more.length ? `<section class="cat"><h2 class="sec">More from ${esc(cat.name)}</h2><div class="grid">${more.map(x => card(x, "../")).join("")}</div></section>` : ""}
</main>`;
  const ld = {
    "@context": "https://schema.org", "@type": "VideoObject", name: v.t, description: v.sum,
    thumbnailUrl: [big(v.id)],
    embedUrl: `https://www.youtube.com/embed/${v.id}`, contentUrl: `https://www.youtube.com/watch?v=${v.id}`,
    inLanguage: "es", publisher: { "@type": "Organization", name: "Marrero Bernal Media LLC" }
  };
  if (v.d) ld.duration = isoDur(v.d); else if (v.iso) ld.duration = v.iso;
  if (v.f) ld.uploadDate = v.f;
  if (v.views) ld.interactionStatistic = { "@type": "InteractionCounter", interactionType: { "@type": "WatchAction" }, userInteractionCount: v.views };
  const crumbs = { "@context": "https://schema.org", "@type": "BreadcrumbList", itemListElement: [
    { "@type": "ListItem", position: 1, name: "Straight 2D Chest", item: SITE + "/" },
    { "@type": "ListItem", position: 2, name: cat.name, item: SITE + "/#" + v.c },
    { "@type": "ListItem", position: 3, name: v.who, item: `${SITE}/${v.slug}/` }] };
  fs.mkdirSync(path.join(OUT, v.slug), { recursive: true });
  fs.writeFileSync(path.join(OUT, v.slug, "index.html"), page({ rel: "../", title: `${v.who}: ${v.t} | Straight 2D Chest`, desc: v.sum, canon: `${SITE}/${v.slug}/`, body, og: big(v.id), ld: [ld, crumbs], type: "video.other" }));
}

// ── Stories (news)
{
  fs.rmSync(path.join(OUT, "news"), { recursive: true, force: true });
  fs.mkdirSync(path.join(OUT, "news"), { recursive: true });
  const body = `<main class="wrap"><section class="cat"><div class="cat-head"><h1 class="sec">Stories</h1><p>English editions of the Recta Al Pecho articles: the stories behind the interviews.</p></div><div class="grid">${NEWS.map(n => ncard(n, "../")).join("")}</div></section></main>`;
  fs.writeFileSync(path.join(OUT, "news", "index.html"), page({ rel: "../", title: "Stories | Straight 2D Chest", desc: "Baseball stories in English — the English editions of the Recta Al Pecho articles.", canon: SITE + "/news/", body }));
  for (const n of NEWS) {
    const iv = n.video && byId[n.video];
    const more = NEWS.filter(x => x.slug !== n.slug).slice(0, 4);
    const body = `
<main class="wrap art">
 <p class="crumb"><a href="../../">Home</a> › <a href="../">Stories</a></p>
 <article>
  <p class="who">${fdate(n.date)} · By Eliam Marrero Bernal</p>
  <h1>${esc(n.title)}</h1>
  <p class="dek">${esc(n.dek)}</p>
  ${n.video ? `<button class="player" data-yt="${n.video}" aria-label="Play the interview"><img src="${big(n.video)}" alt="" width="1280" height="720"><span class="play"></span></button><p class="meta">Watch the full interview — English audio: ⚙ Settings → Audio track → English.${iv ? ` <a href="../../${iv.slug}/">Interview page →</a>` : ""}</p>` : (n.image ? `<img class="hero-img" src="${n.image}" alt="">` : "")}
  <div class="prose-body">${n.body_html}</div>
  <p class="orig">Originally published in Spanish on <a href="${n.recta_url}" hreflang="es">Recta Al Pecho</a>.</p>
 </article>
 ${more.length ? `<section class="cat"><h2 class="sec">More stories</h2><div class="grid">${more.map(x => ncard(x, "../../")).join("")}</div></section>` : ""}
</main>`;
    const ld = { "@context": "https://schema.org", "@type": "NewsArticle", headline: n.title, description: n.dek, datePublished: n.date, inLanguage: "en", image: [newsImg(n)], author: { "@type": "Person", name: "Eliam Marrero Bernal" }, publisher: { "@type": "Organization", name: "Marrero Bernal Media LLC" }, mainEntityOfPage: `${SITE}/news/${n.slug}/`, translationOfWork: { "@type": "Article", url: n.recta_url, inLanguage: "es" } };
    fs.mkdirSync(path.join(OUT, "news", n.slug), { recursive: true });
    fs.writeFileSync(path.join(OUT, "news", n.slug, "index.html"), page({ rel: "../../", title: `${n.title} | Straight 2D Chest`, desc: n.dek, canon: `${SITE}/news/${n.slug}/`, body, og: newsImg(n), ld, type: "article", alt_es: n.recta_url }));
  }
  // Mapa para el selector de idioma de rectaalpecho.com: artículo en español → su versión en inglés
  const map = Object.fromEntries(NEWS.map(n => [n.recta_slug, `${SITE}/news/${n.slug}/`]));
  fs.writeFileSync(path.join(ROOT, "themes/recta/en_map.json"), JSON.stringify(map, null, 1));
}

// ── Series pages
{
  fs.rmSync(path.join(OUT, "series"), { recursive: true, force: true });
  for (const sr of SERIES) {
    const ps = NEWS.filter(n => n.series === sr.id);
    const body = `<main class="wrap"><section class="cat"><p class="crumb"><a href="../../">Home</a> › Series</p><div class="cat-head"><h1 class="sec">${esc(sr.name)}</h1><p>${esc(sr.tag)}</p></div><div class="grid">${ps.map(n => ncard(n, "../../")).join("")}</div></section></main>`;
    fs.mkdirSync(path.join(OUT, "series", sr.slug), { recursive: true });
    fs.writeFileSync(path.join(OUT, "series", sr.slug, "index.html"), page({ rel: "../../", title: `${sr.name} | Straight 2D Chest`, desc: sr.tag, canon: `${SITE}/series/${sr.slug}/`, body, alt_es: `https://rectaalpecho.com/category/${sr.id}/` }));
  }
}

// ── About
{
  const body = `
<main class="wrap prose">
 <h1>About Straight 2D Chest</h1>
 <p><strong>Straight 2D Chest</strong> is the English edition of <a href="https://rectaalpecho.com/" hreflang="es">Recta Al Pecho</a> — in baseball slang, a fastball thrown right at the letters. That is how we ask the questions.</p>
 <p>Sports, with baseball as the passion. We sit down with the people who lived the game: big leaguers, national-team veterans, the players who defected to reach the Major Leagues, and the legends who were forgotten. We started with Cuban baseball, and the conversation keeps growing — Venezuela, the rest of Latin America and, more and more, interviews recorded in English. The conversations are long, unedited in spirit and uncensored. Some were recorded in Miami, some in Cuba.</p>
 <p>Most interviews so far were recorded in Spanish, and every one of them on this site has an <strong>English audio track</strong> on YouTube, so English-speaking fans can follow the whole conversation.</p>
 ${HOWTO}
 <h2>Who makes it</h2>
 <p>Straight 2D Chest and Recta Al Pecho are produced by <a href="https://marrerobernalmedia.com/">Marrero Bernal Media LLC</a>, an independent media company. New interviews premiere every Thursday on the <a href="${YT_CH}" rel="noopener">Recta Al Pecho YouTube channel</a>.</p>
</main>`;
  fs.mkdirSync(path.join(OUT, "about"), { recursive: true });
  fs.writeFileSync(path.join(OUT, "about", "index.html"), page({ rel: "../", title: "About | Straight 2D Chest", desc: "Straight 2D Chest is the English edition of Recta Al Pecho, the sports interview show where baseball is the passion, by Marrero Bernal Media.", canon: SITE + "/about/", body }));
}

// ── 404, robots, sitemap, .htaccess
fs.writeFileSync(path.join(OUT, "404.html"), page({ rel: "/", title: "Page not found | Straight 2D Chest", desc: "Page not found.", canon: SITE + "/", noindex: true, body: `<main class="wrap prose"><h1>Strike three — page not found.</h1><p><a class="btn" href="/">Back to the interviews</a></p></main>` }));
// Verificación de Google Search Console (cuenta personal de Eliam; mismo archivo que El Home y MBM). No borrar.
fs.writeFileSync(path.join(OUT, "googlea64675e7d49037bc.html"), "google-site-verification: googlea64675e7d49037bc.html");
fs.writeFileSync(path.join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${SITE}/sitemap.xml\n`);
const urls = [SITE + "/", SITE + "/about/", SITE + "/news/", ...SERIES.map(x => `${SITE}/series/${x.slug}/`), ...V.map(v => `${SITE}/${v.slug}/`), ...NEWS.map(n => `${SITE}/news/${n.slug}/`)];
fs.writeFileSync(path.join(OUT, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `<url><loc>${u}</loc><lastmod>${BUILD}</lastmod></url>`).join("\n")}\n</urlset>\n`);
fs.writeFileSync(path.join(OUT, ".htaccess"), `# straight2dchest.com — sitio estático (generado por tools/build_s2d.js)
ErrorDocument 404 /404.html
RewriteEngine On
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\\. [NC]
RewriteCond %{HTTP_HOST} straight2dchest\\.com$ [NC]
RewriteRule ^ https://www.straight2dchest.com%{REQUEST_URI} [L,R=301]
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType image/webp "access plus 30 days"
ExpiresByType image/png "access plus 30 days"
ExpiresByType image/jpeg "access plus 30 days"
ExpiresByType text/css "access plus 7 days"
</IfModule>
`);
console.log(`s2d: ${V.length} entrevistas, ${urls.length} URLs en el sitemap`);

// ── recta/en.js: la app de Recta en inglés usa estos datos (mismos textos que straight2dchest.com)
{
  const thIds = fs.readdirSync(path.join(OUT, "img/th")).filter(f => f.endsWith(".jpg")).map(f => f.replace(/\.jpg$/, ""));
  const E = {
    vid: Object.fromEntries(V.map(v => [v.id, { t: v.t, p: v.who, s: v.slug }])),
    th: thIds,
    series: S.appSeries || {},
    myths: (S.appMyths || []).filter(m => byId[m[2]]),
    stories: NEWS.slice(0, 15).map(n => [n.title, fdate(n.date), `${SITE}/news/${n.slug}/`, n.video && byId[n.video] ? n.video : "", n.dek, newsImg(n)])
  };
  fs.writeFileSync(path.join(ROOT, "recta/en.js"), "// Generado por tools/build_s2d.js — no editar a mano\nwindow.RECTA_EN = " + JSON.stringify(E) + ";\n");
}
