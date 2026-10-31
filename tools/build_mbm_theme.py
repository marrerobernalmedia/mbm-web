#!/usr/bin/env python3
"""Genera themes/mbm/ (tema WordPress de marrerobernalmedia.com) a partir de maquetas/mbm/index.html.
Correr desde la raíz del repo cada vez que cambie la maqueta: python3 tools/build_mbm_theme.py"""
import re, shutil, pathlib, json
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
  wp_enqueue_style('mbm', get_stylesheet_uri(), ['mbm-fonts'], MBM_VER);
  wp_enqueue_script('mbm-seguidores', home_url('/seguidores.js'), [], null, true);
  wp_enqueue_script('mbm-en', get_theme_file_uri('en.js'), [], MBM_VER, true);
  wp_enqueue_script('mbm-idioma', home_url('/idioma.js'), ['mbm-en'], null, true);
});

/** La portada siempre es front-page.php, aunque la página tenga plantilla de Elementor guardada. */
add_filter('template_include', function ($t) {
  if (is_front_page() && !is_admin()) { $f = get_theme_file_path('front-page.php'); if (file_exists($f)) return $f; }
  return $t;
}, 999);

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
print('tema generado en', out)
