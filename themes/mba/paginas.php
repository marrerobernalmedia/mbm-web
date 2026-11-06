<?php
/** Páginas propias (Medicare, Obamacare, Medicaid, dispositivos) y redirecciones de páginas viejas.
 *  GENERADO por tools/build_mba_paginas.py — no editar a mano. */
if (!defined('ABSPATH')) exit;

function mba_pag_routes() { static $r = null; if ($r === null) $r = json_decode('{"medicare|es": {"file": "medicare-es", "title": "Medicare Advantage en español · Marrero Bernal & Associates", "desc": "Te ayudamos a comparar planes Medicare Advantage y de medicinas en tu condado, en español. Fechas de inscripción, qué revisar y cómo trabajamos. North Las Vegas.", "img": "medicare.jpg", "pair": "/en/medicare/", "self": "/medicare/"}, "medicare|en": {"file": "medicare-en", "title": "Medicare Advantage help in Spanish and English · Marrero Bernal & Associates", "desc": "We help you compare the Medicare Advantage and drug plans we offer in your county, in Spanish or English. Enrollment dates, what to check and how we work. North Las Vegas.", "img": "medicare.jpg", "pair": "/medicare/", "self": "/en/medicare/"}, "obamacare-nevada|es": {"file": "obamacare-es", "title": "Obamacare en Nevada (Nevada Health Link) con broker certificado · Marrero Bernal & Associates", "desc": "Somos broker certificado de Nevada Health Link. Te ayudamos en español a comparar planes, ver si calificas para ayuda con el pago e inscribirte. Inscripción abierta hasta el 15 de enero.", "img": "salud.jpg", "pair": "/en/obamacare-nevada/", "self": "/obamacare-nevada/"}, "obamacare-nevada|en": {"file": "obamacare-en", "title": "Obamacare in Nevada (Nevada Health Link) with a certified broker · Marrero Bernal & Associates", "desc": "We are a Nevada Health Link certified broker. We help you compare plans, see if you qualify for financial help and enroll, in English or Spanish. Open enrollment runs through January 15.", "img": "salud.jpg", "pair": "/obamacare-nevada/", "self": "/en/obamacare-nevada/"}, "medicaid-nevada|es": {"file": "medicaid-es", "title": "Medicaid de Nevada: cómo solicitarlo · Marrero Bernal & Associates", "desc": "Te orientamos en español sobre Medicaid y Nevada Check Up: quién puede calificar, cómo solicitar en Access Nevada y qué hacer si no calificas.", "img": "medicaid.jpg", "pair": "/en/medicaid-nevada/", "self": "/medicaid-nevada/"}, "medicaid-nevada|en": {"file": "medicaid-en", "title": "Nevada Medicaid: how to apply · Marrero Bernal & Associates", "desc": "Guidance in English and Spanish on Medicaid and Nevada Check Up: who may qualify, how to apply on Access Nevada and what to do if you do not qualify.", "img": "medicaid.jpg", "pair": "/medicaid-nevada/", "self": "/en/medicaid-nevada/"}, "proteccion-de-dispositivos|es": {"file": "dispositivos-es", "title": "Protección de teléfonos y electrónicos desde $16.99 al mes · Marrero Bernal & Associates", "desc": "Pantalla rota, derrames, fallas, pérdida o robo. Protección de dispositivos de Farmers para los teléfonos de la casa y tus electrónicos, desde $16.99 al mes. Aplican términos.", "img": "dispositivos.jpg", "pair": "/en/device-protection/", "self": "/proteccion-de-dispositivos/"}, "device-protection|en": {"file": "dispositivos-en", "title": "Phone and electronics protection from $16.99 a month · Marrero Bernal & Associates", "desc": "Cracked screens, spills, breakdowns, loss or theft. Farmers device protection for your household phones and electronics, from $16.99 a month. Terms apply.", "img": "dispositivos.jpg", "pair": "/proteccion-de-dispositivos/", "self": "/en/device-protection/"}}', true); return $r; }
function mba_pag() { $s = get_query_var('mba_pag'); if (!$s) return null; $k = $s . '|' . (get_query_var('mba_pl') ?: 'es'); $r = mba_pag_routes(); return isset($r[$k]) ? $r[$k] + ['lang' => get_query_var('mba_pl') ?: 'es'] : null; }

