<?php get_header(); ?>
<section class="hero">
  <div class="bg"></div>
  <div class="wrap">
    <div class="kicker">Productora audiovisual · Las Vegas</div>
    <h1>Historias que llegan al corazón de <em>nuestra gente</em>.</h1>
    <p class="lead">Marrero Bernal Media es una productora con experiencia en el mercado latino: producimos, editamos y distribuimos contenido. Con cinco canales de YouTube y más de <span data-seg="tot.todo" data-fmt="mil">1,080,000</span> seguidores entre Facebook, Instagram y YouTube, no solo hacemos tu video: sabemos hacerlo llegar.</p>
    <div class="ctas">
      <a class="btn btn-acc" href="#contacto">Cuéntanos tu proyecto</a>
      <a class="btn btn-ghost" href="#red">Conoce la red ↓</a>
    </div>
  </div>
</section>

<div class="stats">
  <div class="wrap">
    <div class="stat"><b>5</b><span>CANALES EN YOUTUBE</span></div>
    <div class="stat"><b>10</b><span>PÁGINAS EN FACEBOOK</span></div>
    <div class="stat"><b>130K+</b><span>SUSCRIPTORES EN YOUTUBE</span></div>
    <div class="stat"><b>27M+</b><span>VISTAS ACUMULADAS</span></div>
    <div class="stat"><b>4,500+</b><span>PIEZAS PUBLICADAS</span></div>
    <div class="stat"><b data-seg="tot.todo" data-fmt="full" style="font-size:30px">1,083,324</b><span>SEGUIDORES EN REDES · AL <span data-seg="actualizado">2026-10-30</span></span></div>
  </div>
</div>

<section id="red">
  <div class="wrap">
    <div class="kicker">La red</div>
    <h2>Una audiencia propia, construida semana a semana.</h2>
    <p class="lead">Cinco canales de YouTube con estreno fijo cada semana y páginas de Facebook e Instagram que suman más de <span data-seg="tot.metaRed" data-fmt="mil">950,000</span> seguidores. Todo producido por nosotros.</p>
    <div class="red-grid">
      <a class="ch" href="https://www.youtube.com/@LaRisaEsCosaSeria?sub_confirmation=1" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/risa.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_risa.jpg')); ?>" alt="La Risa es Cosa Seria"><div><h3>La Risa es Cosa Seria</h3><p>Stand-up y comedia cubana. Estrenos martes y viernes.</p><span class="n"><span data-seg="yt.larisa">91K</span> en YouTube · <span data-seg="fb.larisa">584K</span> en Facebook · <span data-seg="ig.larisa">50K</span> en Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.youtube.com/@RectaAlPecho?sub_confirmation=1" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/recta.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_recta.jpg')); ?>" alt="Recta al Pecho"><div><h3>Recta Al Pecho</h3><p>Entrevistas y análisis de béisbol latino. Jueves.</p><span class="n"><span data-seg="yt.recta">19K</span> en YouTube · <span data-seg="fb.recta">71K</span> en Facebook · <span data-seg="ig.recta">9.2K</span> en Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.lcedr.com" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/cosa.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_cosa.jpg')); ?>" alt="La Cosa Es De Risa"><div><h3>La Cosa Es De Risa</h3><p>El noticiero oficial de Apagonia. Domingos.</p><span class="n"><span data-seg="yt.lacosa">14K</span> en YouTube · <span data-seg="fb.lacosa">172K</span> en Facebook · <span data-seg="ig.lacosa">31K</span> en Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.welcometoapagonia.com" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/welcome.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_welcome.jpg')); ?>" alt="Welcome to Apagonia"><div><h3>Welcome to Apagonia</h3><p>Serie de comedia situacional. Próximamente.</p><span class="n"><span data-seg="yt.welcome">2.7K</span> en YouTube · <span data-seg="fb.welcome">1.7K</span> en Facebook · <span data-seg="ig.welcome">3.7K</span> en Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.elhomedelarisa.com" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/home.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_home.jpg')); ?>" alt="El Home de la Risa"><div><h3>El Home de la Risa</h3><p>La marca principal que agrupa todas nuestras producciones de humor. Lunes.</p><span class="n"><span data-seg="yt.elhome">3.2K</span> en YouTube · <span data-seg="fb.elhome">13K</span> en Facebook · <span data-seg="ig.elhome">1.7K</span> en Instagram</span></div></div>
      </a>
    </div>
  </div>
