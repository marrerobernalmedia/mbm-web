<?php get_header(); ?>
<section class="hero">
  <div class="wrap">
    <div>
      <div class="kicker">North Las Vegas · desde 2008</div>
      <h1>Seguros, taxes e inmigración, <em>en tu idioma</em> y en un solo lugar.</h1>
      <p class="lead">Somos una agencia de seguros independiente con contratos con múltiples compañías de primer nivel, como Farmers y Progressive, además de preparadores de impuestos y especialistas en trámites. Diecisiete años atendiendo a la comunidad hispana de Nevada, California y Arizona.</p>
      <div class="search" id="search">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5" stroke-linecap="round"/></svg>
        <input id="q" type="search" placeholder="¿Qué necesitas? Ej. seguro de auto, Medicare, LLC, notaría…" autocomplete="off">
        <button type="button">Buscar</button>
        <div class="sugg" id="sugg"></div>
      </div>
      <div class="pop">Lo más buscado:
        <a href="#s-auto">Seguro de auto</a><a href="#s-medicare">Medicare Advantage</a><a href="#s-taxes">Taxes personales</a><a href="#s-llc">Crear una LLC</a><a href="#s-inmigracion">Inmigración</a><a href="#s-notaria">Notaría</a>
      </div>
      <div class="badges"><span>Licencia NV · CA · AZ</span><span>Agencia independiente · 10 aseguradoras</span><span>Español e inglés</span><span>Cotización sin costo</span></div>
    </div>
    <div class="heroimg" style="background:url(<?php echo esc_url(get_theme_file_uri('img/eliam-retrato.jpg')); ?>) center/cover">
      <div><span class="lab">Eliam Marrero Bernal · fundador</span><b>Te atendemos como a familia.</b></div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="tiles">
    <a class="tile" href="#personal"><div class="ic">🚗</div><b>Seguros personales</b><span>Auto, hogar, vida, mascotas, dispositivos y más</span></a>
    <a class="tile" href="#negocios"><div class="ic">🏢</div><b>Seguros de negocio</b><span>Responsabilidad, auto comercial, workers' comp</span></a>
    <a class="tile" href="#s-taxes"><div class="ic">🧾</div><b>Taxes</b><span>Personales y de negocio, todo el año</span></a>
    <a class="tile" href="#s-inmigracion"><div class="ic">🛂</div><b>Inmigración</b><span>Formularios y trámites con USCIS</span></a>
    <a class="tile" href="#s-notaria"><div class="ic">✒️</div><b>Notaría y traducciones</b><span>Documentos certificados en español e inglés</span></a>
    <a class="tile" href="#s-llc"><div class="ic">📑</div><b>Licencias y LLC</b><span>Abre tu negocio en Nevada</span></a>
  </div>
  <div class="carriers"><span>Trabajamos con</span><b>Farmers</b><b>Progressive</b><b>Travelers</b><b>Liberty Mutual</b><b>Mercury</b><b>National General</b><b>Bristol West</b><b>Foremost</b><b>Homeowners of America</b><b>Lemonade</b></div>
  <div class="cli">
    <a class="cli-card" href="https://marrerobernal.securefilepro.com/portal/#/login" target="_blank" rel="noopener"><div class="ic">🔐</div><div><b>Acceso de clientes</b><span>Entra al portal seguro para subir y descargar tus documentos (SecureFilePro).</span></div><em>Entrar →</em></a>
    <a class="cli-card" href="https://55a7805c-ea2c-4f0e-951b-1aa3c932e857.paylinks.godaddy.com" target="_blank" rel="noopener"><div class="ic">💳</div><div><b>Pagar en línea</b><span>Paga tu servicio con tarjeta de forma segura, desde el teléfono o la computadora.</span></div><em>Pagar →</em></a>
  </div>
  <div class="quote" id="cotizar">
    <div><div class="kicker" style="margin-bottom:6px">Cotiza en línea</div><h3>Tu cotización llega directo a nuestra oficina.</h3><p>Cinco minutos, sin llamadas. La revisamos y te contactamos con la mejor opción.</p></div>
    <div class="qbtns">
      <a href="https://esales.farmers.com/fastquote?Lob=Auto&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">🚗 Auto</a>
      <a href="https://esales.farmers.com/fastquote?Lob=Home&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">🏠 Casa</a>
      <a href="https://esales.farmers.com/fastquote?Lob=Condo&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">🏢 Condominio</a>
      <a href="https://esales.farmers.com/fastquote?Lob=Renter&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">🔑 Renters</a>
      <a href="https://esales.farmers.com/fastquote?Lob=Lifec&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">❤️ Vida</a>
      <a href="https://esales.farmers.com/fastquote?Lob=Business&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">💼 Negocio</a>
      <a href="https://esales.farmers.com/fastquote?Lob=autoHome&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">🚗+🏠 Auto + casa</a>
      <a href="https://esales.farmers.com/fastquote?Lob=autoRenter&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">🚗+🔑 Auto + renters</a>
      <a href="https://farmers.bordersolutions.com/ap.php?a=67249W" target="_blank" rel="noopener">🇲🇽 Auto para México</a>
    </div>
  </div>
