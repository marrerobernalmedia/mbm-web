<?php get_header('en'); ?>
<section class="hero">
  <div class="bg"></div>
  <div class="wrap">
    <div class="kicker">Video production company · Las Vegas</div>
    <h1>Stories that reach the heart of <em>our people</em>.</h1>
    <p class="lead">Marrero Bernal Media is a production company with deep experience in the Latino market. We produce, edit and distribute content, and with five YouTube channels and more than <span data-seg="tot.todo" data-fmt="mil">1,080,000</span> followers across Facebook, Instagram and YouTube, we don't just make your video: we know how to get it seen.</p>
    <div class="ctas">
      <a class="btn btn-acc" href="#contacto">Tell us about your project</a>
      <a class="btn btn-ghost" href="#red">Meet the network ↓</a>
    </div>
  </div>
</section>

<div class="stats">
  <div class="wrap">
    <div class="stat"><b>5</b><span>YOUTUBE CHANNELS</span></div>
    <div class="stat"><b>10</b><span>FACEBOOK PAGES</span></div>
    <div class="stat"><b>130K+</b><span>YOUTUBE SUBSCRIBERS</span></div>
    <div class="stat"><b>27M+</b><span>TOTAL VIEWS</span></div>
    <div class="stat"><b>4,500+</b><span>PIECES PUBLISHED</span></div>
    <div class="stat"><b data-seg="tot.todo" data-fmt="full" style="font-size:30px">1,083,324</b><span>SOCIAL FOLLOWERS · AS OF <span data-seg="actualizado">2026-10-30</span></span></div>
  </div>
</div>

<section id="red">
  <div class="wrap">
    <div class="kicker">The network</div>
    <h2>An audience of our own, built week after week.</h2>
    <p class="lead">Five YouTube channels with a fixed weekly premiere, plus Facebook and Instagram pages with more than <span data-seg="tot.metaRed" data-fmt="mil">950,000</span> followers. All produced in-house.</p>
    <div class="red-grid">
      <a class="ch" href="https://www.youtube.com/@LaRisaEsCosaSeria?sub_confirmation=1" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/risa.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_risa.jpg')); ?>" alt="La Risa es Cosa Seria"><div><h3>La Risa es Cosa Seria</h3><p>Cuban stand-up and comedy. New episodes Tuesdays and Fridays.</p><span class="n"><span data-seg="yt.larisa">91K</span> on YouTube · <span data-seg="fb.larisa">584K</span> on Facebook · <span data-seg="ig.larisa">50K</span> on Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.straight2dchest.com/" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/s2d.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_s2d.jpg')); ?>" alt="Straight 2D Chest"><div><h3>Straight 2D Chest</h3><p>Sports · Baseball is the passion: interviews with English audio.</p><span class="n"><span data-seg="yt.recta">19K</span> on YouTube · <span data-seg="fb.recta">71K</span> on Facebook · <span data-seg="ig.recta">9.2K</span> on Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.lcedr.com" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/cosa.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_cosa.jpg')); ?>" alt="La Cosa Es De Risa"><div><h3>La Cosa Es De Risa</h3><p>Apagonia's official newscast. Sundays.</p><span class="n"><span data-seg="yt.lacosa">14K</span> on YouTube · <span data-seg="fb.lacosa">172K</span> on Facebook · <span data-seg="ig.lacosa">31K</span> on Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.welcometoapagonia.com" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/welcome.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_welcome.jpg')); ?>" alt="Welcome to Apagonia"><div><h3>Welcome to Apagonia</h3><p>Sitcom series. Coming soon.</p><span class="n"><span data-seg="yt.welcome">2.7K</span> on YouTube · <span data-seg="fb.welcome">1.7K</span> on Facebook · <span data-seg="ig.welcome">3.7K</span> on Instagram</span></div></div>
      </a>
      <a class="ch" href="https://www.elhomedelarisa.com" target="_blank" rel="noopener">
        <div class="cover" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/home.jpg')); ?>)"></div>
        <div class="body"><img class="av" src="<?php echo esc_url(get_theme_file_uri('img/av_home.jpg')); ?>" alt="El Home de la Risa"><div><h3>El Home de la Risa</h3><p>The flagship brand that brings together all our comedy productions. Mondays.</p><span class="n"><span data-seg="yt.elhome">3.2K</span> on YouTube · <span data-seg="fb.elhome">13K</span> on Facebook · <span data-seg="ig.elhome">1.7K</span> on Instagram</span></div></div>
      </a>
    </div>
  </div>
