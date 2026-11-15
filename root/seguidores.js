/* Seguidores de la red MBM. Fuente única para todos los sitios.
   Se actualiza cada semana (lunes) con los totales que Pepe le da a Eliam
   (Facebook e Instagram) y con vidIQ (YouTube). No editar a mano los sitios:
   editar este archivo y hacer push. */
window.SEGUIDORES = {
  "actualizado": "2026-11-15",
  "fb": {"larisa":586324,"lacosa":174750,"recta":73000,"elhome":17123,"mba":5209,"cuero":2359,"welcome":5228,"mbm":2167,"eliam":11445,"nadie":490},
  "ig": {"larisa":50614,"lacosa":31371,"mbm":10306,"recta":9477,"welcome":3720,"elhome":2776,"nadie":47,"cuero":20,"mba":219,"eliam":7159},
  "yt": {"larisa":92036,"recta":19165,"lacosa":14142,"elhome":3500,"welcome":2922,"mbm":20}
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