add_filter('query_vars', function ($v) { $v[] = 'mba_pag'; $v[] = 'mba_pl'; return $v; });
add_action('init', function () {
  foreach (mba_pag_routes() as $k => $r) {
    [$slug, $lang] = explode('|', $k);
    $re = ($lang === 'en' ? '^en/' : '^') . preg_quote($slug, '#') . '/?$';
    add_rewrite_rule($re, 'index.php?mba_pag=' . $slug . '&mba_pl=' . $lang, 'top');
  }
  if (get_option('mba_pag_rw') !== '3') { flush_rewrite_rules(false); update_option('mba_pag_rw', '3'); }
});
add_filter('redirect_canonical', fn($r) => mba_pag() ? false : $r);
add_action('wp', function () { global $wp_query; if (mba_pag()) { $wp_query->is_404 = false; $wp_query->is_home = false; status_header(200); remove_action('wp_head', 'rel_canonical'); } });
add_filter('template_include', function ($t) { $p = mba_pag(); if ($p) { $f = get_theme_file_path('paginas/' . $p['file'] . '.php'); if (file_exists($f)) return $f; } return $t; }, 1001);
add_filter('pre_get_document_title', function ($t) { $p = mba_pag(); return $p ? $p['title'] : $t; }, 30);
add_filter('language_attributes', function ($a) { $p = mba_pag(); return $p ? 'lang="' . $p['lang'] . '"' : $a; }, 30);
add_filter('body_class', function ($c) { $p = mba_pag(); if ($p) { $c[] = 'subpagina'; if ($p['lang'] === 'en') $c[] = 'lang-en'; } return $c; });
add_action('wp_head', function () {
  $p = mba_pag(); if (!$p) return;
  $self = home_url($p['self']); $pair = home_url($p['pair']);
  [$es, $en] = $p['lang'] === 'es' ? [$self, $pair] : [$pair, $self];
  echo '<meta name="description" content="' . esc_attr($p['desc']) . '"><link rel="canonical" href="' . esc_url($self) . '">'
    . '<link rel="alternate" hreflang="es" href="' . esc_url($es) . '"><link rel="alternate" hreflang="en" href="' . esc_url($en) . '"><link rel="alternate" hreflang="x-default" href="' . esc_url($es) . '">'
    . '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal & Associates"><meta property="og:locale" content="' . ($p['lang'] === 'en' ? 'en_US' : 'es_US') . '">'
    . '<meta property="og:url" content="' . esc_url($self) . '"><meta property="og:title" content="' . esc_attr($p['title']) . '"><meta property="og:description" content="' . esc_attr($p['desc']) . '">'
    . '<meta property="og:image" content="' . esc_url(get_theme_file_uri('img/' . $p['img'])) . '"><meta name="twitter:card" content="summary_large_image">' . "\n";
}, 5);

/** Cabecera y pie dentro de una subpágina: las anclas (#personal…) vuelven a la portada del idioma y las banderas llevan a la página par. */
function mba_pag_fix($h, $lang, $self, $other) {
  $home = $lang === 'en' ? home_url('/en/') : home_url('/');
  $h = preg_replace('/href="#(?!")/', 'href="' . esc_url($home) . '#', $h);
  if ($lang === 'en') $h = str_replace('<a class="logo" href="' . esc_url(home_url('/')) . '"', '<a class="logo" href="' . esc_url($home) . '"', $h);
  $es = $lang === 'es' ? home_url('/' . $self . '/') : home_url('/' . $other . '/');
  $en = $lang === 'en' ? home_url('/en/' . $self . '/') : home_url('/en/' . $other . '/');
  $h = preg_replace('/href="[^"]*"(\s+hreflang="es")/', 'href="' . esc_url($es) . '"$1', $h);
  $h = preg_replace('/href="[^"]*"(\s+hreflang="en")/', 'href="' . esc_url($en) . '"$1', $h);
  return $h;
}

