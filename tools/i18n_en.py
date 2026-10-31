"""Traducción al inglés en el servidor (para las páginas /en/ que Google puede leer).
Usa el mismo diccionario que el conmutador del navegador (en.js: {texto español: texto inglés})."""
import json, re, subprocess, pathlib, html as _h


def load_dict(en_js: pathlib.Path) -> dict:
    out = subprocess.run(
        ["node", "-e", "global.window={};eval(require('fs').readFileSync(process.argv[1],'utf8'));process.stdout.write(JSON.stringify(window.I18N_EN))", str(en_js)],
        capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def translate(html: str, D: dict) -> str:
    # no tocar scripts ni estilos
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<\?php.*?\?>)', html, flags=re.S | re.I)
    for i in range(0, len(parts), 2):
        seg = parts[i]
        def txt(m):
            raw = m.group(1); k = raw.strip()
            ku = _h.unescape(k)
            if k in D or ku in D:
                v = D[k] if k in D else _h.escape(D[ku], quote=False)
                j = raw.index(k)
                return '>' + raw[:j] + v + raw[j + len(k):] + '<'
            return m.group(0)
        seg = re.sub(r'>([^<>]+)<', txt, seg)
        def att(m):
            v = m.group(2); k = v.strip(); ku = _h.unescape(k)
            if k in D: return f'{m.group(1)}="{_h.escape(D[k])}"'
            if ku in D: return f'{m.group(1)}="{_h.escape(D[ku])}"'
            return m.group(0)
        seg = re.sub(r'\b(placeholder|alt|title|aria-label)="([^"]*)"', att, seg)
        parts[i] = seg
    return ''.join(parts)


FLAGS_JS = """<script>(function(){try{var p=location.pathname.replace(/\\/+$/,'/'),en=p.indexOf('/en/')===0,s=localStorage.getItem('mb_lang');
document.querySelectorAll('[data-lang]').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('mb_lang',a.getAttribute('data-lang'))}catch(e){}})});
if(!en&&p==='/'&&!s&&!/bot|crawl|spider|slurp|google|bing|lighthouse|headless/i.test(navigator.userAgent)&&!/^es/i.test(navigator.language||'es'))location.replace('/en/'+location.hash);}catch(e){}})();</script>"""


def flags(html: str, lang: str, home_php: str = "<?php echo esc_url(home_url('/')); ?>", en_php: str = "<?php echo esc_url(home_url('/en/')); ?>") -> str:
    """Las banderas pasan a ser enlaces reales: ES → /, EN → /en/ (con la activa marcada)."""
    html = html.replace('<a href="#" data-lang="es"', f'<a href="{home_php}" hreflang="es" data-lang="es"' + (' class="on"' if lang == 'es' else ''))
    html = html.replace('<a href="#" data-lang="en"', f'<a href="{en_php}" hreflang="en" data-lang="en"' + (' class="on"' if lang == 'en' else ''))
    return html


def php_en(prefix: str, title_es: str, title_en: str, desc_es: str, desc_en: str, locale_site: str) -> str:
    """Bloque PHP para functions.php: ruta /en/, plantilla en inglés, hreflang y metadatos."""
    j = lambda s: json.dumps(s, ensure_ascii=False)
    return f"""
/** VERSIÓN EN INGLÉS legible por Google: /en/ (generada desde la maqueta con el diccionario en.js). */
function {prefix}_is_en() {{ return (bool) get_query_var('{prefix}_en'); }}
add_filter('query_vars', function ($v) {{ $v[] = '{prefix}_en'; return $v; }});
add_action('init', function () {{
  add_rewrite_rule('^en/?$', 'index.php?{prefix}_en=1', 'top');
  if (get_option('{prefix}_en_rw') !== '2') {{ flush_rewrite_rules(false); update_option('{prefix}_en_rw', '2'); }}
}});
add_filter('redirect_canonical', fn($r) => {prefix}_is_en() ? false : $r);
add_filter('template_include', function ($t) {{ if ({prefix}_is_en()) {{ $f = get_theme_file_path('front-page-en.php'); if (file_exists($f)) return $f; }} return $t; }}, 1000);
add_filter('language_attributes', fn($a) => {prefix}_is_en() ? 'lang="en"' : 'lang="es"', 20);
add_filter('pre_get_document_title', fn($t) => {prefix}_is_en() ? {j(title_en)} : $t, 20);
add_filter('body_class', fn($c) => {prefix}_is_en() ? array_merge($c, ['lang-en']) : $c);
add_action('wp_head', function () {{
  if (!is_front_page() && !{prefix}_is_en()) return;
  $es = home_url('/'); $en = home_url('/en/');
  echo '<link rel="alternate" hreflang="es" href="' . esc_url($es) . '"><link rel="alternate" hreflang="en" href="' . esc_url($en) . '"><link rel="alternate" hreflang="x-default" href="' . esc_url($es) . '">' . "\\n";
  if ({prefix}_is_en()) {{
    echo '<link rel="canonical" href="' . esc_url($en) . '"><meta name="description" content="' . esc_attr({j(desc_en)}) . '"><meta property="og:locale" content="en_US"><meta property="og:url" content="' . esc_url($en) . '"><meta property="og:title" content="' . esc_attr({j(title_en)}) . '"><meta property="og:description" content="' . esc_attr({j(desc_en)}) . '">' . "\\n";
  }}
}}, 4);
/** En /en/ WordPress no pone su canonical de portada (lo pone el bloque de arriba). */
add_action('wp', function () {{ if ({prefix}_is_en()) remove_action('wp_head', 'rel_canonical'); }});
/** Sitemap: añade /en/ al sitemap de WordPress. */
add_filter('wp_sitemaps_posts_entry', function ($e, $post) {{ return $e; }}, 10, 2);
add_action('init', function () {{
  if (!function_exists('wp_register_sitemap_provider')) return;
  wp_register_sitemap_provider('idiomas', new class extends WP_Sitemaps_Provider {{
    public function __construct() {{ $this->name = 'idiomas'; $this->object_type = 'idiomas'; }}
    public function get_url_list($page_num, $subtype = '') {{ return [['loc' => home_url('/')], ['loc' => home_url('/en/')]]; }}
    public function get_max_num_pages($subtype = '') {{ return 1; }}
  }});
}});
add_action('wp_footer', function () {{ echo {j(FLAGS_JS)}; }}, 5);
"""