</div>

<section class="svc" id="personal">
  <div class="wrap">
    <div class="kicker">Índice de servicios</div>
    <h2>Todo lo que hacemos, en una sola página.</h2>
    <p class="lead">Cada servicio tiene su propia página con lo que necesitas traer, cuánto demora y preguntas frecuentes. Haz clic y entérate antes de llamar.</p>
    <div class="cols">
      <div class="card">
        <img class="cimg" style="object-position:40% 55%" src="<?php echo esc_url(get_theme_file_uri('img/familia.jpg')); ?>" alt="Familia frente a su casa y su auto en North Las Vegas" width="1280" height="720" loading="lazy">
        <h3>Personal</h3>
        <div class="sub">Para ti y tu familia</div>
        <div class="grp"><b>Vehículos</b><ul><li><a id="s-auto" href="https://esales.farmers.com/fastquote?Lob=Auto&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Auto · cotizar</a></li><li><a href="https://www.farmers.com/motorcycle/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Motocicleta</a></li><li><a href="https://www.farmers.com/recreational/boat-and-watercraft-insurance/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Bote y jet ski</a></li><li><a href="https://www.farmers.com/auto/collectible/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Autos clásicos</a></li><li><a href="https://www.farmers.com/recreational/offroad-vehicle/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">ATV y off-road</a></li><li><a href="https://www.farmers.com/recreational/motor-home/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">RV y casa rodante</a></li></ul></div>
        <div class="grp"><b>Propiedad</b><ul><li><a href="https://esales.farmers.com/fastquote?Lob=Home&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Casa · cotizar</a></li><li><a href="https://esales.farmers.com/fastquote?Lob=Condo&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Condominio · cotizar</a></li><li><a href="https://esales.farmers.com/fastquote?Lob=Renter&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Renters · cotizar</a></li><li><a href="https://www.farmers.com/landlord-rental-properties/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Landlord</a></li><li><a href="https://www.farmers.com/home/mobile-manufactured/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Casa móvil</a></li><li><a href="https://www.farmers.com/home/seasonal-vacation-homes/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Casa de vacaciones</a></li><li><a href="https://www.farmers.com/home/flood/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Inundación</a></li><li><a href="https://www.farmers.com/home/earthquake/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Terremoto</a></li></ul></div>
        <div class="grp"><b>Vida y salud</b><ul><li><a href="https://esales.farmers.com/fastquote?Lob=Lifec&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Vida · cotizar</a></li><li><a href="https://www.farmers.com/life-insurance/coverage/term-life/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Vida a término</a></li><li><a href="https://www.farmers.com/life-insurance/coverage/whole-life/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Vida entera</a></li><li><a href="https://www.farmers.com/life-insurance/coverage/universal-life/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Vida universal</a></li><li><a id="s-medicare" href="#medicare">Medicare Advantage</a></li><li><a href="https://www.farmers.com/medicare-plans/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Planes Medicare (Farmers)</a></li></ul></div>
        <div class="grp"><b>Otros seguros</b><ul><li><a href="https://www.farmers.com/umbrella/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Umbrella</a></li><li><a href="https://www.farmers.com/pet-insurance/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Mascotas</a></li><li><a href="https://www.farmers.com/electronic-device-insurance/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Dispositivos electrónicos</a></li><li><a href="https://esales.farmers.com/fastquote?Lob=autoHome&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Paquete auto + casa · cotizar</a></li><li><a href="https://esales.farmers.com/fastquote?Lob=autoRenter&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Paquete auto + renters · cotizar</a></li><li><a href="https://farmers.bordersolutions.com/ap.php?a=67249W" target="_blank" rel="noopener">Auto para manejar en México · cotizar</a></li></ul></div>
        <div class="grp"><b>Trámites</b><ul><li><a id="s-taxes" href="#contacto">Taxes personales</a></li><li><a href="#irs">E-file directo al IRS</a></li><li><a href="#irs">Número ITIN (Agente Certificada CAA)</a></li><li><a id="s-inmigracion" href="#contacto">Inmigración</a></li><li><a id="s-notaria" href="#contacto">Notaría</a></li><li><a href="#contacto">Traducciones certificadas</a></li><li><a href="#contacto">Revisión gratuita de coberturas</a></li></ul></div>
        <p class="note">Seguros con múltiples compañías de primer nivel, entre ellas Farmers y Progressive. La disponibilidad de coberturas varía por compañía y por estado.</p>
      </div>
      <div class="card" id="negocios">
        <img class="cimg" style="object-position:70% 12%" src="<?php echo esc_url(get_theme_file_uri('img/negocio.jpg')); ?>" alt="Dueño de un negocio en su local" width="1280" height="720" loading="lazy">
        <h3>Negocios</h3>
        <div class="sub">Para tu empresa, desde el primer día</div>
        <div class="grp"><b>Seguros comerciales</b><ul><li><a href="https://esales.farmers.com/fastquote?Lob=Business&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032" target="_blank" rel="noopener">Seguro de negocio · cotizar</a></li><li><a href="https://www.farmers.com/business/auto-insurance/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Auto comercial</a></li><li><a href="https://www.farmers.com/business/property/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Propiedad comercial</a></li><li><a href="https://www.farmers.com/business/general-liability-insurance/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Responsabilidad civil</a></li><li><a href="https://www.farmers.com/business/workers-compensation/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Workers' compensation</a></li><li><a href="https://www.farmers.com/business/industry/?Agent_Code=67249W%2430306E%248833H2&Source_Indicator=AP" target="_blank" rel="noopener">Por industria</a></li></ul></div>
        <div class="grp"><b>Impuestos y formación</b><ul><li><a href="#contacto">Taxes de negocio</a></li><li><a href="#contacto">Licencias de negocio</a></li><li><a id="s-llc" href="#contacto">Creación de LLC</a></li><li><a href="#contacto">EIN y registro estatal</a></li></ul></div>
        <div class="grp"><b>Industrias que atendemos</b><ul><li><a href="#contacto">Restaurantes</a></li><li><a href="#contacto">Construcción</a></li><li><a href="#contacto">Transporte</a></li><li><a href="#contacto">Limpieza</a></li><li><a href="#contacto">Salones y barberías</a></li><li><a href="#contacto">Tiendas</a></li></ul></div>
        <div style="margin-top:26px;padding:18px;background:var(--cream);border-radius:14px">
          <b style="display:block;margin-bottom:4px">¿Vas a abrir tu negocio?</b>
          <span style="font-size:14px;color:var(--mut)">Te formamos la LLC, sacamos la licencia y dejamos el seguro listo en una sola visita.</span>
          <div style="margin-top:12px"><a class="btn btn-navy" href="#contacto">Hablar con un asesor</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker">Por qué nosotros</div>
    <h2>Diecisiete años, la misma oficina, la misma gente.</h2>
    <div class="why">
      <div><b>2008</b><p>Año en que abrimos en North Las Vegas. Seguimos en el mismo lugar.</p></div>
      <div><b>3 estados</b><p>Licencia para vender seguros en Nevada, California y Arizona.</p></div>
      <div><b>10 compañías</b><p>Somos independientes. En auto cotizamos con Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General y Bristol West; en casa, con Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America y Lemonade. Te damos la mejor opción.</p></div>
      <div><b>1 visita</b><p>Seguro, taxes, inmigración y notaría en la misma oficina, en español.</p></div>
    </div>
    <div class="resenas">
      <h3>Lo que dicen nuestros clientes en Google</h3>
      <div class="ti"><?php echo do_shortcode('[trustindex no-registration=google]'); ?></div>
      <div class="premios">
        <img src="<?php echo esc_url(get_theme_file_uri('img/threebest.svg')); ?>" alt="Three Best Rated: mejores agentes de seguros en North Las Vegas 2024" width="200" height="200" loading="lazy">
        <a class="wh" href="https://wallethub.com/profile/eliam-bernal-67214649i#reviews" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/wallethub-best.svg')); ?>" alt="WalletHub Best Award: mejor agente de seguros" width="120" height="181" loading="lazy"><span><b>Mejor agente de seguros en Las Vegas</b><small>según WalletHub · 4.8 ★ · 81 reseñas</small></span></a>
      </div>
    </div>
  </div>
