<?php get_header(); while (have_posts()): the_post(); ?>
<main class="wrap"><div class="page-body"><h1><?php the_title(); ?></h1><article class="art" style="margin-top:0"><?php the_content(); ?></article></div></main>
<?php endwhile; get_footer();