</section>


<section id="estrenos" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Estrenos</div>
    <h2>Lo último que salió en la red.</h2>
    <p class="lead">Los estrenos más recientes de nuestros canales de YouTube. Se actualiza solo con cada estreno.</p>
    <div class="ests" id="estrenos-lista"><p style="color:var(--mut)">Cargando los estrenos…</p></div>
  </div>
</section>
<script src="/estrenos.js" defer></script>

<section id="apps" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Apps</div>
    <h2>Nuestros shows, en tu teléfono.</h2>
    <p class="lead">Dos apps gratis con todos los capítulos, los estrenos de la semana y avisos cuando sale uno nuevo. Se instalan desde el navegador en cualquier teléfono, y en Android también como APK. Muy pronto en Google Play y App Store.</p>
    <div class="apps">
      <div class="app">
        <img src="<?php echo esc_url(get_theme_file_uri('img/marcas/elhome.png')); ?>" alt="El Home de la Risa">
        <div>
          <h3>El Home de la Risa</h3>
          <p>La casa del humor cubano: La Risa es Cosa Seria, La Cosa Es De Risa, Welcome to Apagonia y todos los shows, por capítulo y por humorista.</p>
          <div class="ctas">
            <a class="btn btn-acc" href="https://www.elhomedelarisa.com/" target="_blank" rel="noopener">Abrir la app</a>
            <a class="btn btn-ghost" href="https://marrerobernalmedia.com/apk/elhome.apk">Descargar para Android (APK)</a>
          </div>
        </div>
      </div>
      <div class="app">
        <img src="<?php echo esc_url(get_theme_file_uri('img/marcas/pelotero.png?v=2')); ?>" alt="Recta Al Pecho">
        <div>
          <h3>Recta Al Pecho</h3>
          <p>Béisbol sin filtro: las entrevistas, las series Las Fugas y Los Borrados, los mitos con su respuesta y las noticias de rectaalpecho.com.</p>
          <div class="ctas">
            <a class="btn btn-acc" href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">Abrir la app</a>
            <a class="btn btn-ghost" href="https://marrerobernalmedia.com/apk/recta.apk">Descargar para Android (APK)</a>
          </div>
        </div>
      </div>
    </div>
    <p style="color:var(--mut);font-size:13px;margin-top:16px">Para instalarla desde el navegador: abre la app, toca Compartir (iPhone) o el menú ⋮ (Android) y elige "Añadir a pantalla de inicio". El APK requiere permitir la instalación de apps de origen conocido.</p>
  </div>
</section>

