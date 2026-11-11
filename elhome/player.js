// Reproductor dentro de la app y de la web (Eliam, 11-nov-2026: "la gente se queda en la app y no sale a YouTube").
// Toca un video → se abre aquí, arranca solo y al terminar sigue con el próximo de la lista "Sigue viendo".
// Cada index.html define window.PLAYER = { info(id) → {t, sub, img}, next(id) → [ids], en: bool }.
// Mismo archivo en elhome/player.js y recta/player.js: si cambias uno, copia el otro.
(() => {
  const RX = /^https?:\/\/(?:www\.|m\.)?(?:youtu\.be\/([\w-]{11})|youtube\.com\/(?:watch\?(?:[^#]*&)?v=([\w-]{11})|shorts\/([\w-]{11})|live\/([\w-]{11})))/;
  const idOf = href => { const m = RX.exec(href || ""); return m ? (m[1] || m[2] || m[3] || m[4]) : null; };
  const P = () => window.PLAYER || {};
  const L = (es, en) => (P().en ? en : es);
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

  const css = `
.mbp{position:fixed;inset:0;z-index:9999;background:#000;color:#fff;display:flex;flex-direction:column;font-family:inherit;overscroll-behavior:contain}
.mbp[hidden]{display:none}
.mbp-top{display:flex;align-items:center;gap:8px;padding:calc(env(safe-area-inset-top,0px) + 8px) 10px 8px}
.mbp-top b{flex:1;font-size:14px;opacity:.75;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mbp-x{width:40px;height:40px;border-radius:50%;border:0;background:#222;color:#fff;font-size:22px;line-height:40px;cursor:pointer;flex:none}
.mbp-body{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch}
.mbp-wrap{max-width:960px;margin:0 auto}
.mbp-vid{position:relative;width:100%;aspect-ratio:16/9;background:#111}
.mbp-vid iframe,.mbp-vid>div{position:absolute;inset:0;width:100%;height:100%;border:0}
.mbp-fail{position:absolute;inset:0;z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;background:#111;color:#fff;text-decoration:none;font-weight:700;font-size:15px}
.mbp-fail[hidden]{display:none}
.mbp-fail span{width:64px;height:44px;border-radius:12px;background:#f00;display:flex;align-items:center;justify-content:center;font-size:20px}
.mbp-snd{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);z-index:2;border:0;border-radius:999px;padding:10px 16px;background:rgba(0,0,0,.8);color:#fff;font-weight:700;font-size:14px;cursor:pointer}
.mbp-info{padding:12px 14px 4px}
.mbp-info h3{margin:0 0 4px;font-size:17px;line-height:1.25}
.mbp-info p{margin:0;font-size:13px;opacity:.7}
.mbp-acts{display:flex;gap:8px;padding:10px 14px 4px;flex-wrap:wrap}
.mbp-acts a,.mbp-acts button{border:1px solid #333;background:#161616;color:#fff;border-radius:999px;padding:8px 14px;font-size:13px;font-weight:600;text-decoration:none;cursor:pointer;font-family:inherit}
.mbp-auto{opacity:.85}
.mbp h4{margin:16px 14px 8px;font-size:15px;text-transform:uppercase;letter-spacing:.04em;opacity:.85}
.mbp-list{padding:0 10px calc(env(safe-area-inset-bottom,0px) + 24px)}
.mbp-it{display:flex;gap:10px;align-items:flex-start;width:100%;padding:6px 4px;border:0;background:none;color:#fff;text-align:left;cursor:pointer;font-family:inherit;border-radius:8px}
.mbp-it:hover{background:#151515}
.mbp-it img{width:150px;aspect-ratio:16/9;object-fit:cover;border-radius:6px;flex:none;background:#222}
.mbp-it b{display:block;font-size:14px;line-height:1.25;font-weight:600}
.mbp-it span{display:block;font-size:12px;opacity:.65;margin-top:3px}
.mbp-it em{display:inline-block;font-style:normal;font-size:11px;font-weight:700;background:#c00;border-radius:4px;padding:1px 5px;margin-bottom:3px}
html.mbp-lock,html.mbp-lock body{overflow:hidden}
html.mbp-lock nav.tabs{z-index:10000}
@media(min-width:900px){.mbp-it img{width:180px}}`;

  let root, yt = null, cur = null, apiP = null, queue = [], autoNext = true, forcedMute = false, watch = 0, pushed = false;

  function api(){
    if (window.YT && window.YT.Player) return Promise.resolve();
    if (apiP) return apiP;
    apiP = new Promise((res, rej) => {
      const prev = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = () => { try { prev && prev(); } catch (e) {} res(); };
      const s = document.createElement("script"); s.src = "https://www.youtube.com/iframe_api"; s.async = true;
      s.onerror = () => { apiP = null; rej(); }; document.head.appendChild(s);
    });
    return apiP;
  }

  function build(){
    if (root) return;
    const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    root = document.createElement("div"); root.className = "mbp"; root.hidden = true;
    root.setAttribute("role", "dialog"); root.setAttribute("aria-modal", "true");
    root.innerHTML = `<div class="mbp-top"><button class="mbp-x" data-mbp-close aria-label="${L("Cerrar","Close")}">×</button><b></b></div>
<div class="mbp-body"><div class="mbp-wrap"><div class="mbp-vid"><div id="mbpPlayer"></div><button class="mbp-snd" hidden>🔊 ${L("Toca para activar el sonido","Tap to turn the sound on")}</button></div>
<div class="mbp-info"><h3></h3><p></p></div>
<div class="mbp-acts"><a class="mbp-yt" target="_blank" rel="noopener">▶ ${L("Ver en YouTube","Watch on YouTube")}</a><button class="mbp-auto"></button></div>
<h4>${L("Sigue viendo","Keep watching")}</h4><div class="mbp-list"></div></div></div>`;
    document.body.appendChild(root);
    root.querySelector(".mbp-top b").textContent = document.title.split(/[—|·]/)[0].trim();
    root.addEventListener("click", e => {
      if (e.target.closest("[data-mbp-close]")) { close(); return; }
      const it = e.target.closest("[data-mbp-id]"); if (it) { play(it.dataset.mbpId); root.querySelector(".mbp-body").scrollTop = 0; return; }
      if (e.target.closest(".mbp-snd")) { try { yt.unMute(); yt.setVolume(100); yt.playVideo(); } catch (x) {} forcedMute = false; e.target.closest(".mbp-snd").hidden = true; return; }
      if (e.target.closest(".mbp-auto")) { autoNext = !autoNext; autoBtn(); return; }
      if (e.target.closest(".mbp-yt")) { try { yt && yt.pauseVideo(); } catch (x) {} }
    });
    document.addEventListener("keydown", e => { if (e.key === "Escape" && !root.hidden) close(); });
  }
  const autoBtn = () => { root.querySelector(".mbp-auto").textContent = (autoNext ? "⏭ " : "⏸ ") + L("Reproducción automática: ", "Autoplay: ") + (autoNext ? L("sí","on") : L("no","off")); };

  function fill(id){
    const inf = (P().info && P().info(id)) || {};
    root.querySelector(".mbp-info h3").textContent = inf.t || "";
    root.querySelector(".mbp-info p").textContent = inf.sub || "";
    root.querySelector(".mbp-yt").href = "https://youtu.be/" + id;
    let nx = []; try { nx = (P().next && P().next(id)) || []; } catch (e) {}
    queue = nx.filter(x => x && x !== id).slice(0, 12);
    root.querySelector(".mbp-list").innerHTML = queue.map((x, i) => { const n = (P().info && P().info(x)) || {};
      return `<button class="mbp-it" data-mbp-id="${esc(x)}"><img src="${esc(n.img || "https://i.ytimg.com/vi/" + x + "/mqdefault.jpg")}" alt="" loading="lazy"><div>${i === 0 ? `<em>${L("A continuación","Up next")}</em>` : ""}<b>${esc(n.t || "")}</b><span>${esc(n.sub || "")}${n.d ? " · " + esc(n.d) : ""}</span></div></button>`; }).join("");
    autoBtn();
  }

  function onState(e){
    const s = e.data;
    if (s === 1) { clearTimeout(watch); root.querySelector(".mbp-snd").hidden = !(forcedMute && yt.isMuted && yt.isMuted()); }
    if (s === 0 && autoNext && queue[0]) play(queue[0]);
  }
  // Si el navegador no deja arrancar con sonido (iPhone sobre todo), arranca en silencio con el botón "activar el sonido"
  function guard(){
    clearTimeout(watch);
    watch = setTimeout(() => { try { const s = yt.getPlayerState(); if (s !== 1 && s !== 3 && s !== 0) { forcedMute = true; yt.mute(); yt.playVideo(); } } catch (e) {} }, 2200);
  }

  // Si YouTube no deja verlo aquí, un botón grande para abrirlo en YouTube (un toque: así el navegador no lo bloquea)
  function fail(){
    clearTimeout(watch);
    const v = root.querySelector(".mbp-vid"); let f = v.querySelector(".mbp-fail");
    if (!f) { f = document.createElement("a"); f.className = "mbp-fail"; f.target = "_blank"; f.rel = "noopener"; f.setAttribute("data-yt", ""); v.appendChild(f); }
    f.href = "https://youtu.be/" + cur; f.innerHTML = "<span>▶</span>" + L("Ver este video en YouTube", "Watch this video on YouTube"); f.hidden = false;
  }
  function play(id){
    cur = id; fill(id);
    const f = root.querySelector(".mbp-fail"); if (f) f.hidden = true;
    forcedMute = false; root.querySelector(".mbp-snd").hidden = true;
    if (yt && yt.loadVideoById) { try { yt.loadVideoById(id); guard(); return; } catch (e) {} }
    api().then(() => {
      if (yt && yt.loadVideoById) { yt.loadVideoById(cur); guard(); return; }
      yt = new YT.Player("mbpPlayer", { videoId: cur, host: "https://www.youtube.com",
        playerVars: { autoplay: 1, playsinline: 1, rel: 0, modestbranding: 1, origin: location.origin },
        events: { onReady: e => { try { e.target.playVideo(); } catch (x) {} guard(); }, onStateChange: onState,
          onError: ev => { window.MBP.err = ev.data; fail(); } } });
    }).catch(fail);
  }

  function open(id){
    build();
    root.hidden = false; document.documentElement.classList.add("mbp-lock");
    // En el teléfono el menú de abajo sigue a la vista con el reproductor abierto (Eliam, 11-nov-2026)
    { const nav = document.querySelector("nav.tabs"); root.style.bottom = nav && getComputedStyle(nav).position === "fixed" ? nav.offsetHeight + "px" : ""; }
    if (!pushed) { try { history.pushState({ mbp: 1 }, ""); pushed = true; } catch (e) {} }
    play(id);
  }
  function close(fromPop){
    if (!root || root.hidden) return;
    clearTimeout(watch); try { yt && yt.stopVideo(); } catch (e) {}
    root.hidden = true; document.documentElement.classList.remove("mbp-lock");
    if (pushed) { pushed = false; if (!fromPop) { try { history.back(); } catch (e) {} } }
  }
  // Tocar una pestaña del menú con el reproductor abierto: se cierra y la app va a esa pestaña
  document.addEventListener("click", e => { if (root && !root.hidden && e.target.closest("nav.tabs button")) close(); }, true);
  // Botón "atrás" del teléfono / de la app: cierra el reproductor en vez de salir
  window.addEventListener("popstate", () => { if (root && !root.hidden) close(true); });

  // Cualquier enlace a un video de YouTube se abre aquí (canales, listas y "suscribirme" siguen yendo a YouTube)
  document.addEventListener("click", e => {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const a = e.target.closest && e.target.closest("a[href]"); if (!a || a.hasAttribute("data-yt") || (root && root.contains(a))) return;
    const id = idOf(a.href); if (!id) return;
    e.preventDefault(); open(id);
  }, true);

  // Precarga discreta de la API para que el toque arranque el video al instante
  const pre = () => api().catch(() => {});
  if ("requestIdleCallback" in window) requestIdleCallback(pre, { timeout: 4000 }); else setTimeout(pre, 2500);

  window.MBP = { open, close, idOf };
})();
