/* Ajustes fijos sobre data.js (data.js se reemplaza cada semana; esto no).
   Lo usan la app (index.html) y el generador de páginas (tools/build_elhome_seo.js),
   así la app y la página de Google muestran lo mismo. */
(function () {
  // Un humorista, una sola ficha: los nombres artísticos se unen al nombre principal (Eliam, 30-oct-2026)
  var ALIAS = { "Kamilo Kabello": "Dani Quintero", "Wattage": "Newito" };
  // Videos que la lista de YouTube no trae pero son del humorista (Eliam, 30-oct-2026): van en "En La Risa es Cosa Seria"
  var EXTRA_LR = { "Newito": ["qQ72eLSjGy8"] };
  // Estrenos que data.js trae sin humorista
  var CAST = { "9vWXC53rrWs": ["Bacallao"] };
  // El actor va por su nombre, con sus personajes dentro (Eliam, 5-nov-2026): Orlando Manrufo hace de
  // Mariconchi y de Genaro Pomposo; una sola ficha "Manrufo" con los videos de los dos personajes
  var ACTOR = { "Manrufo": ["Mariconchi", "Genaro Pomposo"] };
  // Los estrenos programados (con su tráiler) entran ya en la ficha del humorista; si el humorista
  // todavía no tiene ficha, se le crea (Eliam, 31-oct-2026: Yamira Díaz).
  window.AJUSTAR = function (D) {
    var V = D.vid, byName = {};
    // Series que se ven en su orden (Lección 1, 2, 3…), también en la página principal (Eliam, 5-nov-2026)
    D.shows.forEach(function (s) { if (s.id === "ayer") s.asc = true; });
    D.comics.forEach(function (c) { c.lr = c.lr || []; c.all = c.all || []; byName[c.name] = c; });
    Object.keys(ALIAS).forEach(function (from) {
      var src = byName[from], dst = byName[ALIAS[from]]; if (!src || !dst) return;
      dst.all = Array.from(new Set(dst.all.concat(src.all)));
      dst.lr = Array.from(new Set(dst.lr.concat(src.lr)));
      dst.aka = (dst.aka || []).concat(from);
      D.comics.splice(D.comics.indexOf(src), 1); delete byName[from];
    });
    Object.keys(EXTRA_LR).forEach(function (name) {
      var c = byName[name]; if (!c) return;
      EXTRA_LR[name].forEach(function (id) { if (!V[id]) return; if (c.lr.indexOf(id) < 0) c.lr.unshift(id); if (c.all.indexOf(id) < 0) c.all.unshift(id); V[id].c = Array.from(new Set((V[id].c || []).concat(name))); });
    });
    Object.keys(CAST).forEach(function (id) { if (V[id] && !(V[id].c || []).length) V[id].c = CAST[id].slice(); });
    Object.keys(ACTOR).forEach(function (actor) {
      var roles = ACTOR[actor], dst = byName[actor];
      roles.forEach(function (r) {
        var src = byName[r]; if (!src) return;
        if (!dst) { src.name = actor; dst = byName[actor] = src; }
        else if (src !== dst) { dst.all = Array.from(new Set(dst.all.concat(src.all))); dst.lr = Array.from(new Set(dst.lr.concat(src.lr))); dst.banner = dst.banner || src.banner; D.comics.splice(D.comics.indexOf(src), 1); }
      });
      if (dst) { dst.aka = Array.from(new Set((dst.aka || []).concat(roles))); roles.forEach(function (r) { byName[r] = dst; }); }
      // En cada capítulo se queda el nombre del personaje (Mariconchi / Genaro Pomposo); los de Manrufo van a su ficha
      if (dst) Object.keys(V).forEach(function (id) { var v = V[id]; if ((v.c || []).some(function (n) { return n === actor || roles.indexOf(n) >= 0; })) { if (dst.all.indexOf(id) < 0) dst.all.push(id); } });
    });
    Object.keys(V).forEach(function (id) { var v = V[id]; if (v.c) v.c = Array.from(new Set(v.c.map(function (n) { return ALIAS[n] || n; }))); });
    var lrecs = {}; D.shows.forEach(function (s) { if (s.id === "lrecs") (s.v || []).forEach(function (i) { lrecs[i] = 1; }); });
    Object.keys(V).forEach(function (id) {
      var v = V[id]; if (!(v.k === "proximo" || v.k === "futuro" || v.nuevo) || !(v.c || []).length) return;
      v.c.forEach(function (name) {
        var c = byName[name];
        if (!c) { c = byName[name] = { name: name, banner: null, lr: [], all: [] }; D.comics.push(c); }
        if (lrecs[id] && c.lr.indexOf(id) < 0) c.lr.unshift(id);
        if (c.all.indexOf(id) < 0) c.all.unshift(id);
      });
    });
    return D;
  };
})();