<section id="servicios" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Servicios</div>
    <h2>Lo que producimos para marcas y empresas.</h2>
    <p class="lead">El mismo equipo y el mismo estándar con que producimos nuestros shows, al servicio de tu marca.</p>
    <div class="works svc">
      <a class="wk big" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/comerciales.jpg')); ?>)" href="https://www.youtube.com/@marrerobernalmedia?sub_confirmation=1" target="_blank" rel="noopener"><div><b>Filmación de comerciales y video corporativo</b><span>Spots para TV, redes y pantallas, videos de marca y testimoniales · ver comerciales en nuestro canal →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/ia.jpg')); ?>)" href="https://youtu.be/9dn14JcyVl0" target="_blank" rel="noopener"><div><b>Animación y producción visual con IA</b><span>Escenarios, personajes animados y gráficos profesionales generados con IA para comerciales y redes · mira el comercial de MLB Kids Seven →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/dron.jpg')); ?>)" href="#dron"><div><b>Filmación aérea con dron</b><span>Piloto certificado por la FAA (Part 107) · bienes raíces, construcción, eventos corporativos y producciones →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/web.jpg')); ?>)" href="#contacto"><div><b>Páginas web y apps para clientes</b><span>Sitios rápidos, bilingües y apps con notificaciones · pide tu propuesta →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/identidad.jpg')); ?>)" href="#contacto"><div><b>Diseño e identidad corporativa</b><span>Logos, manual de marca, papelería y redes · pide tu propuesta →</span></div></a>
    </div>
    <h3 style="margin-top:40px;font-size:18px">Y además</h3>
    <div class="sv-grid">
      <div class="sv"><div class="ic">✂️</div><h3>Edición y postproducción</h3><p>Montaje, corrección de color, diseño sonoro, subtítulos y versiones verticales para cada plataforma.</p></div>
      <div class="sv"><div class="ic">🎙️</div><h3>Podcast y streaming para marcas</h3><p>Diseño del formato, grabación en set, producción y distribución. Recta Al Pecho es nuestro propio caso de éxito.</p></div>
      <div class="sv"><div class="ic">📈</div><h3>Contenido y gestión de canales</h3><p>Optimización y crecimiento de canales de YouTube: estrategia, calendario, empaque (títulos, miniaturas, SEO) y publicación en YouTube, Facebook e Instagram.</p></div>
      <div class="sv"><div class="ic">📷</div><h3>Fotografía profesional</h3><p>Producto, retratos corporativos, eventos y bienes raíces. Combínala con tomas de dron para un paquete completo.</p></div>
      <div class="sv"><div class="ic">🎥</div><h3>Cobertura de eventos multicámara</h3><p>Conferencias, lanzamientos y shows con público, grabados con varias cámaras y sonido profesional, como grabamos nuestros propios shows.</p></div>
      <div class="sv"><div class="ic">🌎</div><h3>Contenido bilingüe</h3><p>Traducción, subtítulos y locución en español e inglés para que tu video llegue a los dos públicos de Las Vegas y de todo EE. UU.</p></div>
      <div class="sv"><div class="ic">📣</div><h3>Publicidad dentro de la red</h3><p>Tu marca dentro de nuestros shows: menciones, carteles en pantalla, segmentos patrocinados y colaboraciones.</p></div>
    </div>
  </div>
</section>

<section id="dron" class="band">
  <div class="wrap">
    <div>
      <div class="kicker">Filmación con dron</div>
      <h2>Tomas aéreas legales, seguras y con calidad de cine.</h2>
      <p class="lead">Nuestro productor es piloto remoto certificado por la FAA (Part 107). Volamos dentro de las reglas federales, estatales y locales, de día o de noche, con los permisos sacados y el vuelo planificado de antemano, para que tu proyecto no tenga sorpresas.</p>
      <ul class="list">
        <li>Certificado de piloto remoto FAA Part 107 vigente, con su capacitación periódica al día.</li>
        <li>Dron registrado en la FAA y con identificación remota (Remote ID).</li>
        <li>Vuelos de día y también de noche, como permite la Part 107, con luces anticolisión visibles a 3 millas.</li>
        <li>Permisos tramitados de antemano: autorización de espacio aéreo controlado (LAANC o FAA DroneZone), permiso de filmación de la ciudad o del condado cuando hace falta y autorización escrita del dueño del lugar.</li>
        <li>Altura máxima según el mapa de la FAA: cerca de los aeropuertos el techo autorizado baja (de 400 pies hasta 0), y zonas como bases militares, presas, parques nacionales e instalaciones críticas piden permiso especial, que tramitamos antes de la fecha.</li>
        <li>Plan de vuelo y revisión de clima, restricciones temporales (TFR) y seguridad del equipo y del público antes de cada vuelo.</li>
        <li>Bienes raíces, construcción y avance de obra, eventos corporativos, comerciales, turismo y producciones de video.</li>
      </ul>
      <div class="ctas" style="margin-top:28px"><a class="btn btn-acc" href="#contacto">Pedir propuesta</a></div>
    </div>
    <img src="<?php echo esc_url(get_theme_file_uri('img/dron.jpg')); ?>" alt="Filmación aérea con dron en Las Vegas">
  </div>
</section>

