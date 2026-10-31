/* Español / English para los sitios de Marrero Bernal.
   Cada sitio define window.I18N_EN = { "texto en español": "English text", ... }
   (claves = texto exacto de cada nodo de texto, placeholder, alt o title, recortado).
   Uso: <a href="#" data-lang="en">EN</a> / data-lang="es". Recuerda la elección
   del visitante; por defecto, inglés si el navegador no está en español. */
(function(){
  var D = window.I18N_EN || {};
  var nodes = [], attrs = [];
  function collect(root){
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {acceptNode:function(n){
      var p = n.parentNode; if(!p) return NodeFilter.FILTER_REJECT;
      var t = p.nodeName; if(t==="SCRIPT"||t==="STYLE"||t==="NOSCRIPT") return NodeFilter.FILTER_REJECT;
      return n.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP; }});
    var n; while((n = w.nextNode())){
      var raw = n.nodeValue, k = raw.trim();
      if(D[k] !== undefined){
        var i = raw.indexOf(k);
        nodes.push({n:n, es:raw, en: raw.slice(0,i) + D[k] + raw.slice(i+k.length)});
      }
    }
    ["placeholder","alt","title","aria-label"].forEach(function(a){
      root.querySelectorAll("["+a+"]").forEach(function(el){
        var v = el.getAttribute(a); if(D[v.trim()] !== undefined) attrs.push({el:el,a:a,es:v,en:D[v.trim()]});
      });
    });
  }
  function apply(lang){
    nodes.forEach(function(x){ x.n.nodeValue = lang==="en" ? x.en : x.es; });
    attrs.forEach(function(x){ x.el.setAttribute(x.a, lang==="en" ? x.en : x.es); });
    document.documentElement.lang = lang;
    document.querySelectorAll("[data-lang]").forEach(function(el){
      el.classList.toggle("on", el.getAttribute("data-lang")===lang);
    });
    var t = document.querySelector("title");
    if(t && D[t.getAttribute("data-es")||""]===undefined){ /* título: usa data-en si existe */
      var en = t.getAttribute("data-en"), es = t.getAttribute("data-es") || t.textContent;
      if(!t.getAttribute("data-es")) t.setAttribute("data-es", es);
      if(en) t.textContent = lang==="en" ? en : es;
    }
    try{ localStorage.setItem("mb_lang", lang); }catch(e){}
  }
  function initial(){
    var m = location.search.match(/[?&]lang=(en|es)/); if(m) return m[1];
    try{ var s = localStorage.getItem("mb_lang"); if(s==="en"||s==="es") return s; }catch(e){}
    var nav = (navigator.language||"es").toLowerCase();
    return nav.indexOf("es")===0 ? "es" : "en";
  }
  function start(){
    collect(document.body);
    document.querySelectorAll("[data-lang]").forEach(function(el){
      el.addEventListener("click", function(e){ e.preventDefault(); apply(el.getAttribute("data-lang")); });
    });
    apply(initial());
  }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