</section>

<section class="med" id="medicare">
  <div class="wrap">
    <div>
      <div class="kicker">Seguros de salud</div>
      <h2>Medicare Advantage, explicado sin letra pequeña.</h2>
      <p class="lead">Si tienes 65 años o más, o calificas por discapacidad, te ayudamos a comparar planes Medicare Advantage disponibles en tu condado y a entender qué cubre cada uno: médico, hospital, medicinas, dental, visión y más.</p>
      <ul>
        <li>Revisión gratuita de tu plan actual, sin compromiso.</li>
        <li>Inscripción anual del 15 de octubre al 7 de diciembre.</li>
        <li>Atención en español durante todo el año, no solo en temporada.</li>
      </ul>
      <div style="margin-top:26px"><a class="btn btn-acc" href="#contacto">Revisar mi plan</a></div>
    </div>
    <div>
    <img class="mimg" src="<?php echo esc_url(get_theme_file_uri('img/medicare.jpg')); ?>" alt="Pareja mayor revisando su plan de salud en casa" width="1280" height="720" loading="lazy">
    <div class="box">
      <h3>Antes de que llames, debes saber:</h3>
      <small>No ofrecemos todos los planes disponibles en su área. Cualquier información que proporcionemos se limita a los planes que ofrecemos en su área. Comuníquese con Medicare.gov o al 1-800-MEDICARE para obtener información sobre todas sus opciones.</small>
      <small>Marrero Bernal &amp; Associates es una agencia de seguros independiente con licencia y no está afiliada ni respaldada por el gobierno de EE. UU. ni por el programa federal Medicare.</small>
      <small>Las coberturas, primas y beneficios varían según el plan y el condado. Los textos finales se ajustan a la guía de mercadeo de CMS vigente.</small>
    </div>
    </div>
  </div>