<section id="publicidad" class="band">
  <div class="wrap">
    <div>
      <div class="kicker">Publicidad en la red</div>
      <h2>Llega al público latino donde ya está mirando.</h2>
      <p class="lead">Un espacio en nuestros programas no es un anuncio que se salta: es parte del show. Nuestras páginas suman más de <span data-seg="tot.todo" data-fmt="mil">1,080,000</span> seguidores: <span data-seg="tot.fbRed" data-fmt="mil">846,000</span> en Facebook, <span data-seg="tot.igRed" data-fmt="mil">106,000</span> en Instagram y <span data-seg="tot.ytRed" data-fmt="mil">130,000</span> suscriptores en YouTube. La Risa es Cosa Seria <span data-seg="fb.larisa" data-fmt="full">584,344</span> en Facebook y <span data-seg="ig.larisa" data-fmt="full">50,500</span> en Instagram · La Cosa Es De Risa <span data-seg="fb.lacosa" data-fmt="full">172,454</span> y <span data-seg="ig.lacosa" data-fmt="full">31,300</span> · Recta Al Pecho <span data-seg="fb.recta" data-fmt="full">71,612</span> y <span data-seg="ig.recta" data-fmt="full">9,202</span> · Marrero Bernal Media <span data-seg="ig.mbm" data-fmt="full">10,100</span> en Instagram. <small style="opacity:.6">Cifras actualizadas el <span data-seg="actualizado">2026-10-30</span>.</small> Cada semana los estrenos llegan a decenas de miles de hogares cubanos y latinos en Estados Unidos.</p>
      <ul class="list">
        <li>Carteles y menciones integradas en los capítulos de La Risa, Recta Al Pecho y el noticiero.</li>
        <li>Segmentos patrocinados y colaboraciones en Facebook e Instagram con nuestras páginas.</li>
        <li>Producción del anuncio incluida: lo hacemos nosotros, con el estilo del programa.</li>
        <li>Reporte de resultados con los datos reales de cada plataforma.</li>
      </ul>
      <div class="ctas" style="margin-top:28px"><a class="btn btn-acc" href="#contacto">Pedir propuesta</a></div>
    </div>
    <img src="<?php echo esc_url(get_theme_file_uri('img/recta.jpg')); ?>" alt="Recta Al Pecho">
  </div>
</section>


<section id="facebook" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Nuestras páginas en Facebook</div>
    <h2>Diez páginas, una sola red.</h2>
    <p class="lead">Cada página tiene su público y su tono. Tu campaña puede salir en una, en varias o en todas a la vez, con la producción hecha por nosotros.</p>
    <div class="fb-grid">
      <a class="fb" href="https://www.facebook.com/RisaEsCosaSeria/" target="_blank" rel="noopener" data-fb="larisa"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_larisa.jpg')); ?>" alt="La Risa es Cosa Seria"><b>La Risa es Cosa Seria</b><span><i data-seg="fb.larisa" data-fmt="full">584,344</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/LaCosaEsDeRisa/" target="_blank" rel="noopener" data-fb="lacosa"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_lacosa.jpg')); ?>" alt="La Cosa Es De Risa"><b>La Cosa Es De Risa</b><span><i data-seg="fb.lacosa" data-fmt="full">172,454</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/RectaAlPecho/" target="_blank" rel="noopener" data-fb="recta"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/pelotero.png?v=2')); ?>" alt="Recta al Pecho"><b>Recta al Pecho</b><span><i data-seg="fb.recta" data-fmt="full">71,612</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/ElHomeDeLaRisa/" target="_blank" rel="noopener" data-fb="elhome"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/elhome.png')); ?>" alt="El Home de la Risa"><b>El Home De La Risa</b><span><i data-seg="fb.elhome" data-fmt="full">13,236</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/eliam" target="_blank" rel="noopener" data-fb="eliam"><img src="<?php echo esc_url(get_theme_file_uri('img/av_eliam.jpg?v=2')); ?>" alt="Eliam Marrero Bernal" style="border-radius:50%"><b>Eliam M. Marrero Bernal</b><span><i data-seg="fb.eliam" data-fmt="full">11,223</i> seguidores · nuestro fundador</span></a>
      <a class="fb" href="https://www.facebook.com/sidecuerosetrata" target="_blank" rel="noopener" data-fb="cuero"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/cuero.png')); ?>" alt="Si de Cuero Se Trata"><b>Si de Cuero se Trata</b><span><i data-seg="fb.cuero" data-fmt="full">2,106</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/apagonia" target="_blank" rel="noopener" data-fb="welcome"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_welcome.jpg')); ?>" alt="Welcome to Apagonia"><b>Welcome to Apagonia</b><span><i data-seg="fb.welcome" data-fmt="full">1,729</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/marrerobernalmedia/" target="_blank" rel="noopener" data-fb="mbm"><img src="<?php echo esc_url(get_theme_file_uri('img/mbm-iso.svg')); ?>" alt="Marrero Bernal Media"><b>Marrero Bernal Media</b><span><i data-seg="fb.mbm" data-fmt="full">1,325</i> seguidores</span></a>
      <a class="fb" href="https://www.facebook.com/aquinoserienadie/" target="_blank" rel="noopener" data-fb="nadie"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/ansn.jpg')); ?>" alt="Aquí No Se Ríe Nadie" style="border-radius:10px"><b>Aquí No Se Ríe Nadie</b><span><i data-seg="fb.nadie" data-fmt="full">263</i> seguidores · estreno primavera 2027</span></a>
      <a class="fb" href="https://www.facebook.com/marrerobernal" target="_blank" rel="noopener" data-fb="mba"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_mba.png')); ?>" alt="Marrero Bernal & Associates"><b>Marrero Bernal &amp; Associates</b><span><i data-seg="fb.mba" data-fmt="full">5,214</i> seguidores · patrocinador</span></a>
    </div>
    <p style="color:var(--mut);font-size:13px;margin-top:18px">Total en Facebook: <b style="color:var(--fg)"><span data-seg="tot.fbTodo" data-fmt="full">863,243</span></b> seguidores, más <span data-seg="tot.igTodo" data-fmt="full">113,887</span> en Instagram.</p>
  </div>