</section>


<section id="estrenos" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Premieres</div>
    <h2>The latest from our network.</h2>
    <p class="lead">The newest premieres on our YouTube channels. Updated automatically with every release.</p>
    <div class="ests" id="estrenos-lista"><p style="color:var(--mut)">Loading premieres…</p></div>
  </div>
</section>
<script src="/estrenos.js" defer></script>

<section id="apps" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Apps</div>
    <h2>Our shows, on your phone.</h2>
    <p class="lead">Two free apps with every episode, the week's premieres and alerts when a new one drops. They install from the browser on any phone, and on Android also as an APK. Coming soon to Google Play and the App Store.</p>
    <div class="apps">
      <div class="app">
        <img src="<?php echo esc_url(get_theme_file_uri('img/marcas/elhome.png')); ?>" alt="El Home de la Risa">
        <div>
          <h3>El Home de la Risa</h3>
          <p>The home of Cuban humor: La Risa es Cosa Seria, La Cosa Es De Risa, Welcome to Apagonia and every show, by episode and by comedian.</p>
          <div class="ctas">
            <a class="btn btn-acc" href="https://www.elhomedelarisa.com/" target="_blank" rel="noopener">Open the app</a>
            <a class="btn btn-ghost" href="https://marrerobernalmedia.com/apk/elhome.apk">Download for Android (APK)</a>
          </div>
        </div>
      </div>
      <div class="app">
        <img src="<?php echo esc_url(get_theme_file_uri('img/marcas/pelotero.png?v=2')); ?>" alt="Straight 2D Chest">
        <div>
          <h3>Straight 2D Chest</h3>
          <p>Sports, with baseball as the passion: the interviews with English audio, the series, the myths with their answers and the stories from straight2dchest.com.</p>
          <div class="ctas">
            <a class="btn btn-acc" href="https://marrerobernalmedia.com/recta/?lang=en" target="_blank" rel="noopener">Open the app</a>
            <a class="btn btn-ghost" href="https://marrerobernalmedia.com/apk/recta.apk">Download for Android (APK)</a>
          </div>
        </div>
      </div>
    </div>
    <p style="color:var(--mut);font-size:13px;margin-top:16px">To install from the browser: open the app, tap Share (iPhone) or the ⋮ menu (Android) and choose "Add to Home Screen". The APK requires allowing installs from known sources.</p>
  </div>
</section>

