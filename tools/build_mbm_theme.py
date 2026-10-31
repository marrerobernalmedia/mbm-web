#!/usr/bin/env python3
"""Genera themes/mbm/ (tema WordPress de marrerobernalmedia.com) a partir de maquetas/mbm/index.html.
Correr desde la raíz del repo cada vez que cambie la maqueta: python3 tools/build_mbm_theme.py"""
import re, shutil, pathlib, json, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import i18n_en
root = pathlib.Path(__file__).resolve().parent.parent
src = (root/'maquetas/mbm/index.html').read_text()
out = root/'themes/mbm'; out.mkdir(parents=True, exist_ok=True)

css  = src.split('<style>')[1].split('</style>')[0]
body = src.split('<body>')[1].split('</body>')[0]
title_en = re.search(r'<title data-en="([^"]+)"', src).group(1)
title_es = re.search(r'<title[^>]*>(.*?)</title>', src).group(1)
desc = re.search(r'<meta name="description" content="([^"]+)"', src).group(1)

head_html = body.split('<section class="hero">')[0]
main_html = '<section class="hero">' + body.split('<section class="hero">')[1].split('<footer>')[0]
foot_html = '<footer>' + body.split('<footer>')[1].split('</footer>')[0] + '</footer>'

U = "<?php echo esc_url(get_theme_file_uri('%s')); ?>"
def fix(h):
    h = re.sub(r'src="img/([^"]+)"', lambda m: 'src="' + U % ('img/'+m.group(1)) + '"', h)
    h = re.sub(r'url\(img/([^)]+)\)', lambda m: 'url(' + U % ('img/'+m.group(1)) + ')', h)
    h = h.replace('<a href="#"><img src=', '<a href="<?php echo esc_url(home_url(\'/\')); ?>"><img src=')
    return h

form_old = re.search(r'<form onsubmit="[^"]*">', main_html).group(0)
main_html = main_html.replace(form_old, '<form method="post" action="<?php echo esc_url(admin_url(\'admin-post.php\')); ?>">\n      <input type="hidden" name="action" value="mbm_contacto"><?php wp_nonce_field(\'mbm_contacto\',\'mbm_n\'); ?><input type="text" name="sitio" style="display:none" tabindex="-1" autocomplete="off">')
main_html = main_html.replace('<input placeholder="Nombre" required>', '<input name="nombre" placeholder="Nombre" required>')
main_html = main_html.replace('<input placeholder="Empresa">', '<input name="empresa" placeholder="Empresa">')
main_html = main_html.replace('<input type="email" placeholder="Correo" required>', '<input type="email" name="correo" placeholder="Correo" required>')
main_html = main_html.replace('<input placeholder="Teléfono o WhatsApp">', '<input name="telefono" placeholder="Teléfono o WhatsApp">')
main_html = main_html.replace('<select><option>¿Qué necesitas?</option>', '<select name="servicio"><option>¿Qué necesitas?</option>')
main_html = main_html.replace('<textarea placeholder="Cuéntanos brevemente el proyecto"></textarea>', '<textarea name="mensaje" placeholder="Cuéntanos brevemente el proyecto"></textarea>')
main_html = main_html.replace('<button class="btn btn-acc" type="submit" style="justify-self:start">Enviar</button>',
  '<button class="btn btn-acc" type="submit" style="justify-self:start">Enviar</button>\n      <?php if (isset($_GET[\'enviado\'])): ?><div class="ok">✅ Recibido. Respondemos en menos de un día hábil.</div><?php elseif (isset($_GET[\'error\'])): ?><div class="ok" style="background:#3a1a1a;color:#ffb4b4">No se pudo enviar. Escríbenos a info@marrerobernalmedia.com.</div><?php endif; ?>')

