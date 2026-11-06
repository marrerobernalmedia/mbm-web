/* Últimos estrenos de la red en marrerobernalmedia.com (ES y /en/).
   Lee los mismos data.js de las apps (elhome/ y recta/), que Claude actualiza el día de cada estreno,
   así la fila se pone al día sola. Un estreno cuenta como salido desde las 8:00 AM de Las Vegas de su fecha. */
(function () {
  var box = document.getElementById('estrenos-lista');
  if (!box) return;
  var EN = /^en/i.test(document.documentElement.lang || '') || /^\/en(\/|$)/.test(location.pathname);
  var BASE = '';
  function lvNow() {
    var p = {};
    new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Los_Angeles', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hour12: false })
      .formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
    return { d: p.year + '-' + p.month + '-' + p.day, h: parseInt(p.hour, 10) % 24 };
  }
  function load(path) {
    return fetch(BASE + path, { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) {
      var w = {}; new Function('window', t)(w); return w.APPDATA || {};
    }).catch(function () { return {}; });
  }
  function fecha(f) {
    var d = new Date(f + 'T12:00:00');
    return d.toLocaleDateString(EN ? 'en-US' : 'es-ES', { day: 'numeric', month: 'short' });
  }
  Promise.all([load('/elhome/data.js'), load('/recta/data.js')]).then(function (r) {
    var H = r[0], R = r[1], now = lvNow(), items = [];
    var salio = function (f) { return f && (f < now.d || (f === now.d && now.h >= 8)); };
    var showDe = {};
    (H.shows || []).forEach(function (s) { (s.v || []).forEach(function (id) { if (!showDe[id]) showDe[id] = s.name; }); });
    Object.keys(H.vid || {}).forEach(function (id) {
      var v = H.vid[id];
      if (salio(v.f)) items.push({ id: id, f: v.f, t: v.t, k: showDe[id] || 'El Home de la Risa' });
    });
    Object.keys(R.vid || {}).forEach(function (id) {
      var v = R.vid[id];
      if (salio(v.f)) items.push({ id: id, f: v.f, t: (v.p ? v.p + ': ' : '') + v.t, k: 'Recta Al Pecho' });
    });
    items.sort(function (a, b) { return b.f.localeCompare(a.f); });
    items = items.slice(0, 6);
    if (!items.length) { box.closest('section').hidden = true; return; }
    box.innerHTML = '';
    items.forEach(function (it) {
      var a = document.createElement('a');
      a.className = 'est';
      a.href = 'https://www.youtube.com/watch?v=' + it.id;
      a.target = '_blank'; a.rel = 'noopener';
      var img = document.createElement('img');
      img.src = 'https://i.ytimg.com/vi/' + it.id + '/mqdefault.jpg';
      img.alt = ''; img.loading = 'lazy'; img.width = 320; img.height = 180;
      var k = document.createElement('span'); k.className = 'k'; k.textContent = it.k + ' · ' + fecha(it.f);
      var t = document.createElement('b'); t.textContent = it.t;
      a.appendChild(img); a.appendChild(k); a.appendChild(t);
      box.appendChild(a);
    });
  });
})();
