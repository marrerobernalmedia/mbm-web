<?php
/**
 * Marrero Bernal & Associates — tema propio (Marrero Bernal Media LLC).
 * GENERADO por tools/build_mba_theme.py desde maquetas/mba/index.html: no editar a mano, editar la maqueta.
 */
if (!defined('ABSPATH')) exit;
define('MBA_VER', '1.0.0');

add_action('after_setup_theme', function () {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
  add_theme_support('html5', ['search-form','gallery','caption','script','style']);
});

add_filter('pre_get_document_title', function ($t) {
  return is_front_page() ? 'Marrero Bernal & Associates · Seguros, taxes e inmigración en Las Vegas' : $t;
});

add_action('wp_head', function () {
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
  if (is_front_page()) echo '<meta name="description" content="' . esc_attr("Marrero Bernal & Associates: agencia de seguros independiente en Las Vegas con contratos con múltiples compañías de primer nivel como Farmers y Progressive. Seguros de auto, hogar, vida, negocio y Medicare; taxes personales y de negocio, inmigración, notaría, traducciones y creación de LLC. En español, en North Las Vegas desde 2008.") . '">' . "\n";
}, 1);

add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('mba-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap', [], null);
  wp_enqueue_style('mba', get_stylesheet_uri(), ['mba-fonts'], MBA_VER);
  wp_enqueue_script('mba-seguidores', 'https://marrerobernalmedia.com/seguidores.js', [], null, true);
  wp_enqueue_script('mba-en', get_theme_file_uri('en.js'), [], MBA_VER, true);
  wp_enqueue_script('mba-idioma', 'https://marrerobernalmedia.com/idioma.js', ['mba-en'], null, true);
  if (is_front_page()) wp_enqueue_script('mba-buscador', get_theme_file_uri('buscador.js'), [], MBA_VER, true);
});

/** Chat del CRM (LeadConnector), igual que el sitio anterior. */
add_action('wp_footer', function () {
  echo '<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="6a3d5751a3d7dca497eb1973"></script>' . "\n";
}, 99);

/** Título en inglés para el conmutador de idioma. */
add_filter('document_title_parts', fn($p) => $p);
add_action('wp_head', function () { echo '<script>document.addEventListener("DOMContentLoaded",function(){var t=document.querySelector("title");if(t&&!t.getAttribute("data-en"))t.setAttribute("data-en",' . json_encode("Marrero Bernal & Associates · Insurance, taxes and immigration in Las Vegas") . ');});</script>' . "\n"; }, 2);

/** Formulario de contacto → correo. */
add_action('admin_post_nopriv_mba_contacto', 'mba_contacto');
add_action('admin_post_mba_contacto', 'mba_contacto');
function mba_contacto() {
  $back = home_url('/');
  if (!isset($_POST['mba_n']) || !wp_verify_nonce($_POST['mba_n'], 'mba_contacto') || !empty($_POST['empresa'])) { wp_redirect($back . '?error=1#contacto'); exit; }
  $f = fn($k) => sanitize_text_field(wp_unslash($_POST[$k] ?? ''));
  $nombre = $f('nombre'); $tel = $f('telefono'); $correo = sanitize_email($_POST['correo'] ?? ''); $serv = $f('servicio'); $msg = sanitize_textarea_field(wp_unslash($_POST['mensaje'] ?? ''));
  if (!$nombre || !$tel) { wp_redirect($back . '?error=1#contacto'); exit; }
  $to = get_option('mba_contacto_email', get_option('admin_email'));
  $body = "Nueva solicitud desde marrerobernal.com\n\nNombre: $nombre\nTeléfono/WhatsApp: $tel\nCorreo: $correo\nServicio: $serv\n\nMensaje:\n$msg\n\nFecha: " . wp_date('Y-m-d H:i');
  $ok = wp_mail($to, "Cotización web: $serv — $nombre", $body, $correo ? ["Reply-To: $correo"] : []);
  wp_redirect($back . ($ok ? '?enviado=1' : '?error=1') . '#contacto'); exit;
}

/** Sin emojis de WP, sin feeds de comentarios: página de una sola pieza. */
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('wp_head', 'wp_generator');