(out/'style.css').write_text('''/*
Theme Name: Marrero Bernal Media
Theme URI: https://marrerobernalmedia.com
Author: Marrero Bernal Media LLC
Description: Tema propio de marrerobernalmedia.com (productora audiovisual con experiencia en el mercado latino). Diseño aprobado por Eliam el 31-oct-2026. Se genera desde la maqueta con tools/build_mbm_theme.py.
Version: 1.0.0
Requires PHP: 8.0
License: Proprietary
Text Domain: mbm
*/
''' + css + '''
.ok{background:#12302a;color:#9fe3c3;border-radius:12px;padding:12px 14px;font-weight:600}
.page-wrap{max-width:860px;margin:0 auto;padding:40px 20px 70px}.page-wrap h1{font-size:40px;margin:0 0 20px}.page-wrap img{height:auto}.page-wrap a{color:var(--acc)}
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
(out/'footer.php').write_text(fix(foot_html) + '\n<?php wp_footer(); ?>\n</body>\n</html>\n')
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
(out/'single.php').write_text((out/'index.php').read_text())
(out/'404.php').write_text('''<?php get_header(); ?>
<div class="page-wrap"><h1>Esta página no existe.</h1><p>Vuelve a la portada: <a href="<?php echo esc_url(home_url('/')); ?>">marrerobernalmedia.com</a>.</p></div>
<?php get_footer(); ?>
''')

(out/'functions.php').write_text('''<?php
/**
 * Marrero Bernal Media — tema propio (Marrero Bernal Media LLC).
 * GENERADO por tools/build_mbm_theme.py desde maquetas/mbm/index.html: no editar a mano, editar la maqueta.
 */
if (!defined('ABSPATH')) exit;
define('MBM_VER', '1.0.0');

add_action('after_setup_theme', function () {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
  add_theme_support('html5', ['search-form','gallery','caption','script','style']);
});

add_filter('pre_get_document_title', fn($t) => is_front_page() ? ''' + json.dumps(title_es, ensure_ascii=False) + ''' : $t);

add_action('wp_head', function () {
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\\n";
  if (is_front_page()) echo '<meta name="description" content="' . esc_attr(''' + json.dumps(desc, ensure_ascii=False) + ''') . '">' . "\\n";
  echo '<script>document.addEventListener("DOMContentLoaded",function(){var t=document.querySelector("title");if(t&&!t.getAttribute("data-en"))t.setAttribute("data-en",' . json_encode(''' + json.dumps(title_en, ensure_ascii=False) + ''') . ');});</script>' . "\\n";
}, 1);

add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('mbm-fonts', 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap', [], null);
  wp_enqueue_style('mbm', get_stylesheet_uri(), ['mbm-fonts'], @filemtime(get_stylesheet_directory() . '/style.css') ?: MBM_VER);
  wp_enqueue_script('mbm-seguidores', home_url('/seguidores.js'), [], @filemtime(ABSPATH . 'seguidores.js') ?: wp_date('YmdH'), true);
  wp_enqueue_script('mbm-en', get_theme_file_uri('en.js'), [], @filemtime(get_theme_file_path('en.js')) ?: MBM_VER, true);
  wp_enqueue_script('mbm-idioma', home_url('/idioma.js'), ['mbm-en'], @filemtime(ABSPATH . 'idioma.js') ?: wp_date('YmdH'), true);
});

/** La portada siempre es front-page.php, aunque la página tenga plantilla de Elementor guardada. */
add_filter('template_include', function ($t) {
  if (is_front_page() && !is_admin()) { $f = get_theme_file_path('front-page.php'); if (file_exists($f)) return $f; }
  return $t;
}, 999);

/** SEO: idioma español, vista previa al compartir y ficha de organización para Google. */
add_filter('language_attributes', fn() => 'lang="es"');
add_action('wp_head', function () {
  if (!is_front_page()) return;
  $img = get_theme_file_uri('img/og.jpg');
  echo '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal Media"><meta property="og:locale" content="es_US"><meta property="og:url" content="' . esc_url(home_url('/')) . '"><meta property="og:title" content="' . esc_attr(wp_get_document_title()) . '"><meta property="og:image" content="' . esc_url($img) . '"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "\n";
  $ld = ['@context' => 'https://schema.org', '@type' => 'Organization', '@id' => home_url('/#mbm'), 'name' => 'Marrero Bernal Media LLC', 'alternateName' => 'Marrero Bernal Media', 'url' => home_url('/'), 'logo' => get_theme_file_uri('img/logo-color.svg'), 'image' => $img, 'foundingLocation' => 'Las Vegas, Nevada',
    'founder' => ['@type' => 'Person', 'name' => 'Eliam Marrero Bernal', 'sameAs' => ['https://www.imdb.com/name/nm3952887/']],
    'email' => 'info@marrerobernalmedia.com', 'telephone' => '+1-833-627-7376',
    'sameAs' => ['https://www.youtube.com/@marrerobernalmedia', 'https://www.facebook.com/marrerobernalmedia', 'https://x.com/MarreroBernalTV', 'https://www.youtube.com/@LaRisaEsCosaSeria', 'https://www.youtube.com/@RectaAlPecho', 'https://www.elhomedelarisa.com/', 'https://rectaalpecho.com/']];
  echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>' . "\n";
}, 3);

