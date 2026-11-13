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
  return (is_front_page() && !mba_is_en()) ? 'Marrero Bernal & Associates · Seguros, taxes y trámites · Las Vegas, todo EE. UU. y el mundo' : $t;
});

add_action('wp_head', function () {
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
  if (is_front_page() && !mba_is_en()) echo '<meta name="description" content="' . esc_attr("Marrero Bernal & Associates: agencia independiente con sede en Las Vegas que atiende clientes en todo Estados Unidos y el extranjero, con contratos con múltiples compañías de primer nivel como Farmers y Progressive. Seguros de auto, hogar, vida, negocio y Medicare; workers' compensation para negocios; taxes personales y de negocio, contabilidad y nómina, ITIN, notaría, traducciones para el DMV y creación de LLC. En español, en North Las Vegas desde 2008.") . '">' . "\n";
}, 1);

add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('mba-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap', [], null);
  wp_enqueue_style('mba', get_stylesheet_uri(), ['mba-fonts'], @filemtime(get_stylesheet_directory() . '/style.css') ?: MBA_VER);
  wp_enqueue_script('mba-seguidores', 'https://marrerobernalmedia.com/seguidores.js', [], wp_date('YmdH'), true);
  if (is_front_page() || mba_is_en()) wp_enqueue_script('mba-buscador', get_theme_file_uri('buscador.js'), [], MBA_VER, true);
});

/** Chat del CRM (LeadConnector), igual que el sitio anterior. */
add_action('wp_footer', function () {
  echo '<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="6a3d5751a3d7dca497eb1973"></script>' . "\n";
  // De dónde llegó la visita (se envía con la solicitud para medir las promos).
  echo '<script>(function(){try{var s=sessionStorage;if(s.getItem("mba_fuente"))return;var q=new URLSearchParams(location.search),h=location.hostname.replace(/^www\./,""),r="";try{r=document.referrer?new URL(document.referrer).hostname.replace(/^www\./,""):""}catch(e){}var f=q.get("utm_source")||(q.get("fbclid")?"facebook":q.get("gclid")?"google ads":r&&r!==h?r:"directo"),c=q.get("utm_campaign");if(c)f+=" / "+c;s.setItem("mba_fuente",f.slice(0,80))}catch(e){}})();</script>' . "\n";
  // Chat: sin fecha de nacimiento en ningún idioma; en las páginas en español, todo el chat en español.
  echo '<script>(function(){var EN=/^\/en(\/|$)/.test(location.pathname),n=0,T={"Name":"Nombre","Phone":"Teléfono","Date Of Birth":"Fecha de nacimiento","Message":"Mensaje","Email":"Correo electrónico"},C=function(k){return "Al enviar, autorizas a Marrero Bernal Agency LLC a enviarte mensajes de texto o llamarte al número indicado con mensajes "+k+", posiblemente por medios automatizados. Pueden aplicarse tarifas de mensajes y datos; la frecuencia varía. El consentimiento no es condición de compra. <a href=\"https://www.leadconnectorhq.com/terms2\" target=\"_blank\" rel=\"noopener noreferrer\">Términos</a> y <a href=\"https://www.leadconnectorhq.com/privacy-policy\" target=\"_blank\" rel=\"noopener noreferrer\">política de privacidad</a>. Responde HELP para ayuda y STOP para cancelar."},t=setInterval(function(){var e=document.querySelector("chat-widget");if(++n>80){clearInterval(t);return}if(!e||!e.contactFormOptions)return;clearInterval(t);try{var o0=e.contactFormOptions,s0=typeof o0==="string",a0=(s0?JSON.parse(o0):o0).filter(function(f){return f.value!=="dateOfBirth"});e.contactFormOptions=s0?JSON.stringify(a0):a0;if(EN)return;e.locale="es";e.promptMsg="¡Hola! ¿Tienes una pregunta? Escríbenos.";e.heading="¿Tienes una pregunta?";e.subHeading="Escribe tu pregunta y un representante te responderá enseguida.";e.prefilledMessageText="Quiero más información";var o=e.contactFormOptions,s=typeof o==="string",a=s?JSON.parse(o):o;a.forEach(function(f){if(T[f.label]){f.label=T[f.label];f.placeholder=f.label}});e.contactFormOptions=s?JSON.stringify(a):a;var c=e.aTwoPCompliance;if(c){var cs=typeof c==="string",d=cs?JSON.parse(c):c;if(d.a2pOptInForm1)d.a2pOptInForm1=C("informativos o de servicio");if(d.a2pOptInForm2)d.a2pOptInForm2=C("promocionales");e.aTwoPCompliance=cs?JSON.stringify(d):d}}catch(x){}},250);})();</script>' . "\n";
}, 99);