</section>

<section id="trabajos">
  <div class="wrap">
    <div class="kicker">Nuestras producciones</div>
    <h2>Shows y formatos propios de la casa.</h2>
    <div class="works">
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/risa.jpg')); ?>)" href="https://www.youtube.com/@LaRisaEsCosaSeria?sub_confirmation=1" target="_blank" rel="noopener"><div><b>La Risa es Cosa Seria</b><span>Serie de stand-up · producción completa</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/welcome.jpg')); ?>)" href="https://www.welcometoapagonia.com" target="_blank" rel="noopener"><div><b>Welcome to Apagonia · Próximamente</b><span>Serie de comedia situacional · guion, dirección y post</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/recta.jpg')); ?>)" href="https://www.youtube.com/@RectaAlPecho?sub_confirmation=1" target="_blank" rel="noopener"><div><b>Recta Al Pecho</b><span>Programa de entrevistas · set, grabación y distribución</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/cosa.jpg')); ?>)" href="https://www.lcedr.com" target="_blank" rel="noopener"><div><b>La Cosa Es De Risa</b><span>Apagonia Hoy, el noticiero, y los segmentos de Bacallao Sin Pan, el Despingovery y más · formato propio</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/home.jpg')); ?>)" href="https://www.elhomedelarisa.com" target="_blank" rel="noopener"><div><b>El Home de la Risa</b><span>La marca que agrupa todas nuestras producciones de humor</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/cuero.jpg')); ?>)" href="https://www.lcedr.com" target="_blank" rel="noopener"><div><b>Si de Cuero se Trata · Estreno 18 de diciembre</b><span>El roast cubano · formato propio</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/ansn.jpg')); ?>)" href="https://www.facebook.com/aquinoserienadie/" target="_blank" rel="noopener"><div><b>Aquí No Se Ríe Nadie · Primavera 2027</b><span>El duelo cubano: el que se ríe, toma · formato propio</span></div></a>
    </div>
  </div>
</section>

