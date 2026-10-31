// Genera el sitio en inglés www.straight2dchest.com en la carpeta s2d/
// Uso: node tools/build_s2d.js   (lee recta/data.js para duración, fecha y vistas)
const fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, ".."), OUT = path.join(ROOT, "s2d");
const SITE = "https://www.straight2dchest.com";
const YT_CH = "https://www.youtube.com/@RectaAlPecho";
const S = require("./s2d_data.js");
global.window = {}; require(path.join(ROOT, "recta/data.js"));
const RV = window.APPDATA.vid;

const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const V = S.v.map(([id, c, slug, who, t, sum]) => {
  const r = RV[id] || {};
  return { id, c, slug, who, t, sum, d: r.d || "", f: r.f || "", views: r.v || 0 };
});
const byId = Object.fromEntries(V.map(v => [v.id, v]));
// Noticias en inglés: una por artículo de rectaalpecho.com (tools/s2d_news/*.json). Solo salen las de fecha <= hoy (Las Vegas).
const TODAY = new Date(Date.now() - 8 * 3600e3).toISOString().slice(0, 10);
const NEWS_DIR = path.join(__dirname, "s2d_news");
const NEWS = (fs.existsSync(NEWS_DIR) ? fs.readdirSync(NEWS_DIR).filter(f => f.endsWith(".json")) : [])
  .map(f => JSON.parse(fs.readFileSync(path.join(NEWS_DIR, f), "utf8")))
  .filter(n => n.date <= TODAY)
  .sort((a, b) => b.date.localeCompare(a.date) || b.recta_id - a.recta_id);
const newsImg = n => n.image || (n.video ? big(n.video) : SITE + "/img/og.jpg");
function ncard(n, P) {
  return `<a class="card" href="${P}news/${n.slug}/">
  <span class="th"><img src="${newsImg(n)}" alt="" loading="lazy" width="480" height="270"><span class="en">Story</span></span>
  <span class="who">${fdate(n.date)}</span>
  <span class="ttl">${esc(n.title)}</span>
</a>`;
}

// Miniatura en inglés propia (s2d/img/th/<id>.jpg, 1280x720) si existe; si no, la de YouTube.
const hasTh = id => fs.existsSync(path.join(OUT, "img/th", id + ".jpg"));
const thumb = id => hasTh(id) ? `${SITE}/img/th/${id}.jpg` : `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
const big = id => hasTh(id) ? `${SITE}/img/th/${id}.jpg` : `https://i.ytimg.com/vi/${id}/maxresdefault.jpg`;
const isoDur = d => { const p = d.split(":").map(Number); while (p.length < 3) p.unshift(0); return `PT${p[0] ? p[0] + "H" : ""}${p[1]}M${p[2]}S`; };
const human = d => { const p = d.split(":").map(Number); if (p.length === 3) return `${p[0]} h ${p[1]} min`; return `${p[0]} min`; };
const MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const fdate = f => { if (!f) return ""; const [y, m, d] = f.split("-").map(Number); return `${MON[m - 1]} ${d}, ${y}`; };
const BUILD = new Date().toISOString().slice(0, 10);

const css = fs.readFileSync(path.join(__dirname, "s2d_style.css"), "utf8");
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, "style.css"), css);

