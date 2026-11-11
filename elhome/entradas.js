// Entradas gratis a las grabaciones (Eliam, 11-nov-2026): solo se reservan dentro de la app.
// Datos: grabaciones.json (fecha, lugar, cupo). Servidor: reservas.php. Puerta y lista: entradas-admin.php.
// index.html pone ENTRADAS.seccion() en el Inicio y llama ENTRADAS.pintar() después de cada render.
(() => {
  const PLAY = "https://play.google.com/store/apps/details?id=com.marrerobernalmedia.elhome";
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const ls = { get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } }, set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} } };
  // ¿Estamos dentro de la app? (app de iPhone/iPad, o la de Android de Google Play)
  try { if (/^android-app:\/\/com\.marrerobernalmedia\.elhome/.test(document.referrer)) ls.set("mbm_twa", "1"); } catch (e) {}
  const esApp = () => {
    const C = window.Capacitor; if (C && C.isNativePlatform && C.isNativePlatform()) return true;
    if (ls.get("mbm_twa") === "1") return true;
    return /Android/i.test(navigator.userAgent) && window.matchMedia("(display-mode: standalone)").matches;
  };
  const disp = (() => { let d = ls.get("mbm_disp"); if (!d) { d = Array.from(crypto.getRandomValues(new Uint8Array(12)), b => b.toString(16).padStart(2, "0")).join(""); ls.set("mbm_disp", d); } return d; })();
  const DIA = ["domingo","lunes","martes","miércoles","jueves","viernes","sábado"], MES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"];
  const larga = f => { const [y, m, d] = f.split("-").map(Number); const w = new Date(Date.UTC(y, m - 1, d, 12)).getUTCDay(); return DIA[w] + " " + d + " de " + MES[m - 1]; };
  const hoy = () => window.MBM_TODAY || new Date().toISOString().slice(0, 10);

  const css = `
.en-sec{margin-bottom:22px}
.en-vacio{color:var(--mute);padding:8px 0 30px}
.en-sec h2 small{font-weight:600}
.en-list{display:grid;gap:12px}
@media(min-width:900px){.en-list{grid-template-columns:repeat(2,1fr)}}
.en-card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.en-pic{position:relative;aspect-ratio:16/7;background:#000;overflow:hidden}
.en-pic img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.en-badge{position:absolute;left:10px;top:10px;background:var(--bulb);color:#111;font-weight:800;font-size:12px;letter-spacing:.04em;border-radius:999px;padding:5px 10px}
.en-body{padding:12px 14px 14px}
.en-body h3{margin:0 0 2px;font-size:18px;font-weight:800}
.en-body .en-sub{color:var(--mute);font-size:13.5px}
.en-when{display:flex;gap:10px;align-items:center;margin:10px 0 12px}
.en-cal{flex:none;width:52px;border-radius:10px;overflow:hidden;text-align:center;background:var(--bg2);border:1px solid var(--line)}
.en-cal small{display:block;background:var(--door);color:#fff;font-size:10.5px;font-weight:800;letter-spacing:.06em;padding:2px 0;text-transform:uppercase}
.en-cal b{display:block;font-size:22px;line-height:1.3}
.en-when div:last-child{font-size:13.5px;line-height:1.35}
.en-when em{font-style:normal;color:var(--mute)}
.en-cupo{font-size:12.5px;font-weight:700;color:var(--lime);margin-bottom:8px}
.en-elige{font-size:13px;font-weight:700;color:var(--mute);margin:2px 0 8px}
.en-turno{display:flex;gap:12px;align-items:center;border-top:1px solid var(--line);padding:12px 0 4px}
.en-hora{flex:none;width:86px;text-align:center}.en-hora b{display:block;font-size:19px;font-weight:800;white-space:nowrap}.en-hora small{color:var(--mute);font-size:11px;text-transform:uppercase;letter-spacing:.06em}
.en-tc{flex:1;min-width:0}
.en-cupo.lleno{color:var(--bulb)}
.en-go{width:100%;border:0;border-radius:12px;padding:13px;font-weight:800;font-size:15px;background:var(--lime);color:#111;cursor:pointer;font-family:inherit}
.en-go.mia{background:var(--bulb)}
#enRoot[hidden]{display:none}
.en-sheet{max-height:92vh;overflow-y:auto}
.en-f label{display:block;font-size:13px;font-weight:700;margin:10px 0 4px}
.en-f input{width:100%;padding:12px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--fg);font:inherit;font-size:16px}
.en-n{display:flex;align-items:center;gap:12px}
.en-n button{width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:var(--card);color:var(--fg);font-size:22px;font-weight:700;cursor:pointer}
.en-n b{font-size:24px;min-width:28px;text-align:center}
.en-msg{min-height:20px;font-size:13.5px;margin:8px 0;color:#ff8a8a}
.en-ticket{background:#fff;color:#111;border-radius:16px;padding:16px;text-align:center;margin:6px 0 10px}
.en-ticket .qr svg{width:210px;height:210px;display:block;margin:6px auto}
.en-ticket h4{margin:0;font-size:17px}
.en-ticket p{margin:2px 0;color:#333!important;font-size:13.5px}
.en-ticket .cod{font-size:22px;font-weight:900;letter-spacing:.18em;margin-top:4px}
.en-est{display:inline-block;font-weight:800;font-size:12px;border-radius:999px;padding:4px 10px;margin:4px 0}
.en-est.confirmada{background:#1f7a1f;color:#fff}.en-est.espera{background:#f2c14e;color:#111}
.en-link{background:none;border:0;color:var(--mute);text-decoration:underline;font:inherit;font-size:13px;cursor:pointer;padding:8px 0}
.en-store{display:flex;align-items:center;gap:10px;justify-content:center;background:#000;color:#fff;border:1px solid #444;border-radius:12px;padding:12px;font-weight:800;text-decoration:none;margin:8px 0}`;
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  let G = null, F = [], cupos = {}, mias = [], cargado = 0, cargando = null;
  const cargar = (forzar) => {
    if (cargando) return cargando;
    if (!forzar && G && Date.now() - cargado < 60000) return Promise.resolve();
    cargando = Promise.all([
      fetch("grabaciones.json", { cache: "no-cache" }).then(r => r.json()).catch(() => G || []),
      fetch("reservas.php?accion=cupos", { cache: "no-store" }).then(r => r.json()).catch(() => ({})),
      fetch("reservas.php?accion=mias&disp=" + disp, { cache: "no-store" }).then(r => r.json()).catch(() => null)
    ]).then(([g, c, m]) => {
      G = (g || []).filter(x => x.fecha >= hoy()).sort((a, b) => a.fecha.localeCompare(b.fecha));
      // Turnos (p. ej. 3 PM y 6 PM): cada turno es una función con su propio cupo e id "<grabación>-<turno>"
      G.forEach(x => { x.funciones = (x.turnos && x.turnos.length ? x.turnos : [{ id: "", hora: x.hora, cupo: x.cupo }]).map(t => Object.assign({}, x, { turnos: null, funciones: null, grupo: x.id, id: t.id ? x.id + "-" + t.id : x.id, hora: t.hora || "", cupo: t.cupo })); });
      F = G.flatMap(x => x.funciones);
      cupos = (c && c.cupos) || cupos;
      if (m && m.reservas) { mias = m.reservas; ls.set("mbm_mias", JSON.stringify(mias)); }
      else { try { mias = JSON.parse(ls.get("mbm_mias") || "[]"); } catch (e) {} }
      cargado = Date.now();
    }).finally(() => { cargando = null; });
    return cargando;
  };
  const mia = id => mias.find(r => r.grabacion === id && r.estado !== "cancelada");
  const libres = g => { const c = cupos[g.id]; return c ? Math.max(0, c.cupo - c.ocupadas) : g.cupo; };

  const lugarHtml = g => g.lugar ? `📍 ${esc(g.lugar)}${g.direccion ? `<br><em>${esc(g.direccion)}</em>` : ""}${g.mapa ? `<br><a href="${esc(g.mapa)}" target="_blank" rel="noopener" data-yt style="color:var(--lime);font-weight:700">Cómo llegar →</a>` : ""}` : "<em>El lugar te lo avisamos en la app</em>";
  function turno(f, varios) {
    const r = mia(f.id), l = libres(f), otra = !r && f.grupo !== f.id && F.some(x => x.grupo === f.grupo && x.id !== f.id && mia(x.id));
    const cupo = r ? (r.estado === "espera" ? "Estás en la lista de espera" : `Tienes ${r.cantidad} ${r.cantidad == 1 ? "entrada" : "entradas"}`) : !f.abierta ? "Reservas cerradas" : l <= 0 ? "Lleno · lista de espera" : l <= Math.max(10, f.cupo * 0.25) ? `¡Quedan solo ${l}!` : "Entradas Gratis · Cupo Limitado";
    const btn = r ? `<button class="en-go mia" data-en-ver="${esc(f.id)}">🎟️ Ver mi entrada</button>` : !f.abierta || otra ? "" : `<button class="en-go" data-en-res="${esc(f.id)}">🎟️ Reservar${varios ? "" : " gratis"}</button>`;
    return `<div class="en-turno">${f.hora ? `<div class="en-hora"><b>${esc(f.hora)}</b>${varios ? "<small>turno</small>" : ""}</div>` : ""}<div class="en-tc"><div class="en-cupo${l <= 0 && !r ? " lleno" : ""}">${cupo}</div>${btn}</div></div>`;
  }
  function tarjeta(g) {
    const [, m, d] = g.fecha.split("-").map(Number), varios = g.funciones.length > 1;
    return `<div class="en-card"><div class="en-pic"><img src="${esc(g.banner || "og.jpg")}" alt="" loading="lazy"></div>
<div class="en-body"><h3>${esc(g.titulo)}</h3><div class="en-sub">${esc(g.sub || "")}</div>
<div class="en-when"><div class="en-cal"><small>${MES[m - 1].slice(0, 3)}</small><b>${d}</b></div><div><b>${esc(larga(g.fecha).replace(/^./, c => c.toUpperCase()))}</b>${varios ? ` · ${g.funciones.length} turnos` : ""}<br>${lugarHtml(g)}</div></div>
${varios ? `<div class="en-elige">Elige tu turno:</div>` : ""}${g.funciones.map(f => turno(f, varios)).join("")}</div></div>`;
  }
  const html = () => `` + (!G ? `<p class="en-vacio">Cargando…</p>` : G.length ? `<div class="en-list">${G.map(tarjeta).join("")}</div>` : `<p class="en-vacio">Por ahora no hay grabaciones con público anunciadas. Activa los avisos 🔔 y te avisamos cuando se abran las entradas.</p>`);
  function seccion() { return `<section class="en-sec" id="entradasSec">${html()}</section>`; }
  function pintar() {
    const pon = () => { const s = document.getElementById("entradasSec"); if (s) s.innerHTML = html(); };
    pon(); cargar().then(pon);
  }

  // --- hoja (reservar / mi entrada / bajar la app)
  let root;
  function hoja(contenido) {
    if (!root) {
      root = document.createElement("div"); root.id = "enRoot"; root.hidden = true;
      root.innerHTML = `<div class="scrim" data-en-x></div><div class="sheet en-sheet" role="dialog" aria-label="Entradas"></div>`;
      document.body.appendChild(root);
      root.addEventListener("click", e => { if (e.target.closest("[data-en-x]")) cerrar(); });
    }
    root.querySelector(".en-sheet").innerHTML = contenido; root.hidden = false;
  }
  const cerrar = () => { if (root) root.hidden = true; };

  function bajarApp(g) {
    hoja(`<h3>Las entradas se reservan en la app</h3>
<p>Baja gratis la app de El Home de la Risa y reserva tus entradas para <b>${esc(g.titulo)}</b> (${esc(larga(g.fecha))}${g.hora ? ", turno de las " + esc(g.hora) : ""}). En la app también tienes tu entrada con código para la puerta y los avisos de la grabación.</p>
<a class="en-store" href="${PLAY}" target="_blank" rel="noopener">▶ Bajar en Google Play</a>
<p style="font-size:13px;text-align:center">iPhone y iPad: muy pronto en la App Store.</p>
<button class="close" data-en-x>Cerrar</button>`);
  }

  function formulario(g) {
    const max = Math.max(1, g.max || 4), l = libres(g);
    let n = Math.min(2, max);
    hoja(`<h3>Reservar entradas gratis</h3>
<p><b>${esc(g.titulo)}</b> · ${esc(g.sub || "")}<br>${esc(larga(g.fecha).replace(/^./, c => c.toUpperCase()))}${g.hora ? " · <b>turno de las " + esc(g.hora) + "</b>" : ""}${g.lugar ? "<br>📍 " + esc(g.lugar) + (g.direccion ? ", " + esc(g.direccion) : "") : ""}</p>
${l <= 0 ? `<p style="color:var(--bulb)">Ya no quedan entradas. Si te anotas, quedas en la lista de espera y te avisamos si se libera un lugar.</p>` : ""}
<form class="en-f" id="enForm">
<label for="enNom">Tu nombre</label><input id="enNom" name="nombre" autocomplete="name" maxlength="80" required value="${esc(ls.get("mbm_nom") || "")}">
<label for="enTel">Tu teléfono (WhatsApp)</label><input id="enTel" name="telefono" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="Ej. 702 555 1234 o +34 600 000 000" required value="${esc(ls.get("mbm_tel") || "")}">
<label>¿Cuántas entradas? <span style="font-weight:400;color:var(--mute)">(máximo ${max})</span></label>
<div class="en-n"><button type="button" data-en-n="-1" aria-label="Menos">−</button><b id="enN">${n}</b><button type="button" data-en-n="1" aria-label="Más">+</button></div>
<div style="position:absolute;left:-9999px" aria-hidden="true"><input name="web" tabindex="-1" autocomplete="off"></div>
<div class="en-msg" id="enMsg" role="status"></div>
<button class="en-go" id="enSend">${l <= 0 ? "Anotarme en la lista de espera" : "Reservar mis entradas"}</button>
<p style="font-size:12px;margin-top:10px">Usamos tu nombre y teléfono solo para la lista de la puerta y para avisarte de esta grabación. <a href="privacidad/" target="_blank" rel="noopener" style="color:inherit">Privacidad</a></p>
</form><button class="close" data-en-x>Cancelar</button>`);
    root.querySelectorAll("[data-en-n]").forEach(b => b.onclick = () => { n = Math.max(1, Math.min(max, n + +b.dataset.enN)); root.querySelector("#enN").textContent = n; });
    root.querySelector("#enForm").onsubmit = async e => {
      e.preventDefault();
      const f = e.target, msg = root.querySelector("#enMsg"), send = root.querySelector("#enSend");
      const fd = new FormData(f); fd.set("accion", "reservar"); fd.set("grabacion", g.id); fd.set("cantidad", n); fd.set("disp", disp);
      send.disabled = true; msg.textContent = "";
      try {
        const r = await fetch("reservas.php", { method: "POST", body: fd }).then(x => x.json());
        if (!r.ok) throw new Error(r.error || "No se pudo reservar. Prueba otra vez.");
        ls.set("mbm_nom", fd.get("nombre")); ls.set("mbm_tel", fd.get("telefono"));
        mias = mias.filter(x => x.codigo !== r.reserva.codigo).concat(r.reserva); ls.set("mbm_mias", JSON.stringify(mias));
        etiqueta(g.id, r.reserva.estado);
        await cargar(true); pintar(); entrada(g, true);
      } catch (err) { msg.textContent = err.message || "Sin conexión. Prueba otra vez."; send.disabled = false; }
    };
  }

  // Etiqueta en OneSignal para avisar solo a quienes reservaron esa grabación
  function etiqueta(id, estado) {
    try { (window.OneSignalDeferred = window.OneSignalDeferred || []).push(OS => { try { OS.User && OS.User.addTag && OS.User.addTag("grabacion_" + id.replace(/\W/g, "_"), estado); } catch (e) {} }); } catch (e) {}
  }

  let qrP = null;
  const qrLib = () => qrP || (qrP = new Promise((ok, no) => { if (window.qrcode) return ok(); const s = document.createElement("script"); s.src = "qrcode.js"; s.onload = ok; s.onerror = no; document.head.appendChild(s); }));
  function entrada(g, recien) {
    const r = mia(g.id); if (!r) { formulario(g); return; }
    const url = location.origin + location.pathname.replace(/[^/]*$/, "") + "entradas-admin.php?entrada=" + r.codigo;
    const pushOn = document.getElementById("pushLbl") && /✓/.test(document.getElementById("pushLbl").textContent);
    hoja(`<h3>${recien ? (r.estado === "espera" ? "Estás en la lista de espera" : "¡Listo! Tienes tus entradas") : "Tu entrada"}</h3>
${r.estado === "espera" ? `<p>La grabación está llena. Si alguien cancela, tu reserva pasa sola a confirmada y aquí lo vas a ver.</p>` : `<p>Muestra este código en la puerta. También lo encuentras siempre aquí, en la app.</p>`}
<div class="en-ticket"><h4>${esc(g.titulo)}</h4><p>${esc(g.sub || "")}</p><p><b>${esc(larga(g.fecha).replace(/^./, c => c.toUpperCase()))}${g.hora ? " · " + esc(g.hora) : ""}</b></p>${g.lugar ? `<p>📍 ${esc(g.lugar)}${g.direccion ? "<br>" + esc(g.direccion) : ""}</p>` : ""}${g.mapa ? `<p><a href="${esc(g.mapa)}" target="_blank" rel="noopener" data-yt style="color:#0a58ca;font-weight:700">Cómo llegar →</a></p>` : ""}
<div class="qr" id="enQr"></div><div class="en-est ${esc(r.estado)}">${r.estado === "espera" ? "LISTA DE ESPERA" : "CONFIRMADA"}</div>
<p style="font-size:16px"><b>${esc(r.nombre)}</b> · ${r.cantidad} ${r.cantidad == 1 ? "entrada" : "entradas"}</p><div class="cod">${esc(r.codigo)}</div></div>
${!pushOn && document.getElementById("pushBtn") && !document.getElementById("pushBtn").hidden ? `<button class="en-go" data-en-push>🔔 Activar avisos para recordarte la grabación</button>` : ""}
<p style="font-size:12.5px">Si cambias de planes, cancela para que otra persona pueda ir.</p>
<button class="en-link" data-en-cancel="${esc(r.codigo)}">Cancelar mi reserva</button>
<button class="close" data-en-x>Listo</button>`);
    qrLib().then(() => { const q = qrcode(0, "M"); q.addData(url); q.make(); const el = root.querySelector("#enQr"); if (el) el.innerHTML = q.createSvgTag({ cellSize: 4, margin: 2, scalable: true }); }).catch(() => {});
    const pb = root.querySelector("[data-en-push]"); if (pb) pb.onclick = () => { document.getElementById("pushBtn").click(); pb.remove(); };
    root.querySelector("[data-en-cancel]").onclick = async e => {
      if (!confirm("¿Seguro que quieres cancelar tu reserva?")) return;
      const fd = new FormData(); fd.set("accion", "cancelar"); fd.set("codigo", e.target.dataset.enCancel); fd.set("disp", disp);
      try { await fetch("reservas.php", { method: "POST", body: fd }); } catch (x) {}
      mias = mias.filter(x => x.codigo !== e.target.dataset.enCancel); ls.set("mbm_mias", JSON.stringify(mias)); etiqueta(g.id, "cancelada");
      cerrar(); await cargar(true); pintar();
    };
  }

  document.addEventListener("click", e => {
    const a = e.target.closest("[data-en-res],[data-en-ver]"); if (!a || !G) return;
    const g = F.find(x => x.id === (a.dataset.enRes || a.dataset.enVer)); if (!g) return;
    if (a.dataset.enVer) return entrada(g);
    if (!esApp()) return bajarApp(g);
    formulario(g);
  });
  // Enlace directo (avisos, WhatsApp): ...?entradas=1 abre la pestaña Entradas (lo hace index.html)
  window.ENTRADAS = { seccion, pintar, esApp };
})();