<section id="nosotros" class="about" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="marcas">
      <a href="https://www.youtube.com/@LaRisaEsCosaSeria?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/larisa.png')); ?>" alt="La Risa es Cosa Seria"></a><a href="https://www.youtube.com/@RectaAlPecho?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/recta.png')); ?>" alt="Recta Al Pecho"></a><a href="https://www.youtube.com/channel/UCsLPvvD_UDgwo91eeUOZUSQ?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/lacosa.png')); ?>" alt="La Cosa Es De Risa"></a><a href="https://www.youtube.com/channel/UCtf5fq1TdwirbFswJfZSWCA?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/welcome.png')); ?>" alt="Welcome to Apagonia"></a><a href="https://www.youtube.com/@marrerobernalmedia?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/mbentv.png')); ?>" alt="MB en TV · tráileres de Marrero Bernal Media"></a><a href="https://www.youtube.com/channel/UCItBxtE_Ky-C7Q3IfvC5ZMg?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/cuero.png')); ?>" alt="Si de Cuero se Trata"></a>
    </div>
    <div>
      <div class="kicker">Nosotros</div>
      <h2>Una productora con la mirada de un director.</h2>
      <p class="lead">Marrero Bernal Media LLC nace en Las Vegas con <a href="https://www.imdb.com/name/nm3952887/" target="_blank" rel="noopener" style="text-decoration:underline;text-underline-offset:3px">Eliam Marrero Bernal</a> como productor: director y director de fotografía con créditos en cine y televisión. Lo que empezó como un canal de humor cubano es hoy una red de cinco canales, siete páginas en Meta y un equipo de producción que estrena contenido todas las semanas del año.</p>
      <p class="lead" style="margin-top:14px">Trabajamos con el mismo rigor para un capítulo de nuestra serie que para el comercial de un cliente: guion, luz, sonido, ritmo y, sobre todo, saber a quién le hablamos.</p>
      <div class="creds">
        <span>Dirección y fotografía</span><a href="https://www.imdb.com/name/nm3952887/" target="_blank" rel="noopener"><span>Créditos en IMDb ↗</span></a><span>Piloto FAA Part 107</span><span>Las Vegas · Miami</span><span>Español e inglés</span>
      </div>
    </div>
  </div>
</section>

<section id="proceso">
  <div class="wrap">
    <div class="kicker">Cómo trabajamos</div>
    <h2>Del primer mensaje a la entrega.</h2>
    <div class="steps">
      <div class="step"><h3>Escuchamos</h3><p>Nos cuentas qué necesitas y a quién quieres llegar. Sin formularios eternos: una llamada basta.</p></div>
      <div class="step"><h3>Proponemos</h3><p>Recibes una propuesta clara con formato, alcance, calendario y presupuesto cerrado.</p></div>
      <div class="step"><h3>Producimos</h3><p>Guion, rodaje, dron, edición y diseño con nuestro equipo. Tú apruebas cada etapa.</p></div>
      <div class="step"><h3>Entregamos y distribuimos</h3><p>Versiones para cada plataforma y, si lo quieres, difusión dentro de nuestra red con reporte de resultados.</p></div>
    </div>
  </div>
</section>

<section id="contacto" class="contact">
  <div class="wrap">
    <div class="cinfo">
      <div class="kicker">Contacto</div>
      <h2>Cuéntanos tu proyecto.</h2>
      <p>Respondemos en menos de un día hábil.</p>
      <a href="mailto:info@marrerobernalmedia.com">info@marrerobernalmedia.com</a>
      <p>Las Vegas, Nevada · producciones en todo Estados Unidos</p>
      <p style="margin-top:22px">YouTube · Facebook · Instagram · TikTok · X: <b style="color:var(--fg)">@marrerobernalmedia</b></p>
    </div>
    <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="mbm_contacto"><?php wp_nonce_field('mbm_contacto','mbm_n'); ?><input type="text" name="sitio" style="display:none" tabindex="-1" autocomplete="off">
      <input name="nombre" placeholder="Nombre" required>
      <input name="empresa" placeholder="Empresa">
      <input type="email" name="correo" placeholder="Correo" required>
      <input name="telefono" placeholder="Teléfono o WhatsApp">
      <select name="servicio"><option>¿Qué necesitas?</option><option>Comercial o video corporativo</option><option>Edición y postproducción</option><option>Filmación con dron</option><option>Fotografía</option><option>Cobertura de evento</option><option>Traducción, subtítulos o locución</option><option>Animación con IA</option><option>Podcast o streaming</option><option>Diseño e identidad corporativa</option><option>Página web o app</option><option>Gestión de canales</option><option>Publicidad en la red</option></select>
      <textarea name="mensaje" placeholder="Cuéntanos brevemente el proyecto"></textarea>
      <button class="btn btn-acc" type="submit" style="justify-self:start">Enviar</button>
      <?php if (isset($_GET['enviado'])): ?><div class="ok">✅ Recibido. Respondemos en menos de un día hábil.</div><?php elseif (isset($_GET['error'])): ?><div class="ok" style="background:#3a1a1a;color:#ffb4b4">No se pudo enviar. Escríbenos a info@marrerobernalmedia.com.</div><?php endif; ?>
    </form>
  </div>
</section>


<?php get_footer(); ?>