<section id="servicios" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Services</div>
    <h2>What we produce for brands and businesses.</h2>
    <p class="lead">The same team and the same standard behind our own shows, working for your brand.</p>
    <div class="works svc">
      <a class="wk big" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/comerciales.jpg')); ?>)" href="https://www.youtube.com/@marrerobernalmedia?sub_confirmation=1" target="_blank" rel="noopener"><div><b>Commercial and corporate video production</b><span>TV, social and screen spots, brand videos and testimonials · see the commercials on our channel →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/ia.jpg')); ?>)" href="https://youtu.be/9dn14JcyVl0" target="_blank" rel="noopener"><div><b>AI animation and visual production</b><span>AI-generated sets, animated characters and professional graphics for commercials and social media · watch the MLB Kids Seven commercial →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/dron.jpg')); ?>)" href="#dron"><div><b>Aerial drone filming</b><span>FAA Part 107 certified pilot · real estate, construction, corporate events and productions →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/web.jpg')); ?>)" href="#contacto"><div><b>Websites and apps for clients</b><span>Fast bilingual websites and apps with notifications · request a proposal →</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/identidad.jpg')); ?>)" href="#contacto"><div><b>Design and corporate identity</b><span>Logos, brand guidelines, stationery and social media · request a proposal →</span></div></a>
    </div>
    <h3 style="margin-top:40px;font-size:18px">And also</h3>
    <div class="sv-grid">
      <div class="sv"><div class="ic">✂️</div><h3>Editing and post-production</h3><p>Editing, color grading, sound design, subtitles and vertical cuts for every platform.</p></div>
      <div class="sv"><div class="ic">🎙️</div><h3>Podcast and streaming for brands</h3><p>Format design, studio recording, production and distribution. Straight 2D Chest is our own success story.</p></div>
      <div class="sv"><div class="ic">📈</div><h3>Content and channel management</h3><p>YouTube channel optimization and growth: strategy, calendar, packaging (titles, thumbnails, SEO) and publishing on YouTube, Facebook and Instagram.</p></div>
      <div class="sv"><div class="ic">📷</div><h3>Professional photography</h3><p>Product, corporate portraits, events and real estate. Pair it with drone shots for a complete package.</p></div>
      <div class="sv"><div class="ic">🎥</div><h3>Multi-camera event coverage</h3><p>Conferences, launches and live-audience shows, shot with multiple cameras and professional sound, the way we record our own shows.</p></div>
      <div class="sv"><div class="ic">🌎</div><h3>Bilingual content</h3><p>Translation, subtitles and voice-over in Spanish and English so your video reaches both audiences in Las Vegas and across the U.S.</p></div>
      <div class="sv"><div class="ic">📣</div><h3>Advertising inside the network</h3><p>Your brand inside our shows: mentions, on-screen cards, sponsored segments and collaborations.</p></div>
    </div>
  </div>
</section>

<section id="dron" class="band">
  <div class="wrap">
    <div>
      <div class="kicker">Drone filming</div>
      <h2>Legal, safe aerial shots with cinema quality.</h2>
      <p class="lead">Our producer is an FAA-certified remote pilot (Part 107). We fly within federal, state and local rules, day or night, with permits secured and the flight planned in advance, so your project has no surprises.</p>
      <ul class="list">
        <li>Current FAA Part 107 remote pilot certificate, with recurrent training up to date.</li>
        <li>FAA-registered drone with Remote ID.</li>
        <li>Day and night flights, as Part 107 allows, with anti-collision lights visible for 3 miles.</li>
        <li>Permits handled in advance: controlled-airspace authorization (LAANC or FAA DroneZone), city or county film permits when required, and written permission from the property owner.</li>
        <li>Maximum altitude per the FAA map: near airports the authorized ceiling drops (from 400 feet down to 0), and areas such as military bases, dams, national parks and critical facilities need special permission, which we request before the shoot date.</li>
        <li>Flight plan and checks of weather, temporary flight restrictions (TFRs) and crew and public safety before every flight.</li>
        <li>Real estate, construction progress, corporate events, commercials, tourism and video productions.</li>
      </ul>
      <div class="ctas" style="margin-top:28px"><a class="btn btn-acc" href="#contacto">Request a proposal</a></div>
    </div>
    <img src="<?php echo esc_url(get_theme_file_uri('img/dron.jpg')); ?>" alt="Aerial drone filming in Las Vegas">
  </div>
</section>

