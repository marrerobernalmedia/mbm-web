/* Ajustes fijos sobre data.js (data.js se reemplaza cada semana; esto no).
   Lo usan la app (index.html) y el generador de páginas (tools/build_elhome_seo.js),
   así la app y la página de Google muestran lo mismo. */
(function () {
  // Un humorista, una sola ficha: los nombres artísticos se unen al nombre principal (Eliam, 30-oct-2026)
  var ALIAS = { "Kamilo Kabello": "Dani Quintero", "Wattage": "Newito" };
  // Videos que la lista de YouTube no trae pero son del humorista (Eliam, 30-oct-2026): van en "En La Risa es Cosa Seria"
  var EXTRA_LR = { "Newito": ["qQ72eLSjGy8"] };
  // Estrenos que data.js trae sin humorista
  // Capítulos que data.js trae solo con el nombre del humorista: su título real de YouTube (Eliam, 8-nov-2026)
  var TITULOS = { "L8Wp7E1EGuo": "La novela de donde NADIE SE VA, el apagón ROMÁNTICO y Leopoldo en la balsa. LRECS #84 | MIGDALIA", "-BAEkShCWcU": "LISANDRA de 👁️de AGUA que no AGUANTÓ, la tarjeta CRICAR y el hombre del APAGÓN. LRECS #83 | NARCISO", "t4WxtA1VkQc": "Soy el MAPA: el trauma de los niños, el papelito y la chancleta. LRECS #82 | DANI QUINTERO", "wjOs64ijv2k": "¿Dónde está EDDY? La i-220a, la operación y el apagón que lo volvió. LRECS #81 | EDDY CEBALLOS", "K86J-zYlH4I": "CHISTES DE BORRACHOS: El perdido de Los Alpes y García el policía. LRECS #80 | Juan Karlos el Gordo", "Pmjdz2_9tFU": "La MACHI llama al ENEMIGO: ¿A qué hora es el ATAQUE? 😱 LRECS #78 | Marcos Medina", "72DG3nlOl8E": "El PARTO vs los \"3 minutos\", la MENOPAUSIA y lo que aguanta la cubana. LRECS #77 | Yaneza", "y4IoY70R1qU": "65 SEMANAS de embarazo \"hasta que ..\", el repelente EN DÓLARES y el chikungunya. LRECS #76 | Philips", "Y4VBGdENl30": "La CASA de 3 pisos… ¡de TIERRA!, la de WhatsApp y la canción del gago. LRECS #75 | Marcos el Pío", "nv2W_Bhxg5g": "Le canta a su CALVA, el que cocina con HIGIENE EXTREMA y la maleta. LRECS #49 | Marcos Medina", "d3oBhlzHFts": "Los baches que se comen los carros, el safari urbano y La Habana del 2030. LRECS #44 | Eddy Ceballos", "Xc-c64wvToE": "El dólar que se fue de jonrón, el consultorio de los síntomas y el mosquito. LRECS #43 | BAUDILIO", "ugzU5DL9xrY": "El yogur de SOYA, la suegra encantadora de SERPIENTES y la SARNA. LRECS #15 | VISTI CÁRDENAS", "a7ffHQAqZcg": "VISTI CÁRDENAS | Esto solo pasa en CUBA cu | LRECS #14" };
  var CAST = { "9vWXC53rrWs": ["Bacallao"] };
  // Humoristas que faltan en un capítulo que ya trae otro (Eliam, 8-nov-2026): "Habla 4 IDIOMAS…" de
  // Bacallao Sin Pan es también con Genaro Pomposo (Orlando Manrufo) → entra en la ficha de Manrufo
  // y los especiales de La Risa con dos humoristas (Eliam, 8-nov-2026): el capítulo entra también en la ficha del otro
  var SUMAR = { "Upd19ziJMH4": ["Genaro Pomposo"], "6dbNi1XFZxs": ["El Habanero"], "5jffAxE5-dc": ["El Habanero"],
    "-bRT6Gi1aRE": ["Mentepollo", "Cabo Pantera"], "SWV7QPHBM-U": ["La Llave"], "NaB7wj5LbUI": ["Eddy Ceballos"],
    // Compilatorios: los que salen en la portada/título (Eliam, 8-nov-2026: Lindoro en "La televisión cubana")
    "ravQUTT4dco": ["Lindoro"], "lApWsQw4Aio": ["Mariconchi", "Rigo Ferrera"], "IokEG-yY0ds": ["El Habanero", "Mariconchi"],
    "Z9f8IATzAuw": ["Mentepollo"], "11KYGWub6Zk": ["La Llave", "El Habanero"], "HVZEbcBsDvc": ["Bacallao"],
    "IFXkzeovKzM": ["Rigo Ferrera"], "P1bSrakbi2A": ["Cabo Pantera"] };
  // El actor va por su nombre, con sus personajes dentro (Eliam, 5-nov-2026): Orlando Manrufo hace de
  // Mariconchi y de Genaro Pomposo; una sola ficha "Manrufo" con los videos de los dos personajes
  var ACTOR = { "Manrufo": ["Mariconchi", "Genaro Pomposo", "Orlando Manrufo"],
    // Burumba (Manolo Parkinson) es un personaje de Eddy Ceballos, alias Eddy Jones (Eliam, 8-nov-2026)
    "Eddy Ceballos": ["Burumba", "Manolo Parkinson", "Eddy Jones"] };
  // Los estrenos programados (con su tráiler) entran ya en la ficha del humorista; si el humorista
  // todavía no tiene ficha, se le crea (Eliam, 31-oct-2026: Yamira Díaz).
  window.AJUSTAR = function (D) {
    var V = D.vid, byName = {};
    Object.keys(TITULOS).forEach(function (id) { if (V[id]) V[id].t = TITULOS[id]; });
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
    var enLR = {}; D.shows.forEach(function (s) { if (s.id === "lrecs") (s.v || []).concat((s.subs || []).flatMap(function (x) { return x.v || []; })).forEach(function (i) { enLR[i] = 1; }); });
    Object.keys(SUMAR).forEach(function (id) { if (!V[id]) return; V[id].c = Array.from(new Set((V[id].c || []).concat(SUMAR[id])));
      SUMAR[id].forEach(function (n) { var c = byName[n]; if (!c) return; if (c.all.indexOf(id) < 0) c.all.push(id); if (enLR[id] && c.lr.indexOf(id) < 0) c.lr.push(id); }); });
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
    // Apagonia Hoy es un noticiero de elenco fijo (Bacallao, Lady Bhagga y casi siempre Dani Quintero) y ningún
    // capítulo está dedicado a un humorista: sus capítulos van SOLO en Apagonia Hoy, sin nombres debajo y fuera
    // de las fichas de los humoristas (Eliam, 8-nov-2026)
    var soloShow = {}; D.shows.forEach(function (s) { if (s.id === "hoy") (s.v || []).concat((s.subs || []).flatMap(function (x) { return x.v || []; })).forEach(function (i) { soloShow[i] = 1; }); });
    Object.keys(soloShow).forEach(function (id) { if (V[id]) V[id].c = []; });
    D.comics.forEach(function (c) { c.all = c.all.filter(function (i) { return !soloShow[i]; }); c.lr = c.lr.filter(function (i) { return !soloShow[i]; }); });
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
    // Debajo de cada capítulo de Apagonia Hoy van los personajes fijos (Eliam, 8-nov-2026): el presentador
    // Kamilo Kabello (con K las dos veces; lo hace Dani Quintero) y la conductora Juana Sin Armas (la hace
    // Yanelsi, la de Lady Bhagga). Solo como nombre debajo: no entran en ninguna ficha de humorista.
    Object.keys(soloShow).forEach(function (id) { if (V[id]) V[id].c = ["Kamilo Kabello", "Juana Sin Armas"]; });
    // Cada capítulo de Apagonia Hoy tiene un actor invitado (Eliam, 8-nov-2026): va delante de los fijos y el capítulo
    // entra en la ficha del invitado. Sin número de episodio (ninguno lo lleva).
    var HOY_INVITADOS = {
      // Manrufo: en Apagonia Hoy lo entrevistan como él mismo, Orlando Manrufo, salvo en "Murió la libreta" y
      // "Ni en pobreza", donde sale como Mariconchi (Eliam, 8-nov-2026)
      "eXfx56gUutQ": ["Orlando Manrufo"], "NMpPuEm8bwI": ["Mayito el Gladiador"], "jgdWgzIt724": ["Mariconchi", "Nieto de Juana"],
      "RoSEL5ufLfw": ["Burumba", "Julio Meireles"], "B5MnYHBJFNk": ["Burumba", "Julio Meireles"],
      "wroK9S73DcA": ["Mayito el Gladiador"], "ImQ0QYJloR0": ["Mayito el Gladiador"],
      "rDCbNKUIoRY": ["Mentepollo"], "uaG6X7E6tck": ["Mentepollo"],
      "KTDyO6Vunrk": ["Cabo Pantera"], "uA_OQ5wLKqo": ["Cabo Pantera"],
      "Ypwwhoc4Cbw": ["Voltímetro", "El Rubio"], "V7kR6ISOZi0": ["Voltímetro", "El Rubio"],
      "9YUyqlIElh0": ["Marcos Medina", "Philips"], "4YV4c6xOGiQ": ["Marcos Medina", "Philips"],
      "030feE-J8EY": ["Yaneza"], "9H6FAa1kSN0": ["Yaneza"],
      "_mMIlsYH8tQ": ["Voltímetro"], "yLH7LoHnj0g": ["Voltímetro"],
      "Gda0eiRjizI": ["Juan Karlos"], "kbbLN6JpwoU": ["Eddy Ceballos"],
      "sfbGeaBQsxM": ["El Habanero"], "JXRfSgv2his": ["El Habanero"], "5X1cNhJalCs": ["El Habanero", "El Rubio"],
      "mq8kpm3klM8": ["El Rubio"], "BUCsZYIoUyU": ["Orlando Manrufo"], "M57sV2raNsw": ["Mariconchi"],
      "Rv-MZasqyfQ": ["Minerva"], "cSPSxDnfpKg": ["Philips"], "wRd8XMnIj-I": ["Javier Darío"],
      "DAx42djn-iA": ["Dani Quintero"], "_456m4SuYSw": ["Bacallao"],
      "d0IwhM1jxMY": ["Narciso", "Marcos Medina"], "depAnCzOROU": ["Narciso", "Marcos Medina"],
      "UmWVGA1qI6s": ["Orlando Manrufo"], "cbbJyuVwVPE": ["Migdalia"], "1kBZb7UJfzo": ["Bacallao"]
    };
    Object.keys(soloShow).forEach(function (id) { if (V[id]) V[id].n = ""; });
    Object.keys(HOY_INVITADOS).forEach(function (id) { if (!V[id]) return;
      V[id].c = HOY_INVITADOS[id].concat(V[id].c);
      HOY_INVITADOS[id].forEach(function (n) { var c = byName[n];
        if (!c) { c = byName[n] = { name: n, banner: null, lr: [], all: [] }; D.comics.push(c); }
        if (c.all.indexOf(id) < 0) c.all.push(id); }); });
    return D;
  };
})();