/** Título en inglés para el conmutador de idioma. */
add_filter('document_title_parts', fn($p) => $p);
add_action('wp_head', function () { echo '<script>document.addEventListener("DOMContentLoaded",function(){var t=document.querySelector("title");if(t&&!t.getAttribute("data-en"))t.setAttribute("data-en",' . json_encode("Marrero Bernal & Associates · Insurance, taxes and paperwork · Las Vegas, nationwide and worldwide") . ');});</script>' . "\n"; }, 2);

/** SEO: idioma español, vista previa al compartir y ficha de negocio local (InsuranceAgency) para Google. */
add_filter('language_attributes', fn() => 'lang="es"');
add_action('wp_head', function () {
  if (!is_front_page() || mba_is_en()) return;
  $img = get_theme_file_uri('img/og.jpg'); $t = 'Marrero Bernal & Associates · Seguros, taxes y trámites · Las Vegas, todo EE. UU. y el mundo';
  echo '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal & Associates"><meta property="og:locale" content="es_US"><meta property="og:url" content="' . esc_url(home_url('/')) . '"><meta property="og:title" content="' . esc_attr($t) . '"><meta property="og:image" content="' . esc_url($img) . '"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "
";
  $ld = ['@context' => 'https://schema.org', '@type' => 'InsuranceAgency', '@id' => home_url('/#agencia'), 'name' => 'Marrero Bernal & Associates', 'url' => home_url('/'), 'logo' => get_theme_file_uri('img/logo.svg'), 'image' => $img,
    'telephone' => '+1-888-877-2583', 'priceRange' => '$$', 'foundingDate' => '2008', 'knowsLanguage' => ['es', 'en'],
    'address' => ['@type' => 'PostalAddress', 'streetAddress' => '3455 W Craig Rd Ste D', 'addressLocality' => 'North Las Vegas', 'addressRegion' => 'NV', 'postalCode' => '89032', 'addressCountry' => 'US'],
    'openingHoursSpecification' => [['@type' => 'OpeningHoursSpecification', 'dayOfWeek' => ['Monday','Tuesday','Wednesday','Thursday','Friday'], 'opens' => '09:00', 'closes' => '17:00']],
    'contactPoint' => [['@type' => 'ContactPoint', 'telephone' => '+1-888-877-2583', 'contactType' => 'customer service', 'availableLanguage' => ['Spanish','English']]],
    'areaServed' => [['@type' => 'State', 'name' => 'Nevada'], ['@type' => 'State', 'name' => 'California'], ['@type' => 'State', 'name' => 'Arizona']],
    'makesOffer' => [['@type' => 'Offer', 'itemOffered' => ['@type' => 'Service', 'name' => 'Preparación de impuestos a distancia (IRS e-file)', 'serviceType' => 'Tax preparation', 'areaServed' => [['@type' => 'Country', 'name' => 'United States'], ['@type' => 'Place', 'name' => 'Worldwide']]]], ['@type' => 'Offer', 'itemOffered' => ['@type' => 'Service', 'name' => 'Solicitud de ITIN con Agentes de Aceptación Certificados (CAA)', 'serviceType' => 'ITIN application']]],
    'sameAs' => ['https://www.facebook.com/marrerobernal']];
  echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>' . "
";
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
  $body = "Nueva solicitud desde marrerobernal.com\n\nNombre: $nombre\nTeléfono/WhatsApp: $tel\nCorreo: $correo\nServicio: $serv\n\nMensaje:\n$msg\n\nFecha: " . wp_date('Y-m-d H:i');
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

/** VERSIÓN EN INGLÉS legible por Google: /en/ (generada desde la maqueta con el diccionario en.js). */
function mba_is_en() { return (bool) get_query_var('mba_en'); }
add_filter('query_vars', function ($v) { $v[] = 'mba_en'; return $v; });
add_action('init', function () {
  add_rewrite_rule('^en/?$', 'index.php?mba_en=1', 'top');
  if (get_option('mba_en_rw') !== '2') { flush_rewrite_rules(false); update_option('mba_en_rw', '2'); }
});
add_filter('redirect_canonical', fn($r) => mba_is_en() ? false : $r);
add_filter('template_include', function ($t) { if (mba_is_en()) { $f = get_theme_file_path('front-page-en.php'); if (file_exists($f)) return $f; } return $t; }, 1000);
add_filter('language_attributes', fn($a) => mba_is_en() ? 'lang="en"' : 'lang="es"', 20);
add_filter('pre_get_document_title', fn($t) => mba_is_en() ? "Marrero Bernal & Associates · Insurance, taxes and paperwork · Las Vegas, nationwide and worldwide" : $t, 20);
add_filter('body_class', fn($c) => mba_is_en() ? array_merge($c, ['lang-en']) : $c);
add_action('wp_head', function () {
  if (!is_front_page() && !mba_is_en()) return;
  $es = home_url('/'); $en = home_url('/en/');
  echo '<link rel="alternate" hreflang="es" href="' . esc_url($es) . '"><link rel="alternate" hreflang="en" href="' . esc_url($en) . '"><link rel="alternate" hreflang="x-default" href="' . esc_url($es) . '">' . "\n";
  if (mba_is_en()) {
    echo '<link rel="canonical" href="' . esc_url($en) . '"><meta name="description" content="' . esc_attr("Marrero Bernal & Associates: independent agency based in Las Vegas serving clients across the United States and abroad, with contracts with top carriers such as Farmers and Progressive. Auto, home, life, business and Medicare insurance; workers' compensation for businesses; personal and business taxes, bookkeeping and payroll, ITIN, notary, Nevada DMV translations and LLC formation. In Spanish and English, in North Las Vegas since 2008.") . '"><meta property="og:locale" content="en_US"><meta property="og:url" content="' . esc_url($en) . '"><meta property="og:title" content="' . esc_attr("Marrero Bernal & Associates · Insurance, taxes and paperwork · Las Vegas, nationwide and worldwide") . '"><meta property="og:description" content="' . esc_attr("Marrero Bernal & Associates: independent agency based in Las Vegas serving clients across the United States and abroad, with contracts with top carriers such as Farmers and Progressive. Auto, home, life, business and Medicare insurance; workers' compensation for businesses; personal and business taxes, bookkeeping and payroll, ITIN, notary, Nevada DMV translations and LLC formation. In Spanish and English, in North Las Vegas since 2008.") . '">' . "\n";
  }
}, 4);
/** En /en/ WordPress no pone su canonical de portada (lo pone el bloque de arriba). */
add_action('wp', function () { if (mba_is_en()) remove_action('wp_head', 'rel_canonical'); });
/** Sitemap: añade /en/ al sitemap de WordPress. */
add_filter('wp_sitemaps_posts_entry', function ($e, $post) { return $e; }, 10, 2);
add_action('init', function () {
  if (!function_exists('wp_register_sitemap_provider')) return;
  wp_register_sitemap_provider('idiomas', new class extends WP_Sitemaps_Provider {
    public function __construct() { $this->name = 'idiomas'; $this->object_type = 'idiomas'; }
    public function get_url_list($page_num, $subtype = '') { return [['loc' => home_url('/')], ['loc' => home_url('/en/')]]; }
    public function get_max_num_pages($subtype = '') { return 1; }
  });
});
add_action('wp_footer', function () { echo "<script>(function(){try{var p=location.pathname.replace(/\\/+$/,'/'),en=p.indexOf('/en/')===0,s=localStorage.getItem('mb_lang');\ndocument.querySelectorAll('[data-lang]').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('mb_lang',a.getAttribute('data-lang'))}catch(e){}})});\nif(!en&&p==='/'&&!s&&!/bot|crawl|spider|slurp|google|bing|lighthouse|headless/i.test(navigator.userAgent)&&!/^es/i.test(navigator.language||'es'))location.replace('/en/'+location.hash);}catch(e){}})();</script>"; }, 5);
require_once __DIR__ . '/paginas.php';