function page({ rel, title, desc, canon, body, og, ld, type, alt_es }) {
  const P = rel; // prefijo relativo a la raíz ("" o "../")
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${canon}">
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
<link rel="stylesheet" href="${P}style.css?v=${BUILD}">
${ld ? `<script type="application/ld+json">${JSON.stringify(ld)}</script>` : ""}
</head>
<body>
<header class="top"><div class="wrap top-in">
 <a class="brand" href="${P || "./"}"><img src="${P}img/logo-h.webp" alt="Straight 2D Chest" width="560" height="285"></a>
 <nav><a href="${P}#interviews">Interviews</a><a href="${P}news/">Stories</a><a href="${P}about/">About</a><a class="sub" href="${YT_CH}?sub_confirmation=1" rel="noopener">Subscribe</a></nav>
 <span class="lang" role="group" aria-label="Language / Idioma"><a href="${alt_es || "https://rectaalpecho.com/"}" hreflang="es" lang="es" title="Español — Recta Al Pecho"><svg viewBox="0 0 30 20" width="22" height="15" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg><b>ES</b></a><a href="${canon}" hreflang="en" class="on" title="English"><svg viewBox="0 0 38 20" width="22" height="15" aria-hidden="true"><rect width="38" height="20" fill="#fff"/><g fill="#b22234"><rect width="38" height="1.54"/><rect y="3.08" width="38" height="1.54"/><rect y="6.15" width="38" height="1.54"/><rect y="9.23" width="38" height="1.54"/><rect y="12.31" width="38" height="1.54"/><rect y="15.38" width="38" height="1.54"/><rect y="18.46" width="38" height="1.54"/></g><rect width="15.2" height="10.77" fill="#3c3b6e"/></svg><b>EN</b></a></span>
</div></header>
${body}
<footer class="foot"><div class="wrap foot-in">
 <img src="${P}img/logo-h.webp" alt="" width="280" height="142" loading="lazy">
 <div>
  <p><strong>Straight 2D Chest</strong> is the English edition of <a href="https://rectaalpecho.com/" hreflang="es">Recta Al Pecho</a>, the uncensored Cuban baseball interview show.</p>
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
  <span class="th"><img src="${thumb(v.id)}" alt="" loading="lazy" width="480" height="360">${v.d ? `<span class="dur">${v.d}</span>` : ""}<span class="en">EN audio</span></span>
  <span class="who">${esc(v.who)}</span>
  <span class="ttl">${esc(v.t)}</span>
</a>`;
}

const HOWTO = `<div class="howto"><strong>Hear it in English</strong><ol><li>Press play.</li><li>Open <b>⚙ Settings</b> (on the YouTube app: <b>⋮</b>).</li><li>Choose <b>Audio track → English</b>.</li></ol></div>`;

// ── Home
{
  const feat = S.featured.map(id => byId[id]);
  const lead = feat[0];
  const body = `
<section class="hero"><div class="wrap hero-in">
 <div class="hero-txt">
  <p class="kick">The English edition of Recta Al Pecho</p>
  <h1>Cuban baseball,<br><span>straight to the chest.</span></h1>
  <p class="lede">Long, uncensored conversations with the players who made Cuban baseball — big leaguers, defectors and the legends the system tried to erase. Every interview here has an English audio track.</p>
  <p class="cta"><a class="btn" href="#interviews">Browse the interviews</a><a class="btn ghost" href="${YT_CH}?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></p>
 </div>
 <img class="hero-logo" src="img/logo-sq.webp" alt="Straight 2D Chest logo: a batter in the stance" width="640" height="588">
</div></section>

<section class="wrap feat">
 <h2 class="sec">Start here</h2>
 <div class="feat-grid">
  <a class="feat-lead" href="${lead.slug}/"><span class="th"><img src="${big(lead.id)}" alt="" width="1280" height="720"><span class="en">EN audio</span></span><span class="who">${esc(lead.who)}</span><span class="ttl big">${esc(lead.t)}</span><span class="sum">${esc(lead.sum)}</span></a>
  <div class="feat-side">${feat.slice(1).map(v => card(v, "")).join("")}</div>
 </div>
</section>

${NEWS.length ? `<section class="wrap cat" id="stories"><div class="cat-head"><h2 class="sec">Latest stories</h2><p>The stories behind the interviews, translated from Recta Al Pecho. <a href="news/">All stories →</a></p></div><div class="grid">${NEWS.slice(0, 4).map(n => ncard(n, "")).join("")}</div></section>` : ""}
<div id="interviews"></div>
${S.cats.map(c => {
    const list = V.filter(v => v.c === c.id);
    return `<section class="wrap cat" id="${c.id}">
 <div class="cat-head"><h2 class="sec">${esc(c.name)}</h2><p>${esc(c.tag)}</p></div>
 <div class="grid">${list.map(v => card(v, "")).join("")}</div>
</section>`;
  }).join("\n")}

<section class="band"><div class="wrap band-in">
 <div><h2>How the English audio works</h2><p>The interviews are recorded in Spanish. On YouTube, each one carries an English audio track, so you can watch the whole conversation in English.</p></div>
 ${HOWTO}
</div></section>
`;
  const ld = { "@context": "https://schema.org", "@type": "WebSite", name: "Straight 2D Chest", alternateName: "Recta Al Pecho (English)", url: SITE + "/", inLanguage: "en", publisher: { "@type": "Organization", name: "Marrero Bernal Media LLC", url: "https://marrerobernalmedia.com/" } };
  fs.writeFileSync(path.join(OUT, "index.html"), page({ rel: "", title: "Straight 2D Chest — Cuban Baseball Interviews in English", desc: "Uncensored interviews with Cuban and Latin baseball legends — MLB stars, defectors and the greats Cuba tried to erase. The English edition of Recta Al Pecho.", canon: SITE + "/", body, ld }));
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
  if (v.d) ld.duration = isoDur(v.d);
  if (v.f) ld.uploadDate = v.f;
  if (v.views) ld.interactionStatistic = { "@type": "InteractionCounter", interactionType: { "@type": "WatchAction" }, userInteractionCount: v.views };
  fs.mkdirSync(path.join(OUT, v.slug), { recursive: true });
  fs.writeFileSync(path.join(OUT, v.slug, "index.html"), page({ rel: "../", title: `${v.who}: ${v.t} | Straight 2D Chest`, desc: v.sum, canon: `${SITE}/${v.slug}/`, body, og: big(v.id), ld, type: "video.other" }));
}

// ── Stories (news)
{
  fs.rmSync(path.join(OUT, "news"), { recursive: true, force: true });
  fs.mkdirSync(path.join(OUT, "news"), { recursive: true });
  const body = `<main class="wrap"><section class="cat"><div class="cat-head"><h1 class="sec">Stories</h1><p>English editions of the Recta Al Pecho articles: the stories behind the interviews.</p></div><div class="grid">${NEWS.map(n => ncard(n, "../")).join("")}</div></section></main>`;
  fs.writeFileSync(path.join(OUT, "news", "index.html"), page({ rel: "../", title: "Stories | Straight 2D Chest", desc: "Cuban baseball stories in English — the English editions of the Recta Al Pecho articles.", canon: SITE + "/news/", body }));
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

// ── About
{
  const body = `
<main class="wrap prose">
 <h1>About Straight 2D Chest</h1>
 <p><strong>Straight 2D Chest</strong> is the English edition of <a href="https://rectaalpecho.com/" hreflang="es">Recta Al Pecho</a> — in Cuban baseball slang, a fastball thrown right at the letters. That is how we ask the questions.</p>
 <p>We sit down with the people who lived Cuban baseball: Serie Nacional stars, Team Cuba veterans, the players who defected and reached the Major Leagues, and the ones who stayed and were forgotten. The conversations are long, unedited in spirit and uncensored. Some were recorded in Miami, some in Cuba.</p>
 <p>The interviews are recorded in Spanish. Every video on this site has an <strong>English audio track</strong> on YouTube, so English-speaking fans can follow the whole conversation.</p>
 ${HOWTO}
 <h2>Who makes it</h2>
 <p>Straight 2D Chest and Recta Al Pecho are produced by <a href="https://marrerobernalmedia.com/">Marrero Bernal Media LLC</a>, an independent media company. New Spanish-language interviews premiere every Thursday on the <a href="${YT_CH}" rel="noopener">Recta Al Pecho YouTube channel</a>.</p>
</main>`;
  fs.mkdirSync(path.join(OUT, "about"), { recursive: true });
  fs.writeFileSync(path.join(OUT, "about", "index.html"), page({ rel: "../", title: "About | Straight 2D Chest", desc: "Straight 2D Chest is the English edition of Recta Al Pecho, the uncensored Cuban baseball interview show by Marrero Bernal Media.", canon: SITE + "/about/", body }));
}

// ── 404, robots, sitemap, .htaccess
fs.writeFileSync(path.join(OUT, "404.html"), page({ rel: "/", title: "Page not found | Straight 2D Chest", desc: "Page not found.", canon: SITE + "/", body: `<main class="wrap prose"><h1>Strike three — page not found.</h1><p><a class="btn" href="/">Back to the interviews</a></p></main>` }));
fs.writeFileSync(path.join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${SITE}/sitemap.xml\n`);
const urls = [SITE + "/", SITE + "/about/", SITE + "/news/", ...V.map(v => `${SITE}/${v.slug}/`), ...NEWS.map(n => `${SITE}/news/${n.slug}/`)];
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