/** Formulario de contacto → correo. */
add_action('admin_post_nopriv_mbm_contacto', 'mbm_contacto');
add_action('admin_post_mbm_contacto', 'mbm_contacto');
function mbm_contacto() {
  $back = home_url('/');
  if (!isset($_POST['mbm_n']) || !wp_verify_nonce($_POST['mbm_n'], 'mbm_contacto') || !empty($_POST['sitio'])) { wp_redirect($back . '?error=1#contacto'); exit; }
  $f = fn($k) => sanitize_text_field(wp_unslash($_POST[$k] ?? ''));
  $nombre = $f('nombre'); $empresa = $f('empresa'); $tel = $f('telefono'); $correo = sanitize_email($_POST['correo'] ?? ''); $serv = $f('servicio'); $msg = sanitize_textarea_field(wp_unslash($_POST['mensaje'] ?? ''));
  if (!$nombre || !$correo) { wp_redirect($back . '?error=1#contacto'); exit; }
  $to = get_option('mbm_contacto_email', 'info@marrerobernalmedia.com');
  $body = "Nuevo proyecto desde marrerobernalmedia.com\\n\\nNombre: $nombre\\nEmpresa: $empresa\\nCorreo: $correo\\nTeléfono/WhatsApp: $tel\\nServicio: $serv\\n\\nMensaje:\\n$msg\\n\\nFecha: " . wp_date('Y-m-d H:i');
  $ok = wp_mail($to, "Proyecto web: $serv — $nombre", $body, ["Reply-To: $correo"]);
  wp_redirect($back . ($ok ? '?enviado=1' : '?error=1') . '#contacto'); exit;
}

/** El tema manda: Elementor Pro no sustituye cabecera ni pie (su cabecera vieja traía el selector de TranslatePress). */
add_filter('elementor/theme/need_override_location', '__return_false');
add_action('elementor/theme/register_locations', function ($manager) { $manager->register_all_core_location(); });
/** Sin selector flotante de TranslatePress: el idioma lo cambia el ES · EN de la cabecera. */
add_filter('trp_floating_ls_html', '__return_empty_string');
add_action('wp_enqueue_scripts', function () { wp_dequeue_script('trp-language-switcher-js-v2'); wp_dequeue_style('trp-language-switcher-v2'); }, 100);

/** La página vieja /apps/ pasa a la sección Apps de la portada. */
add_action('template_redirect', function () { if (is_page('apps')) { wp_redirect(home_url('/#apps'), 301); exit; } });

remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('wp_head', 'wp_generator');
''')

shutil.copy(root/'maquetas/mbm/en.js', out/'en.js')
img = out/'img'; img.mkdir(exist_ok=True)
for f in (root/'maquetas/mbm/img').rglob('*'):
    if f.is_file():
        d = img/f.relative_to(root/'maquetas/mbm/img'); d.parent.mkdir(parents=True, exist_ok=True); shutil.copy(f, d)

# ---------- versión en inglés (/en/) ----------
D = i18n_en.load_dict(root/'maquetas/mbm/en.js')
title_es_ = re.search(r'<title[^>]*>(.*?)</title>', src).group(1)
desc_en = D.get(desc, desc)
hp = (out/'header.php').read_text()
(out/'header.php').write_text(i18n_en.flags(hp, 'es'))
(out/'header-en.php').write_text(i18n_en.translate(i18n_en.flags(hp, 'en'), D))
(out/'footer-en.php').write_text(i18n_en.translate((out/'footer.php').read_text(), D))
fp = (out/'front-page.php').read_text().replace('<?php get_header(); ?>', "<?php get_header('en'); ?>").replace('<?php get_footer(); ?>', "<?php get_footer('en'); ?>")
fp = i18n_en.translate(fp, D)
for a, b2 in [('✅ Recibido. Te contactamos el mismo día hábil.', '✅ Received. We will contact you the same business day.'), ('✅ Recibido. Respondemos en menos de un día hábil.', '✅ Received. We reply within one business day.'), ('No se pudo enviar. Llámanos al 888-877-2583.', 'Could not send. Call us at 888-877-2583.'), ('No se pudo enviar. Escríbenos a info@marrerobernalmedia.com.', 'Could not send. Email us at info@marrerobernalmedia.com.')]:
    fp = fp.replace(a, b2)
# En inglés, la tarjeta de Recta en "La red" es Straight 2D Chest (Recta en inglés) — Eliam, 31-oct-2026
_ch = re.compile(r'<a class="ch" href="https://www\.youtube\.com/@RectaAlPecho\?sub_confirmation=1"(.*?)</a>', re.S)
def _s2d(m):
    b = m.group(0).replace('https://www.youtube.com/@RectaAlPecho?sub_confirmation=1', 'https://www.straight2dchest.com/')
    b = b.replace("img/av_recta.jpg", "img/av_s2d.jpg").replace('alt="Recta al Pecho"', 'alt="Straight 2D Chest"')
    b = re.sub(r'<h3>[^<]*</h3><p>[^<]*</p>', '<h3>Straight 2D Chest</h3><p>Recta Al Pecho in English. Sports · Baseball is the passion: interviews with English audio.</p>', b)
    return b
fp, _n = _ch.subn(_s2d, fp, count=1)
assert _n == 1, 'tarjeta de Recta no encontrada'
# Resto de la versión en inglés: Trabajos, páginas de Facebook y logos de "Nosotros" (Eliam, 31-oct-2026)
fp = fp.replace("img/recta.jpg')); ?>)\"></div>\n        <div class=\"body\"><img class=\"av\" src=\"<?php echo esc_url(get_theme_file_uri('img/av_s2d.jpg", "img/s2d.jpg')); ?>)\"></div>\n        <div class=\"body\"><img class=\"av\" src=\"<?php echo esc_url(get_theme_file_uri('img/av_s2d.jpg")
_wk = re.compile(r'<a class="wk" style="background-image:url\(<\?php echo esc_url\(get_theme_file_uri\(\'img/recta\.jpg\'\)\); \?>\)" href="https://www\.youtube\.com/@RectaAlPecho\?sub_confirmation=1"(.*?)</a>', re.S)
fp, _n = _wk.subn(lambda m: m.group(0).replace("img/recta.jpg", "img/s2d.jpg").replace("https://www.youtube.com/@RectaAlPecho?sub_confirmation=1", "https://www.straight2dchest.com/").replace("<b>Recta Al Pecho</b>", "<b>Straight 2D Chest</b>"), fp, count=1)
assert _n == 1, 'trabajo de Recta no encontrado'
_fb = re.compile(r'(<a class="fb" href="https://www\.facebook\.com/RectaAlPecho/"[^>]*>)<img src="([^"]*?)img/marcas/recta\.png([^"]*)" alt="Recta al Pecho"><b>Recta al Pecho</b>')
fp, _n = _fb.subn(lambda m: m.group(1) + '<img src="' + m.group(2) + 'img/marcas/s2d.png' + m.group(3) + '" alt="Straight 2D Chest"><b>Recta Al Pecho · Straight 2D Chest</b>', fp, count=1)
assert _n == 1, 'página de Facebook de Recta no encontrada'
_lg = re.compile(r'<a href="https://www\.youtube\.com/@RectaAlPecho\?sub_confirmation=1" target="_blank" rel="noopener"><img src="([^"]*?)img/marcas/recta\.png([^"]*)" alt="Recta Al Pecho"></a>')
fp, _n = _lg.subn(lambda m: '<a href="https://www.straight2dchest.com/" target="_blank" rel="noopener"><img src="' + m.group(1) + 'img/marcas/s2d.png' + m.group(2) + '" alt="Straight 2D Chest"></a>', fp, count=1)
assert _n == 1, 'logo de Recta en Nosotros no encontrado'
# Apps en inglés: la app de Recta abre en inglés como Straight 2D Chest (Eliam, 31-oct-2026)
_ap = re.compile(r'<img src="([^"]*?)img/marcas/recta\.png([^"]*)" alt="Recta Al Pecho">\s*<div>\s*<h3>Recta Al Pecho</h3>\s*<p>[^<]*</p>\s*<div class="ctas">\s*<a class="btn btn-acc" href="https://marrerobernalmedia\.com/recta/"')
fp, _n = _ap.subn(lambda m: '<img src="' + m.group(1) + 'img/marcas/s2d.png' + m.group(2) + '" alt="Straight 2D Chest">\n        <div>\n          <h3>Straight 2D Chest</h3>\n          <p>Sports, with baseball as the passion: the interviews with English audio, the series, the myths with their answers and the stories from straight2dchest.com.</p>\n          <div class="ctas">\n            <a class="btn btn-acc" href="https://marrerobernalmedia.com/recta/?lang=en"', fp, count=1)
assert _n == 1, 'app de Recta en inglés no encontrada'


(out/'front-page-en.php').write_text(fp)
fn = (out/'functions.php').read_text()
fn = re.sub(r"\n\s*wp_enqueue_script\('mbm-en'[^\n]*", "", fn)
fn = re.sub(r"\n\s*wp_enqueue_script\('mbm-idioma'[^\n]*", "", fn)
fn = fn.replace("if (is_front_page()) wp_enqueue_script('mbm-buscador'", "if (is_front_page() || mbm_is_en()) wp_enqueue_script('mbm-buscador'").replace("is_front_page() ? ", "(is_front_page() && !mbm_is_en()) ? ").replace("if (!is_front_page()) return;", "if (!is_front_page() || mbm_is_en()) return;").replace("if (is_front_page()) echo '<meta name=\"description\"", "if (is_front_page() && !mbm_is_en()) echo '<meta name=\"description\"")
fn += i18n_en.php_en('mbm', title_es_, title_en, desc, desc_en, '')
(out/'functions.php').write_text(fn)
print('tema generado en', out)
