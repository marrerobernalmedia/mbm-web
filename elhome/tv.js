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
html.tv, html.tv body{overflow-x:hidden!important;max-width:100vw}
html.tv #bellBtn, html.tv .brand span{display:none!important}
html.tv .hdrow{gap:12px;min-width:0}
html.tv .hdrow .hd{flex:0 1 auto;min-width:0;gap:12px}
html.tv .hdrow .brand{margin-right:4px}
html.tv .hdrow .brand b{font-size:20px;white-space:nowrap}
html.tv .hdrow .hd>img{width:44px;height:44px}
html.tv .hdrow nav.tabs div{gap:2px}
html.tv .hdrow nav.tabs button{padding:9px 11px;font-size:15px}
html.tv .hdrow .search{flex:1 1 200px;min-width:160px;max-width:none;margin-left:auto}
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
    // Solo desplazamiento vertical: la página nunca se corre de lado
    if (!el.closest("header, nav.tabs")) el.scrollIntoView({ block: "center", inline: "nearest", behavior: "smooth" });
    else window.scrollTo({ top: 0, behavior: "smooth" });
    if (window.scrollX) window.scrollTo(0, window.scrollY);
    document.documentElement.scrollLeft = 0; document.body.scrollLeft = 0;
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

  document.addEventListener("keydown", e => {
    const k = e.key;
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