<section id="publicidad" class="band">
  <div class="wrap">
    <div>
      <div class="kicker">Advertising on the network</div>
      <h2>Reach the Latino audience where it's already watching.</h2>
      <p class="lead">A spot in our programs isn't an ad to skip: it's part of the show. Our pages add up to more than <span data-seg="tot.todo" data-fmt="mil">1,080,000</span> followers: <span data-seg="tot.fbRed" data-fmt="mil">846,000</span> on Facebook, <span data-seg="tot.igRed" data-fmt="mil">106,000</span> on Instagram and <span data-seg="tot.ytRed" data-fmt="mil">130,000</span> YouTube subscribers. La Risa es Cosa Seria <span data-seg="fb.larisa" data-fmt="full">584,344</span> on Facebook and <span data-seg="ig.larisa" data-fmt="full">50,500</span> on Instagram · La Cosa Es De Risa <span data-seg="fb.lacosa" data-fmt="full">172,454</span> and <span data-seg="ig.lacosa" data-fmt="full">31,300</span> · Straight 2D Chest <span data-seg="fb.recta" data-fmt="full">71,612</span> and <span data-seg="ig.recta" data-fmt="full">9,202</span> · Marrero Bernal Media <span data-seg="ig.mbm" data-fmt="full">10,100</span> on Instagram. <small style="opacity:.6">Figures updated on <span data-seg="actualizado">2026-10-30</span>.</small> Every week our premieres reach tens of thousands of Cuban and Latino homes across the United States.</p>
      <ul class="list">
        <li>Cards and mentions integrated into episodes of La Risa, Straight 2D Chest and the newscast.</li>
        <li>Sponsored segments and Facebook/Instagram collaborations with our pages.</li>
        <li>Ad production included: we make it ourselves, in the show's own style.</li>
        <li>Results report with real data from each platform.</li>
      </ul>
      <div class="ctas" style="margin-top:28px"><a class="btn btn-acc" href="#contacto">Request a proposal</a></div>
    </div>
    <img src="<?php echo esc_url(get_theme_file_uri('img/recta.jpg')); ?>" alt="Straight 2D Chest">
  </div>
</section>


<section id="facebook" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="kicker">Our Facebook pages</div>
    <h2>Ten pages, one network.</h2>
    <p class="lead">Each page has its own audience and tone. Your campaign can run on one, several or all of them at once, with production done by us.</p>
    <div class="fb-grid">
      <a class="fb" href="https://www.facebook.com/RisaEsCosaSeria/" target="_blank" rel="noopener" data-fb="larisa"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_larisa.jpg')); ?>" alt="La Risa es Cosa Seria"><b>La Risa es Cosa Seria</b><span><i data-seg="fb.larisa" data-fmt="full">584,344</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/LaCosaEsDeRisa/" target="_blank" rel="noopener" data-fb="lacosa"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_lacosa.jpg')); ?>" alt="La Cosa Es De Risa"><b>La Cosa Es De Risa</b><span><i data-seg="fb.lacosa" data-fmt="full">172,454</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/RectaAlPecho/" target="_blank" rel="noopener" data-fb="recta"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/pelotero.png?v=2')); ?>" alt="Straight 2D Chest"><b>Straight 2D Chest</b><span><i data-seg="fb.recta" data-fmt="full">71,612</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/ElHomeDeLaRisa/" target="_blank" rel="noopener" data-fb="elhome"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/elhome.png')); ?>" alt="El Home de la Risa"><b>El Home De La Risa</b><span><i data-seg="fb.elhome" data-fmt="full">13,236</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/eliam" target="_blank" rel="noopener" data-fb="eliam"><img src="<?php echo esc_url(get_theme_file_uri('img/av_eliam.jpg?v=2')); ?>" alt="Eliam Marrero Bernal" style="border-radius:50%"><b>Eliam M. Marrero Bernal</b><span><i data-seg="fb.eliam" data-fmt="full">11,223</i> followers · our founder</span></a>
      <a class="fb" href="https://www.facebook.com/sidecuerosetrata" target="_blank" rel="noopener" data-fb="cuero"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/cuero.png')); ?>" alt="Si de Cuero Se Trata"><b>Si de Cuero se Trata</b><span><i data-seg="fb.cuero" data-fmt="full">2,106</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/apagonia" target="_blank" rel="noopener" data-fb="welcome"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_welcome.jpg')); ?>" alt="Welcome to Apagonia"><b>Welcome to Apagonia</b><span><i data-seg="fb.welcome" data-fmt="full">1,729</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/marrerobernalmedia/" target="_blank" rel="noopener" data-fb="mbm"><img src="<?php echo esc_url(get_theme_file_uri('img/mbm-iso.svg')); ?>" alt="Marrero Bernal Media"><b>Marrero Bernal Media</b><span><i data-seg="fb.mbm" data-fmt="full">1,325</i> followers</span></a>
      <a class="fb" href="https://www.facebook.com/aquinoserienadie/" target="_blank" rel="noopener" data-fb="nadie"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/ansn.jpg')); ?>" alt="Aquí No Se Ríe Nadie" style="border-radius:10px"><b>Aquí No Se Ríe Nadie</b><span><i data-seg="fb.nadie" data-fmt="full">263</i> followers · premieres spring 2027</span></a>
      <a class="fb" href="https://www.facebook.com/marrerobernal" target="_blank" rel="noopener" data-fb="mba"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/iso_mba.png')); ?>" alt="Marrero Bernal & Associates"><b>Marrero Bernal &amp; Associates</b><span><i data-seg="fb.mba" data-fmt="full">5,214</i> followers · sponsor</span></a>
    </div>
    <p style="color:var(--mut);font-size:13px;margin-top:18px">Facebook total: <b style="color:var(--fg)"><span data-seg="tot.fbTodo" data-fmt="full">863,243</span></b> followers, plus <span data-seg="tot.igTodo" data-fmt="full">113,887</span> on Instagram.</p>
  </div>
