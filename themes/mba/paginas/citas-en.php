<?php /* citas (en) — GENERADO por tools/build_mba_paginas.py */
ob_start(); get_header('en'); echo mba_pag_fix(ob_get_clean(), 'en', 'appointments', 'citas'); ?>
<main class="subpage">
<section class="sub sol"><div class="wrap" style="max-width:860px">
  <div class="kicker">Appointments</div>
  <h1 style="font-family:Fraunces,serif;margin:6px 0 10px">Book your appointment at the office</h1>
  <p class="lead" style="margin:0 0 18px">Pick a day and time. Appointments are Monday, Tuesday, Thursday and Friday from 9:00 AM to 4:00 PM, except holidays. If you prefer, call or WhatsApp us at 888-877-2583.</p>
  <p style="margin:0 0 18px;padding:12px 14px;border-radius:12px;background:#fff;border:1px solid #e4dfd3"><b>Tell us what the appointment is for.</b> When you enter your details, use the “Additional information” box to tell us the reason: taxes, auto insurance, ITIN, translation, notary or other. That way we have everything ready for you.</p>
  <div style="position:relative;background:#fff;border-radius:16px">
  <div id="cita-carga" style="position:absolute;left:0;right:0;top:0;padding:64px 16px;text-align:center;color:#6b6558;font-weight:600;pointer-events:none">Loading the calendar…</div>
  <iframe src="https://api.leadconnectorhq.com/widget/booking/J9VOKpFkhYtqSUi4Lbrn" style="position:relative;width:100%;min-height:720px;border:none;overflow:hidden;background:transparent;border-radius:16px" scrolling="no" id="J9VOKpFkhYtqSUi4Lbrn_cita" title="Appointment calendar" onload="setTimeout(function(){var c=document.getElementById(&quot;cita-carga&quot;);if(c)c.remove()},1500)"></iframe>
  </div>
  <script>(function(){var n=0,t=setInterval(function(){var e=document.querySelector("chat-widget"),r=e&&e.shadowRoot;if(r&&!r.getElementById("mba-sin-saludo")){var s=document.createElement("style");s.id="mba-sin-saludo";s.textContent=".lc_text-widget--prompt{display:none!important}";r.appendChild(s)}if(++n>120||(r&&r.getElementById("mba-sin-saludo")))clearInterval(t)},250)})();</script>
  <script src="https://link.msgsndr.com/js/form_embed.js" type="text/javascript"></script>
</div></section>

</main>
<?php ob_start(); get_footer('en'); echo mba_pag_fix(ob_get_clean(), 'en', 'appointments', 'citas'); ?>
