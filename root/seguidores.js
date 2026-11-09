/* Seguidores de la red MBM. Fuente única para todos los sitios.
   Se actualiza cada semana (lunes) con los totales que Pepe le da a Eliam
   (Facebook e Instagram) y con vidIQ (YouTube). No editar a mano los sitios:
   editar este archivo y hacer push. */
window.SEGUIDORES = {
  "actualizado": "2026-11-09",
  "fb": {"larisa":585725,"lacosa":173701,"recta":72407,"elhome":14449,"mba":5213,"cuero":2330,"welcome":3726,"mbm":1397,"eliam":11329,"nadie":456},
  "ig": {"larisa":50597,"lacosa":31382,"mbm":10256,"recta":9422,"welcome":3705,"elhome":2040,"nadie":46,"cuero":19,"mba":218,"eliam":7163},
  "yt": {"larisa":91809,"recta":19129,"lacosa":13983,"elhome":3347,"welcome":2807,"mbm":17}
};
(function(){
  var S=window.SEGUIDORES, RED=["larisa","lacosa","recta","elhome","welcome","mbm","cuero","nadie"];
  function sum(o,keys){var t=0;keys.forEach(function(k){t+=o[k]||0});return t;}
  var fbRed=sum(S.fb,RED), igRed=sum(S.ig,RED), ytRed=sum(S.yt,RED);
  S.tot={fbRed:fbRed, igRed:igRed, ytRed:ytRed, metaRed:fbRed+igRed, todo:fbRed+igRed+ytRed,
         mba: (S.fb.mba||0)+(S.ig.mba||0)+(S.fb.eliam||0)+(S.ig.eliam||0),
         fbTodo: sum(S.fb,Object.keys(S.fb)), igTodo: sum(S.ig,Object.keys(S.ig))};
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
