#!/usr/bin/env python3
"""Genera themes/mba/ (tema WordPress de marrerobernal.com) a partir de la maqueta maquetas/mba/index.html.
Correr desde la raíz del repo cada vez que cambie la maqueta: python3 tools/build_mba_theme.py"""
import re, shutil, pathlib, json, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import i18n_en
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

# reseñas de Google (Trustindex) en el sitio real
main_html = main_html.replace('<!--TRUSTINDEX--><p class="ti-demo">★★★★★ Aquí aparecen las reseñas de Google de la oficina.</p>', "<?php echo do_shortcode('[trustindex no-registration=google]'); ?>")

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
Description: Tema propio de marrerobernal.com (agencia de seguros independiente, taxes, ITIN, traducciones, notaría). Diseño aprobado por Eliam el 31-oct-2026. Se genera desde la maqueta con tools/build_mba_theme.py.
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
<?php if (is_front_page() || preg_match('#^/en/?$#', (string) parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH))) : ?><script src="https://s3.amazonaws.com/vonageclick2callme/click2callme.js?version=v1" c2cmKey="dmq10aFDG29Db9WC57GhgWY7EedaWz5f7or%2BNiWHlFtFD4%2FFgdPktS9wcP6CJ2AXDkJLUkTIkmImrRVuwjxoEQ%3D%3D" c2cmCompanyName="Marrero%20Bernal%20and%20Associates" c2cmLinkType="click-to-call-orange"></script><?php endif; ?>
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
  return is_front_page() ? 'Marrero Bernal & Associates · Seguros, taxes y trámites · Las Vegas, todo EE. UU. y el mundo' : $t;
});

add_action('wp_head', function () {
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\\n";
  if (is_front_page()) echo '<meta name="description" content="' . esc_attr(''' + json.dumps(desc, ensure_ascii=False) + ''') . '">' . "\\n";
}, 1);

add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('mba-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap', [], null);
  wp_enqueue_style('mba', get_stylesheet_uri(), ['mba-fonts'], @filemtime(get_stylesheet_directory() . '/style.css') ?: MBA_VER);
  wp_enqueue_script('mba-seguidores', 'https://marrerobernalmedia.com/seguidores.js', [], wp_date('YmdH'), true);
  wp_enqueue_script('mba-en', get_theme_file_uri('en.js'), [], @filemtime(get_theme_file_path('en.js')) ?: MBA_VER, true);
  wp_enqueue_script('mba-idioma', 'https://marrerobernalmedia.com/idioma.js', ['mba-en'], wp_date('Ymd'), true);
  if (is_front_page()) wp_enqueue_script('mba-buscador', get_theme_file_uri('buscador.js'), [], MBA_VER, true);
});

/** Chat del CRM (LeadConnector), igual que el sitio anterior. */
add_action('wp_footer', function () {
  echo '<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="6a3d5751a3d7dca497eb1973"></script>' . "\\n";
  // De dónde llegó la visita (se envía con la solicitud para medir las promos).
  echo '<script>(function(){try{var s=sessionStorage;if(s.getItem("mba_fuente"))return;var q=new URLSearchParams(location.search),h=location.hostname.replace(/^www\\./,""),r="";try{r=document.referrer?new URL(document.referrer).hostname.replace(/^www\\./,""):""}catch(e){}var f=q.get("utm_source")||(q.get("fbclid")?"facebook":q.get("gclid")?"google ads":r&&r!==h?r:"directo"),c=q.get("utm_campaign");if(c)f+=" / "+c;s.setItem("mba_fuente",f.slice(0,80))}catch(e){}})();</script>' . "\\n";
  // En las páginas en español, el chat sale en español (el widget viene en inglés por defecto).
  echo '<script>(function(){if(/^\\/en(\\/|$)/.test(location.pathname))return;var n=0,T={"Name":"Nombre","Phone":"Teléfono","Date Of Birth":"Fecha de nacimiento","Message":"Mensaje","Email":"Correo electrónico"},C=function(k){return "Al enviar, autorizas a Marrero Bernal Agency LLC a enviarte mensajes de texto o llamarte al número indicado con mensajes "+k+", posiblemente por medios automatizados. Pueden aplicarse tarifas de mensajes y datos; la frecuencia varía. El consentimiento no es condición de compra. <a href=\\"https://www.leadconnectorhq.com/terms2\\" target=\\"_blank\\" rel=\\"noopener noreferrer\\">Términos</a> y <a href=\\"https://www.leadconnectorhq.com/privacy-policy\\" target=\\"_blank\\" rel=\\"noopener noreferrer\\">política de privacidad</a>. Responde HELP para ayuda y STOP para cancelar."},t=setInterval(function(){var e=document.querySelector("chat-widget");if(++n>80){clearInterval(t);return}if(!e||!e.contactFormOptions)return;clearInterval(t);try{e.locale="es";e.promptMsg="¡Hola! ¿Tienes una pregunta? Escríbenos.";e.heading="¿Tienes una pregunta?";e.subHeading="Escribe tu pregunta y un representante te responderá enseguida.";e.prefilledMessageText="Quiero más información";var o=e.contactFormOptions,s=typeof o==="string",a=s?JSON.parse(o):o;a.forEach(function(f){if(T[f.label]){f.label=T[f.label];f.placeholder=f.label}});e.contactFormOptions=s?JSON.stringify(a):a;var c=e.aTwoPCompliance;if(c){var cs=typeof c==="string",d=cs?JSON.parse(c):c;if(d.a2pOptInForm1)d.a2pOptInForm1=C("informativos o de servicio");if(d.a2pOptInForm2)d.a2pOptInForm2=C("promocionales");e.aTwoPCompliance=cs?JSON.stringify(d):d}}catch(x){}},250);})();</script>' . "\\n";
}, 99);

