#!/usr/bin/env python3
"""Genera themes/mba/ (tema WordPress de marrerobernal.com) a partir de la maqueta maquetas/mba/index.html.
Correr desde la raíz del repo cada vez que cambie la maqueta: python3 tools/build_mba_theme.py"""
import re, shutil, pathlib, json
root = pathlib.Path(__file__).resolve().parent.parent
src = (root/'maquetas/mba/index.html').read_text()
out = root/'themes/mba'; out.mkdir(parents=True, exist_ok=True)

css  = src.split('<style>')[1].split('</style>')[0]
body = src.split('<body>')[1].split('</body>')[0]
title_en = re.search(r'<title data-en="([^"]+)"', src).group(1)
desc = re.search(r'<meta name="description" content="([^"]+)"', src).group(1)

# partes del body
head_html = body.split('<section class="hero">')[0]                     # topbar + header
main_html = '<section class="hero">' + body.split('<section class="hero">')[1].split('<footer>')[0]
foot_html = '<footer>' + body.split('<footer>')[1].split('</footer>')[0] + '</footer>'
inline_js = body.split('<script>')[1].split('</script>')[0]

U = "<?php echo esc_url(get_theme_file_uri('%s')); ?>"
def fix(h):
    h = re.sub(r'src="img/([^"]+)"', lambda m: 'src="' + U % ('img/'+m.group(1)) + '"', h)
    h = re.sub(r'url\(img/([^)]+)\)', lambda m: 'url(' + U % ('img/'+m.group(1)) + ')', h)
    h = h.replace('href="#"', 'href="#contacto"').replace('href="#contacto" data-lang', 'href="#" data-lang')
    h = h.replace('<a class="logo" href="#contacto">', '<a class="logo" href="<?php echo esc_url(home_url(\'/\')); ?>">')
    return h

# formulario real → admin-post
form_old = re.search(r'<form onsubmit="[^"]*">', main_html).group(0)
main_html = main_html.replace(form_old, '<form method="post" action="<?php echo esc_url(admin_url(\'admin-post.php\')); ?>">\n      <input type="hidden" name="action" value="mba_contacto"><?php wp_nonce_field(\'mba_contacto\',\'mba_n\'); ?><input type="text" name="empresa" style="display:none" tabindex="-1" autocomplete="off">')
main_html = main_html.replace('<input placeholder="Nombre" required>', '<input name="nombre" placeholder="Nombre" required>')
main_html = main_html.replace('<input placeholder="Teléfono o WhatsApp" required>', '<input name="telefono" placeholder="Teléfono o WhatsApp" required>')
main_html = main_html.replace('<input type="email" placeholder="Correo (opcional)">', '<input type="email" name="correo" placeholder="Correo (opcional)">')
main_html = main_html.replace('<select><option>¿Qué necesitas?</option>', '<select name="servicio"><option>¿Qué necesitas?</option>')
main_html = main_html.replace('<textarea placeholder="Cuéntanos brevemente"></textarea>', '<textarea name="mensaje" placeholder="Cuéntanos brevemente"></textarea>')
main_html = main_html.replace('<small>Respondemos el mismo día hábil. Nunca compartimos tus datos.</small>',
  '<small>Respondemos el mismo día hábil. Nunca compartimos tus datos.</small>\n      <?php if (isset($_GET[\'enviado\'])): ?><div class="ok">✅ Recibido. Te contactamos el mismo día hábil.</div><?php elseif (isset($_GET[\'error\'])): ?><div class="ok" style="background:#fdecec;color:#8a1f1f">No se pudo enviar. Llámanos al 888-877-2583.</div><?php endif; ?>')

(out/'style.css').write_text('''/*
Theme Name: Marrero Bernal & Associates
Theme URI: https://marrerobernal.com
Author: Marrero Bernal Media LLC
Description: Tema propio de marrerobernal.com (agencia de seguros independiente, taxes, inmigración, notaría). Diseño aprobado por Eliam el 31-oct-2026. Se genera desde la maqueta con tools/build_mba_theme.py.
Version: 1.0.0
Requires PHP: 8.0
License: Proprietary
Text Domain: mba
*/
''' + css + '''
.ok{background:#e7f6ee;color:#135c3a;border-radius:12px;padding:12px 14px;font-weight:600}
.page-wrap{max-width:860px;margin:0 auto;padding:40px 20px 70px}.page-wrap h1{font-family:Fraunces,serif;font-size:40px;margin:0 0 20px}.page-wrap img{height:auto}
''')

(out/'header.php').write_text('''<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
''' + fix(head_html))

(out/'footer.php').write_text(fix(foot_html) + '''
<?php wp_footer(); ?>
</body>
</html>
''')

