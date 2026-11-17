// Modo TELEVISOR (Android TV / Google TV). Solo se activa dentro de la app de TV (su navegador lleva "MBMTV"
// en el user agent) o con ?tv=1 en la dirección para probarlo en un navegador normal. Fuera de eso no hace nada.
// Se maneja con el control remoto: flechas para moverse, OK para abrir, Atrás para volver.
(() => {
  let on = /MBMTV/.test(navigator.userAgent);
  try {
    if (/[?&]tv=1/.test(location.search)) sessionStorage.setItem("mbm-tv", "1");
    if (sessionStorage.getItem("mbm-tv") === "1") on = true;
  } catch (e) {}
  if (!on) return;
  const root = document.documentElement;
  root.classList.add("tv");

  const st = document.createElement("style");
  st.textContent = `
html.tv{font-size:18px}
html.tv body{font-size:18px}
html.tv .app{max-width:1280px}
html.tv nav.tabs [data-tab="entradas"],
html.tv #instBtn, html.tv #appBtn, html.tv .inst,
html.tv a[href*="marrerobernalmedia.com/apps"], html.tv a[href*="larisaapp.com"],
html.tv [data-share], html.tv .redwrap{display:none!important}
html.tv{overflow-x:hidden!important}
html.tv body{overflow-x:clip!important;max-width:100vw}
html.tv #bellBtn, html.tv .brand span, html.tv .en-aviso, html.tv [data-open-sheet], html.tv #pushBtn{display:none!important}
html.tv .hdrow{gap:12px;min-width:0}
html.tv .hdrow .hd{flex:0 1 auto;min-width:0;gap:12px}
html.tv .hdrow .brand{margin-right:4px}
html.tv .hdrow .brand b{font-size:20px;white-space:nowrap}
html.tv .hdrow .hd>img{width:44px;height:44px}
html.tv .hdrow nav.tabs div{gap:2px}
html.tv .hdrow nav.tabs button{padding:9px 11px;font-size:15px}
html.tv .hdrow .search{flex:1 1 200px;min-width:160px;max-width:none;margin-left:auto}
html.tv .mbp-top, html.tv .mbp-info, html.tv .mbp-acts, html.tv .mbp h4, html.tv .mbp-list{display:none!important}
html.tv .mbp-body{overflow:hidden}
html.tv .mbp-vid{position:fixed!important;inset:0;width:100vw!important;height:100vh!important;aspect-ratio:auto!important;z-index:1;background:#000}
html.tv .mbp.tvlist h4, html.tv .mbp.tvlist .mbp-list{display:block!important;position:relative;z-index:2}
html.tv .mbp.tvlist .mbp-list{display:flex!important;gap:14px;overflow-x:auto;padding:4px 28px 26px;scrollbar-width:none}
html.tv .mbp.tvlist .mbp-body{position:fixed;left:0;right:0;bottom:0;top:auto;z-index:2;overflow:visible;background:linear-gradient(transparent,rgba(0,0,0,.92) 30%);padding-top:60px}
html.tv .mbp.tvlist h4{margin:0 28px 10px;font-size:18px}
html.tv .mbp.tvlist .mbp-it{flex:none;width:240px;flex-direction:column;gap:6px;background:rgba(20,20,20,.9);padding:8px}
html.tv .mbp.tvlist .mbp-it img{width:100%}
html.tv .mbp.tvlist .mbp-it b{font-size:14px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
html.tv .mbp.tvlist .mbp-it span{display:none}
html.tv .mbp-vid iframe{pointer-events:none}
html.tv .mbp-fail.tv-foco{position:absolute!important;transform:none}
html.tv .mbp-snd.tv-foco{position:absolute!important;transform:translateX(-50%) scale(1.04)}
html.tv .tvhint{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:10001;background:rgba(0,0,0,.78);color:#fff;border-radius:999px;padding:10px 20px;font:600 16px/1.2 system-ui,sans-serif;pointer-events:none;transition:opacity .4s}
html.tv .tvhint.off{opacity:0}
html.tv .shead{grid-template-columns:minmax(0,3fr) minmax(0,2fr)!important;align-items:center}
html.tv .shead .pic{align-self:stretch;display:flex;align-items:center;background:#000}
html.tv .shead .pic img{width:100%;height:auto!important;aspect-ratio:16/9;object-fit:cover;display:block}
html.tv .shead .b{padding:14px 18px!important;align-self:stretch!important;display:flex;flex-direction:column;justify-content:center}
html.tv .shead h1{font-size:26px!important}
html.tv .shead p{font-size:14px}
html.tv .shead .btn{padding:10px 14px;font-size:14px}
html.tv :focus{outline:none}
html.tv .tv-foco{outline:4px solid var(--lime,#8fd11f)!important;outline-offset:4px;border-radius:12px;box-shadow:0 0 0 8px rgba(143,209,31,.25);transform:scale(1.04);transition:transform .12s, box-shadow .12s;position:relative;z-index:5}
html.tv nav.tabs button.tv-foco{transform:none}
html.tv input.tv-foco{transform:none}
`;
  (document.head || root).appendChild(st);
  const ph = () => { const q = document.getElementById("q"); if (q) q.placeholder = "Buscar…"; };
  ph(); document.addEventListener("DOMContentLoaded", ph);

  const SEL = 'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"]), [data-show], [data-comic], [data-tab-go], [data-sub], [data-play], [data-id]';
  const visible = el => {
    if (el.disabled || el.closest("[hidden]")) return false;
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) return false;
    const cs = getComputedStyle(el);
    return cs.visibility !== "hidden" && cs.display !== "none" && cs.opacity !== "0";
  };
  // Si el reproductor u otra ventana está abierta, solo se navega dentro de ella
  const scope = () => {
    const modal = [...document.querySelectorAll('.mbp:not([hidden]), [role="dialog"]')].filter(m => !m.closest("[hidden]") && visible(m)).pop();
    return modal || document;
  };
  const items = () => [...scope().querySelectorAll(SEL)].filter(el => !el.closest("iframe") && visible(el));

  let cur = null;
  const mark = el => {
    if (cur && cur !== el) cur.classList.remove("tv-foco");
    cur = el;
    if (!el) return;
    if (!el.matches('a[href],button,input,select,textarea,[tabindex]')) el.setAttribute("tabindex", "0");
    el.classList.add("tv-foco");
    try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); }
    // La pantalla sigue al cursor (sin animación: en el TV la animación se cortaba) y nunca se corre de lado
    if (el.closest("header, nav.tabs")) { (document.scrollingElement || root).scrollTop = 0; window.scrollTo(0, 0); return; }
    const box = el.closest(".mbp-list") || null;
    // Filas que se desplazan de lado (carruseles): acomoda la fila, no la página
    let p = el.parentElement;
    while (p && p !== document.body) {
      const cs = getComputedStyle(p);
      if (/(auto|scroll)/.test(cs.overflowX) && p.scrollWidth > p.clientWidth + 2) {
        const pr = p.getBoundingClientRect(), r = el.getBoundingClientRect();
        if (r.left < pr.left + 20) p.scrollLeft -= (pr.left + 20 - r.left);
        else if (r.right > pr.right - 20) p.scrollLeft += (r.right - pr.right + 20);
        break;
      }
      p = p.parentElement;
    }
    if (box || el.closest(".mbp")) return;
    const r = el.getBoundingClientRect(), H = window.innerHeight;
    const hdr = document.querySelector("header"), top = 70;
    if (r.top < top || r.bottom > H - 30) {
      // Si quedó trabado el bloqueo del reproductor (html.mbp-lock) con el reproductor cerrado, se quita
      if (root.classList.contains("mbp-lock") && !document.querySelector(".mbp:not([hidden])")) root.classList.remove("mbp-lock");
      const d = r.top - Math.max(top, (H - r.height) / 2);
      // El contenedor que de verdad se desplaza (la página o una caja con barra propia)
      let sc = el.parentElement;
      while (sc && sc !== document.body && sc !== root) { const o = getComputedStyle(sc).overflowY; if (/(auto|scroll)/.test(o) && sc.scrollHeight > sc.clientHeight + 2) break; sc = sc.parentElement; }
      if (!sc || sc === document.body || sc === root) sc = document.scrollingElement || root;
      sc.scrollTop = Math.max(0, sc.scrollTop + d);
      if (sc === (document.scrollingElement || root) && Math.abs(window.scrollY - sc.scrollTop) > 2) window.scrollTo(0, sc.scrollTop);
    }
    if (document.documentElement.scrollLeft) document.documentElement.scrollLeft = 0;
  };

  const center = r => ({ x: r.left + r.width / 2, y: r.top + r.height / 2 });
  function move(dir) {
    const list = items();
    if (!list.length) return;
    if (!cur || !document.contains(cur) || !list.includes(cur)) { mark(first()); return; }
    const a = cur.getBoundingClientRect(), ca = center(a);
    let best = null, bestScore = Infinity;
    for (const el of list) {
      if (el === cur || cur.contains(el) || el.contains(cur)) continue;
      const b = el.getBoundingClientRect(), cb = center(b);
      const dx = cb.x - ca.x, dy = cb.y - ca.y;
      let main, side;
      if (dir === "ArrowRight") { if (b.left < a.right - 4 && dx <= 4) continue; main = dx; side = Math.abs(dy); }
      else if (dir === "ArrowLeft") { if (b.right > a.left + 4 && dx >= -4) continue; main = -dx; side = Math.abs(dy); }
      else if (dir === "ArrowDown") { if (b.top < a.bottom - 4 && dy <= 4) continue; main = dy; side = Math.abs(dx); }
      else { if (b.bottom > a.top + 4 && dy >= -4) continue; main = -dy; side = Math.abs(dx); }
      if (main <= 0) continue;
      const score = main + side * 2.2;
      if (score < bestScore) { bestScore = score; best = el; }
    }
    if (best) mark(best);
  }

  // Reproductor a pantalla completa: OK pausa/sigue, ← → retrocede/adelanta 10 s, ↓ muestra "Sigue viendo", Atrás cierra
  let hintT = 0;
  const hint = txt => {
    let h = document.querySelector(".tvhint");
    if (!h) { h = document.createElement("div"); h.className = "tvhint"; }
    (document.querySelector(".mbp:not([hidden])") || document.body).appendChild(h);
    h.textContent = txt; h.classList.remove("off"); clearTimeout(hintT); hintT = setTimeout(() => h.classList.add("off"), 3500);
  };
  const player = () => document.querySelector(".mbp:not([hidden])");
  let wasOpen = false;
  setInterval(() => {
    const pl = player();
    if (pl && !wasOpen) { hint("OK: pausa · ← → : 10 segundos · ↓ : más capítulos · Atrás: salir"); try { if (document.activeElement && document.activeElement.tagName === "IFRAME") document.activeElement.blur(); } catch (e) {} }
    if (!pl && wasOpen) { const h = document.querySelector(".tvhint"); if (h) h.classList.add("off"); }
    wasOpen = !!pl;
    // Si el video toma el foco, se lo devolvemos a la página para que el control remoto siga funcionando
    if (pl && document.activeElement && document.activeElement.tagName === "IFRAME") { try { window.focus(); document.activeElement.blur(); } catch (e) {} }
  }, 300);
  // Botón Atrás del control: retrocede un paso dentro de la app (show → lista → Inicio) y solo sale desde Inicio
  let volviendo = false;
  // Pila de "dónde estaba": pantalla, desplazamiento y el elemento marcado, para volver exactamente ahí con Atrás
  const pila = [];
  const huella = el => {
    if (!el) return null;
    for (const a of ["data-comic", "data-show", "data-tab-go", "data-tab", "data-sub"]) {
      if (el.hasAttribute(a)) { const v = el.getAttribute(a); const todos = [...document.querySelectorAll(`[${a}="${CSS.escape(v)}"]`)]; return { a, v, i: Math.max(0, todos.indexOf(el)) }; }
    }
    if (el.matches("a[href]")) { const v = el.getAttribute("href"); const todos = [...document.querySelectorAll("a[href]")].filter(x => x.getAttribute("href") === v); return { a: "href", v, i: Math.max(0, todos.indexOf(el)) }; }
    return null;
  };
  const buscar = h => {
    if (!h) return null;
    const todos = h.a === "href" ? [...document.querySelectorAll("a[href]")].filter(x => x.getAttribute("href") === h.v) : [...document.querySelectorAll(`[${h.a}="${CSS.escape(h.v)}"]`)];
    return todos[h.i] || todos[0] || null;
  };
  const foto = el => {
    let st = null;
    try { st = { tab, openShow, openComic, sub, sort }; } catch (x) {}
    return { st, y: window.scrollY, h: huella(el) };
  };
  const paso = el => { if (!volviendo) { pila.push(foto(el || cur)); try { history.pushState({ tv: 1 }, ""); } catch (x) {} } };
  document.addEventListener("click", e => {
    const t = e.target.closest && e.target.closest('[data-show], [data-comic], [data-tab-go], nav.tabs button');
    if (!t) return;
    if (t.matches("nav.tabs button") && t.getAttribute("aria-selected") === "true") return;
    paso(t);
  }, true);
  document.addEventListener("input", e => { if (e.target && e.target.id === "q" && e.target.value.trim().length === 1 && !e.target.dataset.tvPaso) { e.target.dataset.tvPaso = "1"; paso(); } }, true);
  window.addEventListener("popstate", () => {
    if (document.querySelector(".mbp:not([hidden])")) return; // el reproductor maneja su propio Atrás
    const antes = pila.pop();
    volviendo = true;
    try {
      const q = document.getElementById("q");
      if (q && (q.value.trim() || q.dataset.tvPaso)) {
        const habia = q.value.trim(); q.value = ""; delete q.dataset.tvPaso; try { q.blur(); } catch (x) {}
        if (habia) q.dispatchEvent(new Event("input", { bubbles: true }));
      } else if (antes && antes.st) {
        // Vuelve a la misma pantalla de antes (pestaña, show o humorista abierto, sección y orden)
        try {
          tab = antes.st.tab; openShow = antes.st.openShow; openComic = antes.st.openComic; sub = antes.st.sub; sort = antes.st.sort;
          document.querySelectorAll("nav.tabs button").forEach(x => x.setAttribute("aria-selected", x.dataset.tab === tab));
          render();
        } catch (x) {
          const atras = document.querySelector("#view [data-back]"), ini = document.querySelector('nav.tabs [data-tab="inicio"]');
          if (atras) atras.click(); else if (ini) ini.click();
        }
      } else {
        const atras = document.querySelector("#view [data-back]");
        const ini = document.querySelector('nav.tabs [data-tab="inicio"]');
        if (atras) atras.click();
        else if (ini && ini.getAttribute("aria-selected") !== "true") ini.click();
      }
    } finally { volviendo = false; }
    // Mismo lugar de la página y el mismo elemento marcado
    const y = antes ? antes.y : 0;
    (document.scrollingElement || root).scrollTop = y; window.scrollTo(0, y);
    setTimeout(() => {
      (document.scrollingElement || root).scrollTop = y; window.scrollTo(0, y);
      const el = antes && buscar(antes.h);
      mark(el && visible(el) ? el : first());
    }, 120);
  });


  // En el televisor el capítulo se abre en la app de YouTube del TV (pantalla completa, control normal, la vista cuenta en el canal).
  // El reproductor de la página parpadeaba en algunos TV (TCL, 17-nov-2026). Si el TV no tiene la app de YouTube, se usa el de la página.
  const RXV = /^https?:\/\/(?:www\.|m\.)?(?:youtu\.be\/([\w-]{11})|youtube\.com\/(?:watch\?(?:[^#]*&)?v=([\w-]{11})|shorts\/([\w-]{11})|live\/([\w-]{11})))/;
  const vid = href => { const m = RXV.exec(href || ""); return m ? (m[1] || m[2] || m[3] || m[4]) : null; };
  const enApp = /MBMTV/.test(navigator.userAgent);
  document.addEventListener("click", e => {
    if (!enApp) return;
    const a = e.target.closest && e.target.closest("a[href]");
    const it = e.target.closest && e.target.closest("[data-mbp-id]");
    const id = it ? it.dataset.mbpId : a ? vid(a.href) : null;
    if (!id) return;
    // App nueva (con pantalla completa de verdad, lleva "MBMTVFS"): se ve dentro de la app, a pantalla completa
    if (/MBMTVFS/.test(navigator.userAgent) && window.MBP) {
      if (it) return; // dentro del reproductor ("Sigue viendo") lo maneja el reproductor
      e.preventDefault(); e.stopImmediatePropagation();
      window.MBP.open(id);
      const pl = document.querySelector(".mbp");
      try { const rq = pl.requestFullscreen || pl.webkitRequestFullscreen; const r = rq && rq.call(pl); if (r && r.catch) r.catch(() => {}); } catch (x) {}
      return;
    }
    e.preventDefault(); e.stopImmediatePropagation();
    try { window.MBP && window.MBP.close(); } catch (x) {}
    location.href = "https://youtu.be/" + id; // youtu.be no está en allowNavigation: Android lo manda a la app de YouTube con el video
    // Sin respaldo automático: el reproductor de la página le quitaba el sonido a YouTube y la app de YouTube se cerraba a los 2 s (17-nov-2026)
  }, true);

  // El video nunca se queda con el foco (si lo toma, el control remoto deja de llegar a la página)
  window.addEventListener("blur", () => { if (player()) setTimeout(() => { try { const f = document.querySelector(".mbp-vid iframe"); if (f) f.setAttribute("tabindex", "-1"); if (document.activeElement) document.activeElement.blur(); window.focus(); } catch (e) {} }, 0); });
  document.addEventListener("click", e => { const pl = player(); if (pl && e.target.closest("[data-mbp-id]")) { pl.classList.remove("tvlist"); mark(null); } }, true);

  document.addEventListener("keydown", e => {
    const k = e.key;
    // Entrar al cuadro de búsqueda (OK) cuenta como un paso: Atrás sale del cuadro, no de la app
    if (k === "Enter" && cur && cur.id === "q") {
      if (!cur.dataset.tvPaso) { cur.dataset.tvPaso = "1"; paso(); }
      // En el TV el teclado no sale solo: se pide a la app (y, por si acaso, con un toque simulado)
      const q = cur;
      if (!q.value.trim()) { e.preventDefault(); try { q.blur(); } catch (x) {} setTimeout(() => { try { q.focus(); q.click(); } catch (x) {} try { window.MBMNative && window.MBMNative.teclado(); } catch (x) {} }, 30); return; }
    }
    const pl = player();
    if (pl && !pl.classList.contains("tvlist")) {
      const y = window.MBP && window.MBP.yt;
      const extra = pl.querySelector(".mbp-fail:not([hidden]), .mbp-snd:not([hidden])");
      if (k === "Enter" || k === " " || k === "MediaPlayPause") {
        e.preventDefault();
        if (extra) { extra.click(); return; }
        try { if (y.getPlayerState() === 1) { y.pauseVideo(); hint("⏸ Pausa"); } else { y.playVideo(); hint("▶"); } } catch (x) {}
        return;
      }
      if (k === "ArrowRight" || k === "ArrowLeft" || k === "MediaFastForward" || k === "MediaRewind") {
        e.preventDefault();
        const d = (k === "ArrowRight" || k === "MediaFastForward") ? 10 : -10;
        try { y.seekTo(Math.max(0, y.getCurrentTime() + d), true); hint(d > 0 ? "+10 s ⏩" : "⏪ −10 s"); } catch (x) {}
        return;
      }
      if (k === "ArrowDown" || k === "ArrowUp") {
        e.preventDefault();
        const first = pl.querySelector(".mbp-it");
        if (first) { pl.classList.add("tvlist"); setTimeout(() => mark(first), 30); }
        return;
      }
      return;
    }
    if (pl && pl.classList.contains("tvlist") && k === "ArrowUp") { e.preventDefault(); pl.classList.remove("tvlist"); mark(null); return; }
    if (cur && cur.tagName === "INPUT" && (k === "ArrowLeft" || k === "ArrowRight")) return; // mover el cursor del texto
    if (k === "ArrowUp" || k === "ArrowDown" || k === "ArrowLeft" || k === "ArrowRight") {
      e.preventDefault(); move(k); return;
    }
    if ((k === "Enter" || k === " ") && cur && document.contains(cur) && !/^(A|BUTTON|INPUT|TEXTAREA|SELECT)$/.test(cur.tagName)) {
      e.preventDefault(); cur.click();
    }
  }, true);

  // Cuando la pantalla cambia (pestaña, show, reproductor), el foco vuelve a algo visible
  const first = () => { const l = items(); return l.find(el => !el.closest("nav.tabs, header, [data-mbp-close]")) || l[0] || null; };
  const fix = () => { if (!cur || !document.contains(cur) || !visible(cur) || !items().includes(cur)) mark(first()); };
  new MutationObserver(() => { clearTimeout(fix.t); fix.t = setTimeout(fix, 150); }).observe(root, { childList: true, subtree: true, attributes: true, attributeFilter: ["hidden"] });
  window.addEventListener("load", () => setTimeout(fix, 300));
})();