</section>

<section id="trabajos">
  <div class="wrap">
    <div class="kicker">Our productions</div>
    <h2>Our own shows and formats.</h2>
    <div class="works">
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/risa.jpg')); ?>)" href="https://www.youtube.com/@LaRisaEsCosaSeria?sub_confirmation=1" target="_blank" rel="noopener"><div><b>La Risa es Cosa Seria</b><span>Stand-up series · full production</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/welcome.jpg')); ?>)" href="https://www.welcometoapagonia.com" target="_blank" rel="noopener"><div><b>Welcome to Apagonia · Coming soon</b><span>Sitcom series · writing, directing and post</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/s2d.jpg')); ?>)" href="https://www.straight2dchest.com/" target="_blank" rel="noopener"><div><b>Straight 2D Chest</b><span>Interview show · set, recording and distribution</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/cosa.jpg')); ?>)" href="https://www.lcedr.com" target="_blank" rel="noopener"><div><b>La Cosa Es De Risa</b><span>Apagonia Hoy, the newscast, plus the Bacallao Sin Pan and Despingovery segments and more · original format</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/home.jpg')); ?>)" href="https://www.elhomedelarisa.com" target="_blank" rel="noopener"><div><b>El Home de la Risa</b><span>The brand that brings together all our comedy productions</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/cuero.jpg')); ?>)" href="https://www.lcedr.com" target="_blank" rel="noopener"><div><b>Si de Cuero se Trata · Premieres December 18</b><span>The Cuban roast · original format</span></div></a>
      <a class="wk" style="background-image:url(<?php echo esc_url(get_theme_file_uri('img/ansn.jpg')); ?>)" href="https://www.facebook.com/aquinoserienadie/" target="_blank" rel="noopener"><div><b>Aquí No Se Ríe Nadie · Spring 2027</b><span>The Cuban laugh-off: whoever laughs, drinks · original format</span></div></a>
    </div>
  </div>
</section>

<section id="nosotros" class="about" style="background:var(--bg2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="marcas">
      <a href="https://www.youtube.com/@LaRisaEsCosaSeria?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/larisa.png')); ?>" alt="La Risa es Cosa Seria"></a><a href="https://www.straight2dchest.com/" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/s2d.png')); ?>" alt="Straight 2D Chest"></a><a href="https://www.youtube.com/channel/UCsLPvvD_UDgwo91eeUOZUSQ?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/lacosa.png')); ?>" alt="La Cosa Es De Risa"></a><a href="https://www.youtube.com/channel/UCtf5fq1TdwirbFswJfZSWCA?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/welcome.png')); ?>" alt="Welcome to Apagonia"></a><a href="https://www.youtube.com/@marrerobernalmedia?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/mbentv.png')); ?>" alt="MB en TV · tráileres de Marrero Bernal Media"></a><a href="https://www.youtube.com/channel/UCItBxtE_Ky-C7Q3IfvC5ZMg?sub_confirmation=1" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/marcas/cuero.png')); ?>" alt="Si de Cuero se Trata"></a>
    </div>
    <div>
      <div class="kicker">About</div>
      <h2>A production company with a director's eye.</h2>
      <p class="lead">Marrero Bernal Media LLC was founded in Las Vegas with <a href="https://www.imdb.com/name/nm3952887/" target="_blank" rel="noopener" style="text-decoration:underline;text-underline-offset:3px">Eliam Marrero Bernal</a> as producer: a director and cinematographer with film and television credits. What began as a Cuban comedy channel is today a network of five channels, seven Meta pages and a production team that premieres new content every week of the year.</p>
      <p class="lead" style="margin-top:14px">We bring the same rigor to an episode of our own series as to a client's commercial: script, light, sound, pacing and, above all, knowing who we're talking to.</p>
      <div class="creds">
        <span>Directing and cinematography</span><a href="https://www.imdb.com/name/nm3952887/" target="_blank" rel="noopener"><span>IMDb credits ↗</span></a><span>FAA Part 107 pilot</span><span>Las Vegas · Miami</span><span>Spanish and English</span>
      </div>
    </div>
  </div>
