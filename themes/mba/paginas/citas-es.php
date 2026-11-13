<?php /* citas (es) — GENERADO por tools/build_mba_paginas.py */
ob_start(); get_header(); echo mba_pag_fix(ob_get_clean(), 'es', 'citas', 'appointments'); ?>
<main class="subpage">
<section class="sub sol"><div class="wrap" style="max-width:860px">
  <div class="kicker">Citas</div>
  <h1 style="font-family:Fraunces,serif;margin:6px 0 10px">Agenda tu cita en la oficina</h1>
  <p class="lead" style="margin:0 0 18px">Escoge el día y la hora. Atendemos citas lunes, martes, jueves y viernes de 9:00 AM a 4:00 PM, excepto feriados. Si prefieres, llámanos o escríbenos por WhatsApp al 888-877-2583.</p>
  <p style="margin:0 0 18px;padding:12px 14px;border-radius:12px;background:#fff;border:1px solid #e4dfd3"><b>Dinos para qué es la cita.</b> Al llenar tus datos, escribe en la casilla «Additional information» el motivo: taxes, seguro de auto, ITIN, traducción, notary public u otro. Así te atendemos con todo listo.</p>
  <div style="position:relative;background:#fff;border-radius:16px">
  <div id="cita-carga" style="position:absolute;left:0;right:0;top:0;padding:64px 16px;text-align:center;color:#6b6558;font-weight:600;pointer-events:none">Cargando el calendario…</div>
  <iframe src="https://api.leadconnectorhq.com/widget/booking/J9VOKpFkhYtqSUi4Lbrn" style="position:relative;width:100%;min-height:720px;border:none;overflow:hidden;background:transparent;border-radius:16px" scrolling="no" id="J9VOKpFkhYtqSUi4Lbrn_cita" title="Calendario de citas" onload="setTimeout(function(){var c=document.getElementById(&quot;cita-carga&quot;);if(c)c.remove()},1500)"></iframe>
  </div>
  <script>(function(){var n=0,t=setInterval(function(){var e=document.querySelector("chat-widget"),r=e&&e.shadowRoot;if(r&&!r.getElementById("mba-sin-saludo")){var s=document.createElement("style");s.id="mba-sin-saludo";s.textContent=".lc_text-widget--prompt{display:none!important}";r.appendChild(s)}if(++n>120||(r&&r.getElementById("mba-sin-saludo")))clearInterval(t)},250)})();</script>
  <script src="https://link.msgsndr.com/js/form_embed.js" type="text/javascript"></script>
</div></section>

</main>
<?php ob_start(); get_footer(); echo mba_pag_fix(ob_get_clean(), 'es', 'citas', 'appointments'); ?>