// Título para mostrar (Eliam, 7-nov-2026): si el título de YouTube trae al principio o al final el nombre del
// humorista que ya sale debajo, se le quita. En la app y en las páginas de Google; en YouTube no cambia.
const _n = x => String(x).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
const _sep = "[\\s|:·,\\-–—!¡?¿.\\p{Extended_Pictographic}\\uFE0F\\u200D]";
// Nombre completo del actor, para quitarlo también del título (Eliam, 7-nov-2026: "ORLANDO MANRUFO")
const NOMBRE_COMPLETO = { "Manrufo": ["Orlando Manrufo"] };
window.TITULO_LIMPIO = function (D, id) { const V = D.vid, v = V[id]; let t = v.t; const CM = {}; D.comics.forEach(c => { CM[c.name] = c; (c.aka || []).forEach(a => { CM[a] = CM[a] || c; }); });
  t = t.replace(/&vert;/g, "|");
  // "… y la chancleta. LRECS #82 | DANI QUINTERO": el número y el nombre ya salen arriba y debajo (Eliam, 8-nov-2026)
  t = t.replace(/[\s.|·\-–—]*\bLRECS\s*#?\s*\d+\s*\|\s*[^|]{1,40}$/iu, "").trim() || v.t;
  // La etiqueta del show ya sale arriba (LA RISA ES COSA SERIA #96): se quita el "| LRECS #96" del final
  t = t.replace(/[\s|·\-–—\p{Extended_Pictographic}\uFE0F\u200D]*\bLRECS(\s*(EP\.?\s*)?#?\s*\d+)?\s*$/iu, "").trim() || v.t;
  const names = [...new Set((v.c || []).flatMap(n => { const c = CM[n]; const l = [n].concat(c ? [c.name].concat(c.aka || [], NOMBRE_COMPLETO[c.name] || []) : []); return l.flatMap(x => { const w = x.split(" ")[0]; return w.length >= 5 && w !== x ? [x, w] : [x]; }); }))].sort((a, b) => b.length - a.length);
  if (!names.length) return t;
  // Se quita un solo nombre (el del principio o el del final), para no comerse la frase
  { const nt = _n(t);
    for (const nm of names) { const q = _n(nm).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      let m = nt.match(new RegExp("(^|\\s)" + q + "(" + _sep + "*)$", "u"));
      if (m && m.index + m[1].length > 0 && !/(^|\s)(de|del|con|y|e|a|al|por|para|sin|en|la|el|los|las|cu)$/.test(nt.slice(0, m.index).trim())) { t = t.slice(0, m.index + m[1].length).replace(/[\s|:·,\-–—\p{Extended_Pictographic}\uFE0F\u200D]+$/u, "").trim(); break; }
      m = nt.match(new RegExp("^" + q + "(\\s*(?:[|:·\\-–—]|\\p{Extended_Pictographic})" + _sep + "*)", "u"));
      if (m && m[0].length < nt.length) { t = t.slice(m[0].length).trim(); break; } } }
  return t || v.t; };
