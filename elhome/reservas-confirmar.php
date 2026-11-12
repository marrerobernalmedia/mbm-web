<?php
// Página del enlace que llega por WhatsApp: la persona confirma que va (o cancela). La incluye reservas.php con ?c=TOKEN.
// Confirmar exige tocar el botón (POST): la vista previa que hace WhatsApp del enlace no confirma nada.
if (basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) { http_response_code(404); exit; }
header('Content-Type: text/html; charset=utf-8');
header('X-Robots-Tag: noindex');
$h = fn($s) => htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8');
$tok = preg_replace('/[^a-f0-9]/', '', $_POST['c'] ?? $_GET['c'] ?? '');
$resp = $_POST['r'] ?? '';
$hecho = '';
if (strlen($tok) >= 12 && ($_SERVER['REQUEST_METHOD'] ?? '') === 'POST' && in_array($resp, ['si', 'no'], true) && limite('confirmar', 30, 3600)) {
  con_reservas(function (&$db) use ($tok, $resp, &$hecho) {
    foreach ($db['reservas'] as &$r) if (($r['tok'] ?? '') === $tok) {
      if ($r['estado'] === 'cancelada') return;
      if ($resp === 'si') { $r['reconf'] = date('c'); $r['reconf_via'] = 'enlace'; $hecho = 'si'; }
      else { $r['estado'] = 'cancelada'; $r['motivo'] = 'no-va'; promover($db, $r['grabacion']); $hecho = 'no'; }
      $r['actualizada'] = date('c'); return;
    }
  });
}
$r = null;
if (strlen($tok) >= 12) foreach (leer_reservas()['reservas'] as $x) if (($x['tok'] ?? '') === $tok) $r = $x;
$g = $r ? (grabaciones()[$r['grabacion']] ?? null) : null;
?><!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex"><title>Confirma tu asistencia — El Home de la Risa</title><link rel="icon" href="icons/icon-192.png">
<meta property="og:title" content="Confirma tu asistencia a la grabación"><meta property="og:description" content="El Home de la Risa · toca para confirmar tus entradas"><meta property="og:image" content="<?= $h(base_url()) ?>og.jpg">
<style>:root{--bg:#0c0a0d;--card:#1c181f;--line:#2f2834;--fg:#f7f2ea;--mute:#a99fa8;--lime:#8fd11f;--red:#e2262f;--bulb:#ffd36b;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.w{max-width:520px;margin:0 auto;padding:20px max(16px,env(safe-area-inset-left)) 60px}
.top{display:flex;gap:10px;align-items:center;margin-bottom:14px}.top img{width:40px;height:40px;border-radius:10px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px}
h1{font-size:24px;line-height:1.2;margin:0 0 10px;text-wrap:balance}p{margin:8px 0}.mute{color:var(--mute)}
.dato{background:#120f14;border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:14px 0}.dato b{font-size:18px}
button{font:inherit;width:100%;border:0;border-radius:12px;padding:16px;font-weight:800;font-size:18px;cursor:pointer;background:var(--lime);color:#111;margin-top:10px}
button.no{background:transparent;color:var(--mute);border:1px solid var(--line);font-size:15px;font-weight:600;padding:12px}
.ok{color:var(--lime)}.bad{color:#ff8a8a}.warn{color:var(--bulb)}a{color:var(--lime)}</style></head><body><div class="w">
<div class="top"><img src="icons/icon-192.png" alt=""><b>El Home de la Risa</b></div>
<div class="card">
<?php if (!$r || !$g): ?>
  <h1>No encontramos esa reserva</h1><p class="mute">El enlace no es válido o la grabación ya pasó. Abre la app de El Home de la Risa para ver tus entradas.</p>
<?php else:
  $n = (int)$r['cantidad'];
  $datos = '<div class="dato"><b>' . $h($g['titulo']) . '</b><br>' . $h(ucfirst(fecha_larga($g['fecha']))) . (!empty($g['hora']) ? ' · turno de las ' . $h($g['hora']) : '')
         . (!empty($g['lugar']) ? '<br>📍 ' . $h($g['lugar']) : '') . '<br>' . $h($r['nombre']) . ' · ' . $n . ($n === 1 ? ' entrada' : ' entradas') . '</div>'; ?>
  <?php if ($r['estado'] === 'cancelada' && $hecho === 'no'): ?>
    <h1>Reserva cancelada</h1><p>Gracias por avisar: tus entradas pasan a otra persona.</p><?= $datos ?>
    <p class="mute">Si cambias de idea y todavía quedan entradas, puedes reservar de nuevo en la app.</p>
  <?php elseif ($r['estado'] === 'cancelada'): ?>
    <h1 class="bad">Esta reserva está cancelada</h1>
    <p><?= ($r['motivo'] ?? '') === 'sin-confirmar' ? 'No se confirmó dentro de las ' . HORAS_CONFIRMAR . ' horas y las entradas pasaron a otra persona.' : 'La reserva se canceló.' ?></p><?= $datos ?>
    <p class="mute">Si todavía quedan entradas, puedes reservar de nuevo en la app de El Home de la Risa.</p>
  <?php elseif (!empty($r['reconf'])): ?>
    <h1 class="ok">✓ Asistencia confirmada</h1><p>¡Te esperamos! Tu entrada con el código para la puerta está en la app.</p><?= $datos ?>
    <?php if ($r['estado'] === 'espera'): ?><p class="warn">Sigues en la lista de espera: si se libera un lugar, tu reserva pasa sola a confirmada y lo verás en la app.</p><?php endif; ?>
    <form method="post"><input type="hidden" name="c" value="<?= $h($tok) ?>"><button class="no" name="r" value="no">Ya no puedo ir: cancelar mi reserva</button></form>
  <?php else: ?>
    <h1>¿Vienes a la grabación?</h1>
    <p>Hola, <?= $h($r['nombre']) ?>. Confirma que vas para conservar <?= $n === 1 ? 'tu entrada' : 'tus ' . $n . ' entradas' ?>.</p><?= $datos ?>
    <?php if (!empty($r['aviso'])): ?><p class="warn">Tienes hasta el <?= $h(fecha_larga(date('Y-m-d', vence($r)))) ?> a las <?= $h(date('g:i A', vence($r))) ?> (hora de Las Vegas). Si no confirmas, la reserva se cancela sola.</p><?php endif; ?>
    <form method="post"><input type="hidden" name="c" value="<?= $h($tok) ?>">
    <button name="r" value="si">Sí, voy · confirmar</button>
    <button class="no" name="r" value="no">No puedo ir: cancelar mi reserva</button></form>
  <?php endif; ?>
<?php endif; ?>
</div></div></body></html>
