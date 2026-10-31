<?php get_header(); ?>
<main class="wrap">
<div class="sec-h"><h1>Nuestros autores</h1><p>Las voces que escriben en Recta al Pecho.</p></div>
<div class="autores">
<?php foreach (recta_autores() as $u): ?>
 <a class="autor-card" href="<?php echo esc_url(get_author_posts_url($u->ID)); ?>"><?php echo recta_autor_foto($u->ID, 96); ?><b><?php echo esc_html($u->display_name); ?></b><p><?php echo esc_html(wp_trim_words(recta_autor_bio($u->ID), 22)); ?></p><small><?php echo (int) count_user_posts($u->ID); ?> artículos</small></a>
<?php endforeach; ?>
</div>
</main>
<?php get_footer();