/** Título en inglés para el conmutador de idioma. */
add_filter('document_title_parts', fn($p) => $p);
add_action('wp_head', function () { echo '<script>document.addEventListener("DOMContentLoaded",function(){var t=document.querySelector("title");if(t&&!t.getAttribute("data-en"))t.setAttribute("data-en",' . json_encode(''' + json.dumps(title_en, ensure_ascii=False) + ''') . ');});</script>' . "\\n"; }, 2);

/** SEO: idioma español, vista previa al compartir y ficha de negocio local (InsuranceAgency) para Google. */
add_filter('language_attributes', fn() => 'lang="es"');
add_action('wp_head', function () {
  if (!is_front_page()) return;
  $img = get_theme_file_uri('img/og.jpg'); $t = 'Marrero Bernal & Associates · Seguros, taxes y trámites · Las Vegas, todo EE. UU. y el mundo';
  echo '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal & Associates"><meta property="og:locale" content="es_US"><meta property="og:url" content="' . esc_url(home_url('/')) . '"><meta property="og:title" content="' . esc_attr($t) . '"><meta property="og:image" content="' . esc_url($img) . '"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "\n";
  $ld = ['@context' => 'https://schema.org', '@type' => 'InsuranceAgency', '@id' => home_url('/#agencia'), 'name' => 'Marrero Bernal & Associates', 'url' => home_url('/'), 'logo' => get_theme_file_uri('img/logo.svg'), 'image' => $img,
    'telephone' => '+1-888-877-2583', 'priceRange' => '$$', 'foundingDate' => '2008', 'knowsLanguage' => ['es', 'en'],
    'address' => ['@type' => 'PostalAddress', 'streetAddress' => '3455 W Craig Rd Ste D', 'addressLocality' => 'North Las Vegas', 'addressRegion' => 'NV', 'postalCode' => '89032', 'addressCountry' => 'US'],
    'openingHoursSpecification' => [['@type' => 'OpeningHoursSpecification', 'dayOfWeek' => ['Monday','Tuesday','Wednesday','Thursday','Friday'], 'opens' => '09:00', 'closes' => '17:00']],
    'contactPoint' => [['@type' => 'ContactPoint', 'telephone' => '+1-888-877-2583', 'contactType' => 'customer service', 'availableLanguage' => ['Spanish','English']]],
    'areaServed' => [['@type' => 'State', 'name' => 'Nevada'], ['@type' => 'State', 'name' => 'California'], ['@type' => 'State', 'name' => 'Arizona']],
    'makesOffer' => [['@type' => 'Offer', 'itemOffered' => ['@type' => 'Service', 'name' => 'Preparación de impuestos a distancia (IRS e-file)', 'serviceType' => 'Tax preparation', 'areaServed' => [['@type' => 'Country', 'name' => 'United States'], ['@type' => 'Place', 'name' => 'Worldwide']]]], ['@type' => 'Offer', 'itemOffered' => ['@type' => 'Service', 'name' => 'Solicitud de ITIN con Agentes de Aceptación Certificados (CAA)', 'serviceType' => 'ITIN application']]],
    'sameAs' => ['https://www.facebook.com/marrerobernal']];
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

# ---------- versión en inglés (/en/) ----------
D = i18n_en.load_dict(root/'maquetas/mba/en.js')
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
(out/'front-page-en.php').write_text(fp)
fn = (out/'functions.php').read_text()
fn = re.sub(r"\n\s*wp_enqueue_script\('mba-en'[^\n]*", "", fn)
fn = re.sub(r"\n\s*wp_enqueue_script\('mba-idioma'[^\n]*", "", fn)
fn = fn.replace("if (is_front_page()) wp_enqueue_script('mba-buscador'", "if (is_front_page() || mba_is_en()) wp_enqueue_script('mba-buscador'").replace("is_front_page() ? ", "(is_front_page() && !mba_is_en()) ? ").replace("if (!is_front_page()) return;", "if (!is_front_page() || mba_is_en()) return;").replace("if (is_front_page()) echo '<meta name=\"description\"", "if (is_front_page() && !mba_is_en()) echo '<meta name=\"description\"")
fn += i18n_en.php_en('mba', title_es_, title_en, desc, desc_en, '')
(out/'functions.php').write_text(fn)
print('tema generado en', out)
import runpy; runpy.run_path(str(root/'tools/build_mba_paginas.py'))
