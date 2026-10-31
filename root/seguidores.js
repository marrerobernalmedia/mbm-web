/* Seguidores de la red MBM. Fuente única para todos los sitios.
   Se actualiza cada semana (lunes) con los totales que Pepe le da a Eliam
   (Facebook e Instagram) y con vidIQ (YouTube). No editar a mano los sitios:
   editar este archivo y hacer push. */
window.SEGUIDORES = {
  "actualizado": "2026-10-30",
  "fb": {"larisa":584344,"lacosa":172454,"recta":71612,"elhome":13236,"mba":5214,"cuero":2106,"welcome":1729,"mbm":1325,"eliam":11223},
  "ig": {"larisa":50500,"lacosa":31300,"mbm":10100,"recta":9202,"welcome":3670,"elhome":1668,"nadie":45,"cuero":19,"mba":217,"eliam":7166},
  "yt": {"larisa":91500,"recta":18900,"lacosa":13700,"elhome":3200,"welcome":2700,"mbm":14}
};
(function(){
  var S=window.SEGUIDORES, RED=["larisa","lacosa","recta","elhome","welcome","mbm","cuero","nadie"];
  function sum(o,keys){var t=0;keys.forEach(function(k){t+=o[k]||0});return t;}
  var fbRed=sum(S.fb,RED), igRed=sum(S.ig,RED), ytRed=sum(S.yt,RED);
  S.tot={fbRed:fbRed, igRed:igRed, ytRed:ytRed, metaRed:fbRed+igRed, todo:fbRed+igRed+ytRed,
         mba: (S.fb.mba||0)+(S.ig.mba||0)+(S.fb.eliam||0)+(S.ig.eliam||0)};
  /* Formato: 1,083,000 → "1M+", 584,344 → "584K", 9,202 → "9.2K", 845 → "845" */
  S.k=function(n){ if(n>=1e6) return (Math.floor(n/1e5)/10).toFixed(n%1e6<1e5?0:1).replace(/\.0$/,"")+"M+";
    if(n>=1e4) return Math.floor(n/1e3)+"K"; if(n>=1e3) return (Math.floor(n/100)/10).toFixed(1).replace(/\.0$/,"")+"K"; return String(n); };
  S.full=function(n){ return n.toLocaleString("en-US"); };
  function get(path){ return path.split(".").reduce(function(o,k){return o?o[k]:undefined;},S); }
  function fill(){
    document.querySelectorAll("[data-seg]").forEach(function(el){
      var v=get(el.getAttribute("data-seg")); if(v==null) return;
      var f=el.getAttribute("data-fmt")||"k";
      el.textContent = f==="full" ? S.full(v) : f==="mil" ? S.full(Math.floor(v/1000)*1000) : f==="kplus" ? S.k(v).replace(/\+?$/,"+") : S.k(v);
    });
  }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",fill); else fill();
})();