</section>

<section id="proceso">
  <div class="wrap">
    <div class="kicker">How we work</div>
    <h2>From the first message to delivery.</h2>
    <div class="steps">
      <div class="step"><h3>We listen</h3><p>You tell us what you need and who you want to reach. No endless forms: one call is enough.</p></div>
      <div class="step"><h3>We propose</h3><p>You get a clear proposal with format, scope, schedule and a fixed budget.</p></div>
      <div class="step"><h3>We produce</h3><p>Script, shoot, drone, editing and design with our team. You approve every stage.</p></div>
      <div class="step"><h3>We deliver and distribute</h3><p>Versions for every platform and, if you want, distribution inside our network with a results report.</p></div>
    </div>
  </div>
</section>

<section id="contacto" class="contact">
  <div class="wrap">
    <div class="cinfo">
      <div class="kicker">Contact</div>
      <h2>Tell us about your project.</h2>
      <p>We reply within one business day.</p>
      <a href="mailto:info@marrerobernalmedia.com">info@marrerobernalmedia.com</a>
      <a href="https://wa.me/18336277376" target="_blank" rel="noopener">WhatsApp 833-627-7376</a>
      <a href="tel:+18336277376">833-627-7376 <small style="font-size:13px;font-weight:400;color:var(--mut)">833-MARRERO</small></a>
      <p>Call us and leave a voicemail, or message us on WhatsApp. This number does not receive text messages (SMS).</p>
      <div id="vonageClick2callme" style="margin-top:16px"></div>
      <p>Las Vegas, Nevada · productions across the United States</p>
      <p style="margin-top:22px">YouTube · Facebook · Instagram · TikTok · X: <b style="color:var(--fg)">@marrerobernalmedia</b></p>
    </div>
    <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="mbm_contacto"><?php wp_nonce_field('mbm_contacto','mbm_n'); ?><input type="text" name="sitio" style="display:none" tabindex="-1" autocomplete="off">
      <input name="nombre" placeholder="Name" required>
      <input name="empresa" placeholder="Company">
      <input type="email" name="correo" placeholder="Email" required>
      <input name="telefono" placeholder="Phone or WhatsApp">
      <select name="servicio"><option>What do you need?</option><option>Commercial or corporate video</option><option>Editing and post-production</option><option>Drone filming</option><option>Photography</option><option>Event coverage</option><option>Translation, subtitles or voice-over</option><option>AI animation</option><option>Podcast or streaming</option><option>Design and corporate identity</option><option>Website or app</option><option>Channel management</option><option>Advertising on the network</option></select>
      <textarea name="mensaje" placeholder="Briefly describe the project"></textarea>
      <button class="btn btn-acc" type="submit" style="justify-self:start">Send</button>
      <?php if (isset($_GET['enviado'])): ?><div class="ok">✅ Received. We reply within one business day.</div><?php elseif (isset($_GET['error'])): ?><div class="ok" style="background:#3a1a1a;color:#ffb4b4">Could not send. Email us at info@marrerobernalmedia.com.</div><?php endif; ?>
    </form>
  </div>
</section>


<?php get_footer('en'); ?>