(out/'front-page.php').write_text('<?php get_header(); ?>\n' + fix(main_html) + '\n<?php get_footer(); ?>\n')
(out/'index.php').write_text('''<?php get_header(); ?>
<div class="page-wrap">
<?php if (have_posts()): while (have_posts()): the_post(); ?>
  <article><h1><?php the_title(); ?></h1><?php the_content(); ?></article>
<?php endwhile; else: ?>
  <h1>No hay nada aquí.</h1><p><a href="<?php echo esc_url(home_url('/')); ?>">Volver al inicio</a></p>
<?php endif; ?>
</div>
<?php get_footer(); ?>
''')
(out/'page.php').write_text((out/'index.php').read_text())
(out/'404.php').write_text('''<?php get_header(); ?>
<div class="page-wrap"><h1>Esta página no existe.</h1><p>Lo que buscas seguramente está en la portada: <a href="<?php echo esc_url(home_url('/')); ?>">marrerobernal.com</a>, o llámanos al <a href="tel:+18888772583">888-877-2583</a>.</p></div>
<?php get_footer(); ?>
''')

(out/'functions.php').write_text('''<?php
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
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\\n";
  if (is_front_page()) echo '<meta name="description" content="' . esc_attr(''' + json.dumps(desc, ensure_ascii=False) + ''') . '">' . "\\n";
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
  echo '<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="6a3d5751a3d7dca497eb1973"></script>' . "\\n";
}, 99);

/** Título en inglés para el conmutador de idioma. */
add_filter('document_title_parts', fn($p) => $p);
add_action('wp_head', function () { echo '<script>document.addEventListener("DOMContentLoaded",function(){var t=document.querySelector("title");if(t&&!t.getAttribute("data-en"))t.setAttribute("data-en",' . json_encode(''' + json.dumps(title_en, ensure_ascii=False) + ''') . ');});</script>' . "\\n"; }, 2);

/** SEO: idioma español, vista previa al compartir y ficha de negocio local (InsuranceAgency) para Google. */
add_filter('language_attributes', fn() => 'lang="es"');
add_action('wp_head', function () {
  if (!is_front_page()) return;
  $img = get_theme_file_uri('img/og.jpg'); $t = 'Marrero Bernal & Associates · Seguros, taxes e inmigración en Las Vegas';
  echo '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal & Associates"><meta property="og:locale" content="es_US"><meta property="og:url" content="' . esc_url(home_url('/')) . '"><meta property="og:title" content="' . esc_attr($t) . '"><meta property="og:image" content="' . esc_url($img) . '"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "\n";
  $ld = ['@context' => 'https://schema.org', '@type' => 'InsuranceAgency', '@id' => home_url('/#agencia'), 'name' => 'Marrero Bernal & Associates', 'url' => home_url('/'), 'logo' => get_theme_file_uri('img/logo.svg'), 'image' => $img,
    'telephone' => '+1-888-877-2583', 'priceRange' => '$$', 'foundingDate' => '2008', 'knowsLanguage' => ['es', 'en'],
    'address' => ['@type' => 'PostalAddress', 'streetAddress' => '3455 W Craig Rd Ste D', 'addressLocality' => 'North Las Vegas', 'addressRegion' => 'NV', 'postalCode' => '89032', 'addressCountry' => 'US'],
    'openingHoursSpecification' => [['@type' => 'OpeningHoursSpecification', 'dayOfWeek' => ['Monday','Tuesday','Wednesday','Thursday','Friday'], 'opens' => '09:00', 'closes' => '17:00']],
    'contactPoint' => [['@type' => 'ContactPoint', 'telephone' => '+1-888-877-2583', 'contactType' => 'customer service', 'availableLanguage' => ['Spanish','English']], ['@type' => 'ContactPoint', 'telephone' => '+1-702-997-2982', 'contactType' => 'sales', 'areaServed' => 'US-NV']],
    'areaServed' => [['@type' => 'State', 'name' => 'Nevada'], ['@type' => 'State', 'name' => 'California'], ['@type' => 'State', 'name' => 'Arizona']],
    'sameAs' => ['https://www.facebook.com/marreroassociates']];
  echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>' . "\n";
}, 3);

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
  $body = "Nueva solicitud desde marrerobernal.com\\n\\nNombre: $nombre\\nTeléfono/WhatsApp: $tel\\nCorreo: $correo\\nServicio: $serv\\n\\nMensaje:\\n$msg\\n\\nFecha: " . wp_date('Y-m-d H:i');
  $ok = wp_mail($to, "Cotización web: $serv — $nombre", $body, $correo ? ["Reply-To: $correo"] : []);
  wp_redirect($back . ($ok ? '?enviado=1' : '?error=1') . '#contacto'); exit;
}

/** La portada siempre es front-page.php, aunque la página tenga plantilla de Elementor guardada. */
add_filter('template_include', function ($t) {
  if (is_front_page() && !is_admin()) { $f = get_theme_file_path('front-page.php'); if (file_exists($f)) return $f; }
  return $t;
}, 999);

/** Sin emojis de WP, sin feeds de comentarios: página de una sola pieza. */
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('wp_head', 'wp_generator');
''')

(out/'buscador.js').write_text(inline_js)
shutil.copy(root/'maquetas/mba/en.js', out/'en.js')
img = out/'img'; img.mkdir(exist_ok=True)
for f in (root/'maquetas/mba/img').iterdir(): shutil.copy(f, img/f.name)
print('tema generado en', out)