</section>

<section class="irs" id="irs">
  <div class="wrap">
    <div class="kicker">Impuestos e ITIN</div>
    <h2>Tus taxes van directo al IRS. Sin intermediarios.</h2>
    <div class="irs-grid">
      <div class="card">
        <div class="ic">📡</div>
        <h3>Proveedor autorizado de e-file del IRS</h3>
        <p>Para conectarte a internet necesitas un proveedor de servicio que haga de intermediario. Con los taxes pasa lo mismo: muchas oficinas dependen de otra empresa para enviar tu declaración.</p>
        <p>Nosotros somos proveedor autorizado de e-file del IRS: transmitimos tu declaración directamente al IRS, sin intermediarios.</p>
        <div class="irs-pro">
          <b>¿Eres preparador de impuestos?</b>
          <span>Tú también puedes transmitir tus declaraciones al IRS a través de nosotros.</span>
          <a class="btn btn-navy" href="#contacto">Quiero transmitir con ustedes</a>
        </div>
      </div>
      <div class="card">
        <div class="ic">🪪</div>
        <h3>ITIN con Agente de Aceptación Certificada del IRS</h3>
        <p>Si solicitas el número ITIN por tu cuenta, tienes que enviar tus documentos originales al IRS por correo, como el pasaporte, y se pueden perder.</p>
        <p>En nuestro equipo tenemos una Agente de Aceptación Certificada (CAA) del IRS: ella revisa y certifica tus documentos aquí en la oficina y tú no tienes que mandar los originales.</p>
        <ul>
          <li>Solicitud del ITIN nueva o renovación.</li>
          <li>Tus documentos se quedan contigo.</li>
          <li>Te acompañamos hasta que llega tu número.</li>
        </ul>
        <a class="btn btn-acc" href="#contacto">Solicitar mi ITIN</a>
      </div>
    </div>
  </div>
</section>

