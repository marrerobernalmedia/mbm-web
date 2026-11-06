<?php
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

add_filter('pre_get_document_title', fn($t) => (is_front_page() && !mbm_is_en()) ? "Marrero Bernal Media · Productora audiovisual para el público latino" : $t);

add_action('wp_head', function () {
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
  if (is_front_page() && !mbm_is_en()) echo '<meta name="description" content="' . esc_attr("Marrero Bernal Media LLC: productora audiovisual en Las Vegas con su propia red de canales. Comerciales, video corporativo, postproducción, dron con licencia FAA, diseño, web, podcast y publicidad dentro de la red.") . '">' . "\n";
  echo '<script>document.addEventListener("DOMContentLoaded",function(){var t=document.querySelector("title");if(t&&!t.getAttribute("data-en"))t.setAttribute("data-en",' . json_encode("Marrero Bernal Media · Video production, Las Vegas") . ');});</script>' . "\n";
}, 1);

add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('mbm-fonts', 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap', [], null);
  wp_enqueue_style('mbm', get_stylesheet_uri(), ['mbm-fonts'], @filemtime(get_stylesheet_directory() . '/style.css') ?: MBM_VER);
  wp_enqueue_script('mbm-seguidores', home_url('/seguidores.js'), [], @filemtime(ABSPATH . 'seguidores.js') ?: wp_date('YmdH'), true);
});

/** La portada siempre es front-page.php, aunque la página tenga plantilla de Elementor guardada. */
add_filter('template_include', function ($t) {
  if (is_front_page() && !is_admin()) { $f = get_theme_file_path('front-page.php'); if (file_exists($f)) return $f; }
  return $t;
}, 999);

/** SEO: idioma español, vista previa al compartir y ficha de organización para Google. */
add_filter('language_attributes', fn() => 'lang="es"');
add_action('wp_head', function () {
  if (!is_front_page() || mbm_is_en()) return;
  $img = get_theme_file_uri('img/og.jpg');
  echo '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal Media"><meta property="og:locale" content="es_US"><meta property="og:url" content="' . esc_url(home_url('/')) . '"><meta property="og:title" content="' . esc_attr(wp_get_document_title()) . '"><meta property="og:image" content="' . esc_url($img) . '"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "
";
  $ld = ['@context' => 'https://schema.org', '@type' => 'Organization', '@id' => home_url('/#mbm'), 'name' => 'Marrero Bernal Media LLC', 'alternateName' => 'Marrero Bernal Media', 'url' => home_url('/'), 'logo' => get_theme_file_uri('img/logo-color.svg'), 'image' => $img, 'foundingLocation' => 'Las Vegas, Nevada',
    'founder' => ['@type' => 'Person', 'name' => 'Eliam Marrero Bernal', 'sameAs' => ['https://www.imdb.com/name/nm3952887/']],
    'email' => 'info@marrerobernalmedia.com', 'telephone' => '+1-833-627-7376',
    'sameAs' => ['https://www.youtube.com/@marrerobernalmedia', 'https://www.facebook.com/marrerobernalmedia', 'https://x.com/MarreroBernalTV', 'https://www.youtube.com/@LaRisaEsCosaSeria', 'https://www.youtube.com/@RectaAlPecho', 'https://www.elhomedelarisa.com/', 'https://rectaalpecho.com/']];
  echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>' . "
";
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
  $body = "Nuevo proyecto desde marrerobernalmedia.com\n\nNombre: $nombre\nEmpresa: $empresa\nCorreo: $correo\nTeléfono/WhatsApp: $tel\nServicio: $serv\n\nMensaje:\n$msg\n\nFecha: " . wp_date('Y-m-d H:i');
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
add_action('template_redirect', function () {
  /* Páginas viejas (Elementor) ya en la papelera: sus URL van a la sección nueva */
  $p = trim(parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH) ?? '', '/');
  $m = ['apps' => '/#apps', 'sample-page' => '/', 'hello-world' => '/'];
  if (isset($m[$p])) { wp_redirect(home_url($m[$p]), 301); exit; }
}, 1);

remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('wp_head', 'wp_generator');

/** VERSIÓN EN INGLÉS legible por Google: /en/ (generada desde la maqueta con el diccionario en.js). */
function mbm_is_en() { return (bool) get_query_var('mbm_en'); }
add_filter('query_vars', function ($v) { $v[] = 'mbm_en'; return $v; });
add_action('init', function () {
  add_rewrite_rule('^en/?$', 'index.php?mbm_en=1', 'top');
  if (get_option('mbm_en_rw') !== '2') { flush_rewrite_rules(false); update_option('mbm_en_rw', '2'); }
});
add_filter('redirect_canonical', fn($r) => mbm_is_en() ? false : $r);
add_filter('template_include', function ($t) { if (mbm_is_en()) { $f = get_theme_file_path('front-page-en.php'); if (file_exists($f)) return $f; } return $t; }, 1000);
add_filter('language_attributes', fn($a) => mbm_is_en() ? 'lang="en"' : 'lang="es"', 20);
add_filter('pre_get_document_title', fn($t) => mbm_is_en() ? "Marrero Bernal Media · Video production, Las Vegas" : $t, 20);
add_filter('body_class', fn($c) => mbm_is_en() ? array_merge($c, ['lang-en']) : $c);
add_action('wp_head', function () {
  if (!is_front_page() && !mbm_is_en()) return;
  $es = home_url('/'); $en = home_url('/en/');
  echo '<link rel="alternate" hreflang="es" href="' . esc_url($es) . '"><link rel="alternate" hreflang="en" href="' . esc_url($en) . '"><link rel="alternate" hreflang="x-default" href="' . esc_url($es) . '">' . "\n";
  if (mbm_is_en()) {
    echo '<link rel="canonical" href="' . esc_url($en) . '"><meta name="description" content="' . esc_attr("Marrero Bernal Media LLC: productora audiovisual en Las Vegas con su propia red de canales. Comerciales, video corporativo, postproducción, dron con licencia FAA, diseño, web, podcast y publicidad dentro de la red.") . '"><meta property="og:locale" content="en_US"><meta property="og:url" content="' . esc_url($en) . '"><meta property="og:title" content="' . esc_attr("Marrero Bernal Media · Video production, Las Vegas") . '"><meta property="og:description" content="' . esc_attr("Marrero Bernal Media LLC: productora audiovisual en Las Vegas con su propia red de canales. Comerciales, video corporativo, postproducción, dron con licencia FAA, diseño, web, podcast y publicidad dentro de la red.") . '">' . "\n";
  }
}, 4);
/** En /en/ WordPress no pone su canonical de portada (lo pone el bloque de arriba). */
add_action('wp', function () { if (mbm_is_en()) remove_action('wp_head', 'rel_canonical'); });
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
