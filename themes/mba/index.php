<?php get_header(); ?>
<div class="page-wrap">
<?php if (have_posts()): while (have_posts()): the_post(); ?>
  <article><h1><?php the_title(); ?></h1><?php the_content(); ?></article>
<?php endwhile; else: ?>
  <h1>No hay nada aquí.</h1><p><a href="<?php echo esc_url(home_url('/')); ?>">Volver al inicio</a></p>
<?php endif; ?>
</div>
<?php get_footer(); ?>