<section class="about" id="nosotros">
  <div class="wrap">
    <img src="<?php echo esc_url(get_theme_file_uri('img/eliam.jpg')); ?>" alt="Eliam Marrero Bernal atendiendo clientes en la oficina" style="border-radius:22px;border:1px solid var(--line)">
    <div>
      <div class="kicker">Quiénes somos</div>
      <h2>Una agencia de barrio con licencia en tres estados.</h2>
      <p class="lead">Eliam Marrero Bernal fundó Marrero Bernal &amp; Associates en 2008 con una idea simple: que un cubano, un mexicano o un salvadoreño recién llegado a Las Vegas pudiera resolver su seguro, sus taxes y sus papeles con alguien que le hablara claro y en su idioma.</p>
      <p class="lead" style="margin-top:14px">Hoy somos una agencia independiente con contratos con varias compañías de primer nivel, preparadores de impuestos y un equipo que conoce a cada cliente por su nombre. Lo que ofrecemos no es un producto: es que salgas de la oficina con el problema resuelto.</p>
      <div class="creds"><span>Agencia independiente</span><span>LUTCF · FSCP · CSP</span><span><span data-seg="tot.mba">23K</span>+ seguidores en redes</span><span>Licencia NV · CA · AZ</span><span>The American College</span><span>Español · English</span></div>
    </div>
  </div>
</section>

<section style="background:var(--cream)">
  <div class="wrap">
    <div class="kicker">Cómo funciona</div>
    <h2>Resolver un trámite no tiene que ser un día perdido.</h2>
    <img class="simg" style="object-position:50% 15%" src="<?php echo esc_url(get_theme_file_uri('img/tramites.jpg')); ?>" alt="Clienta firmando sus documentos en la oficina" width="1280" height="720" loading="lazy">
    <div class="steps">
      <div class="step"><h3>Nos cuentas</h3><p>Por teléfono, WhatsApp o en la oficina. Sin cita para la mayoría de los trámites.</p></div>
      <div class="step"><h3>Te decimos qué traer</h3><p>Una lista corta y clara de documentos. Si falta algo, te ayudamos a conseguirlo.</p></div>
      <div class="step"><h3>Lo hacemos contigo</h3><p>Cotizamos, llenamos y revisamos todo delante de ti, en tu idioma.</p></div>
      <div class="step"><h3>Seguimos ahí</h3><p>Reclamos, renovaciones, cambios y preguntas: la misma oficina, la misma gente.</p></div>
    </div>
  </div>
</section>

<section class="contact" id="contacto">
  <div class="wrap">
    <div class="cinfo">
      <div class="kicker">Contacto</div>
      <h2>Ven, llama o escribe.</h2>
      <a class="big" href="tel:+18888772583">888-877-2583</a><div style="font-size:14px;color:var(--mut);margin:-4px 0 10px">888-87-SALUD · gratis desde cualquier estado · local 702-997-2982</div>
      <a class="wa" href="https://wa.me/17023027361" target="_blank" rel="noopener">💬 WhatsApp 702-302-7361</a>
      <p style="margin-top:16px"><b style="color:var(--ink)">3455 W Craig Rd, Suite D</b><br>North Las Vegas, NV 89032</p>
      <p>Lunes a viernes, 9:00 AM – 5:00 PM<br>Sábados y domingos cerrado</p>
      <div class="map"><iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=3455+W+Craig+Rd+Ste+D,+North+Las+Vegas,+NV+89032&output=embed" title="Mapa"></iframe></div>
    </div>
    <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="mba_contacto"><?php wp_nonce_field('mba_contacto','mba_n'); ?><input type="text" name="empresa" style="display:none" tabindex="-1" autocomplete="off">
      <b style="font-family:Fraunces,serif;font-size:22px">Pide tu cotización gratis</b>
      <input name="nombre" placeholder="Nombre" required>
      <input name="telefono" placeholder="Teléfono o WhatsApp" required>
      <input type="email" name="correo" placeholder="Correo (opcional)">
      <select name="servicio"><option>¿Qué necesitas?</option><option>Seguro de auto</option><option>Seguro de casa o renters</option><option>Seguro de vida</option><option>Medicare Advantage</option><option>Seguro de negocio</option><option>Taxes</option><option>Inmigración</option><option>Notaría o traducción</option><option>Licencia o LLC</option><option>Otro</option></select>
      <textarea name="mensaje" placeholder="Cuéntanos brevemente"></textarea>
      <button class="btn btn-navy" type="submit" style="justify-self:start">Enviar</button>
      <small>Respondemos el mismo día hábil. Nunca compartimos tus datos.</small>
      <?php if (isset($_GET['enviado'])): ?><div class="ok">✅ Recibido. Te contactamos el mismo día hábil.</div><?php elseif (isset($_GET['error'])): ?><div class="ok" style="background:#fdecec;color:#8a1f1f">No se pudo enviar. Llámanos al 888-877-2583.</div><?php endif; ?>
    </form>
  </div>
</section>


<?php get_footer(); ?>