/** Páginas viejas del sitio de Elementor → 301 a su destino actual (no se borra nada en WordPress). */
add_action('template_redirect', function () {
  $map = json_decode('{"insurance": "/#personal", "insurance-2": "https://esales.farmers.com/fastquote?Lob=autoHome&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "vehicle-insurance": "https://esales.farmers.com/fastquote?Lob=Auto&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "home-insurance": "https://esales.farmers.com/fastquote?Lob=Home&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "life": "https://esales.farmers.com/fastquote?Lob=Lifec&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "business-insurance-2": "https://esales.farmers.com/fastquote?Lob=Business&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "health": "/obamacare-nevada/", "travel": "/#personal", "personal": "/#personal", "business": "/#negocios", "taxes": "/#irs", "taxes-2": "/#irs", "business-taxes": "/#negocios", "business-licenses": "/#negocios", "about-us": "/#nosotros", "contact": "/#contacto", "blog": "/", "immigration": "/", "payroll": "/", "dmv": "/#dmv", "translations": "/#dmv", "notary": "/#contacto", "media": "https://marrerobernalmedia.com/", "do-you-want-to-avoid-paying-taxes-today-on-your-first-61000-per-year": "/#irs", "the-advance-of-the-child-tax-credit-a-double-edged-weapon": "/#irs", "new-taxes-when-using-services-like-zelle-venmo-and-cash-app": "/#irs", "what-you-need-to-know-when-buying-health-insurance": "/obamacare-nevada/", "when-can-i-apply-for-affordable-health-insurance": "/obamacare-nevada/", "full-cover-is-never-full-cover": "/#personal", "do-i-have-the-correct-auto-insurance": "/#personal", "what-business-insurances-do-i-need": "/#negocios", "how-to-start-your-own-business": "/#negocios", "i-have-an-idea": "/#negocios", "who-do-you-work-for": "/", "growing-your-money-tree": "/", "compound-interest-the-mary-poppins-way": "/", "you-can-avoid-paying-taxes": "/#irs", "new-tax-changes-for-2021": "/#irs", "income": "/#irs", "earned-or-not-that-is-the-question": "/#irs", "nothing-is-certain-except-death-and-taxes": "/#irs", "fun-fun-and-more-fun": "/", "to-each-his-own": "/", "if-its-about-spending-less": "/", "how-to-pay-bills-and-die-while-doing-it": "/", "are-you-saving-for-a-rainy-day": "/", "hello-world": "/"}', true);
  $path = trim(parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH) ?? '', '/');
  if (isset($map[$path])) { $to = $map[$path]; if ($to[0] === '/') $to = home_url($to); wp_redirect($to, 301, 'Marrero Bernal & Associates'); exit; }
}, 1);
/** …y salen del sitemap. */
add_filter('wp_sitemaps_posts_query_args', function ($a, $type) {
  if ($type !== 'page') return $a;
  $ids = [];
  foreach (array_keys(json_decode('{"insurance": "/#personal", "insurance-2": "https://esales.farmers.com/fastquote?Lob=autoHome&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "vehicle-insurance": "https://esales.farmers.com/fastquote?Lob=Auto&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "home-insurance": "https://esales.farmers.com/fastquote?Lob=Home&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "life": "https://esales.farmers.com/fastquote?Lob=Lifec&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "business-insurance-2": "https://esales.farmers.com/fastquote?Lob=Business&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032", "health": "/obamacare-nevada/", "travel": "/#personal", "personal": "/#personal", "business": "/#negocios", "taxes": "/#irs", "taxes-2": "/#irs", "business-taxes": "/#negocios", "business-licenses": "/#negocios", "about-us": "/#nosotros", "contact": "/#contacto", "blog": "/", "immigration": "/", "payroll": "/", "dmv": "/#dmv", "translations": "/#dmv", "notary": "/#contacto", "media": "https://marrerobernalmedia.com/", "do-you-want-to-avoid-paying-taxes-today-on-your-first-61000-per-year": "/#irs", "the-advance-of-the-child-tax-credit-a-double-edged-weapon": "/#irs", "new-taxes-when-using-services-like-zelle-venmo-and-cash-app": "/#irs", "what-you-need-to-know-when-buying-health-insurance": "/obamacare-nevada/", "when-can-i-apply-for-affordable-health-insurance": "/obamacare-nevada/", "full-cover-is-never-full-cover": "/#personal", "do-i-have-the-correct-auto-insurance": "/#personal", "what-business-insurances-do-i-need": "/#negocios", "how-to-start-your-own-business": "/#negocios", "i-have-an-idea": "/#negocios", "who-do-you-work-for": "/", "growing-your-money-tree": "/", "compound-interest-the-mary-poppins-way": "/", "you-can-avoid-paying-taxes": "/#irs", "new-tax-changes-for-2021": "/#irs", "income": "/#irs", "earned-or-not-that-is-the-question": "/#irs", "nothing-is-certain-except-death-and-taxes": "/#irs", "fun-fun-and-more-fun": "/", "to-each-his-own": "/", "if-its-about-spending-less": "/", "how-to-pay-bills-and-die-while-doing-it": "/", "are-you-saving-for-a-rainy-day": "/", "hello-world": "/"}', true)) as $s) { $pg = get_page_by_path($s); if ($pg) $ids[] = $pg->ID; }
  $a['post__not_in'] = array_merge($a['post__not_in'] ?? [], $ids); return $a;
}, 10, 2);
add_action('init', function () {
  if (!function_exists('wp_register_sitemap_provider')) return;
  wp_register_sitemap_provider('paginas', new class extends WP_Sitemaps_Provider {
    public function __construct() { $this->name = 'paginas'; $this->object_type = 'paginas'; }
    public function get_url_list($page_num, $subtype = '') { return array_map(fn($r) => ['loc' => home_url($r['self'])], array_values(mba_pag_routes())); }
    public function get_max_num_pages($subtype = '') { return 1; }
  });
});
