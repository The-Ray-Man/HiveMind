(this["webpackJsonpcra-hive"]=this["webpackJsonpcra-hive"]||[]).push([[4],{298:function(t,e,n){"use strict";n.r(e),n.d(e,"default",(function(){return A}));var c=n(28);var r=n(16),a=n(158);function i(t,e){return{highlighted:[],handleBoardClick:function(){return console.log("Remote player's turn")},handleDropClick:function(){return console.log("Remote player's turn")}}}var o=n(25),u=n(0),s=n(228),j=n(235),l=n(297),f=n(229),d=n(7);function b(t){var e=t.socket,n=Object(u.useState)([]),c=Object(r.a)(n,2),a=c[0],i=c[1],b=Object(u.useState)(""),p=Object(r.a)(b,2),h=p[0],O=p[1];Object(u.useEffect)((function(){var t=function(t){i((function(e){return[].concat(Object(o.a)(e),[t])}))};return e.on("chatMessage",t),function(){e.off("chatMessage",t)}}),[e]);return Object(d.jsx)("div",{children:Object(d.jsxs)(s.a,{fluid:!0,children:[Object(d.jsx)(j.a.Group,{size:"small",style:{height:"500px",overflow:"auto"},children:a.map((function(t){var n=t.text,c=t.sender,r=t.time;return Object(d.jsxs)(d.Fragment,{children:[Object(d.jsx)(j.a,{inverted:!0,floated:c===e.id?"left":"right",color:c===e.id?"yellow":"green",style:{borderRadius:c===e.id?"25px 25px 25px 0px":"25px 25px 0px 25px"},children:n},r),Object(d.jsx)(l.a,{hidden:!0,clearing:!0})]})}))}),Object(d.jsx)("form",{onSubmit:function(t){h&&(e.emit("chatMessage",h),O("")),t.preventDefault()},children:Object(d.jsx)(f.a,{fluid:!0,focus:!0,type:"text",value:h,onChange:function(t){return O(t.target.value)},placeholder:"Type something",action:{icon:"send",color:"primary"}})})]})})}var p=n(266),h=n.n(p),O=n(178);var x=n(176);function v(t){var e=t.socket,n=t.gid,c=t.p1,a=t.p2,i=function(){var t=Object(u.useState)(0),e=Object(r.a)(t,2)[1];return function(){return e((function(t){return t+1}))}}(),o=Object(x.a)(),s=o.apply,j=o.state;return Object(u.useEffect)((function(){e.emit("joinGame",n);var t=function(t){s(t),i()};return e.on("updateAction",t),function(){e.off("updateAction",t)}}),[e]),Object(d.jsx)(m,{state:j,p1:c,p2:a,submitAction:function(t){return e.emit("intendAction",{action:t})}})}function m(t){var e=t.state,n=t.p1,c=t.p2,r=t.submitAction,a=(e.turnNumber%2===0?n:c)(r,e);return Object(d.jsx)(O.a,{controller:a,state:e})}function g(t){var e,n,c=t.gid,o=t.team,s=Object(u.useState)(null),j=Object(r.a)(s,2),l=j[0],f=j[1];return Object(u.useEffect)((function(){var t=h()();return f(t),function(){t.close()}}),[f]),"white"===o?(e=a.a,n=i):(e=i,n=a.a),Object(d.jsx)("div",{children:l?Object(d.jsxs)("div",{children:[Object(d.jsx)(v,{socket:l,gid:c,p1:e,p2:n}),Object(d.jsx)(b,{socket:l})]}):"Not Connected"})}var y=n(166);function k(){var t=a.a,e=a.a;return Object(d.jsx)(y.a,{p1:t,p2:e})}function w(t,e){t(e.actions[Math.floor(Math.random()*e.actions.length)])}function S(t){var e,n;return"white"===t.team?(e=a.a,n=w):(e=w,n=a.a),Object(d.jsx)(y.a,{p1:e,p2:n})}function A(){var t=Object(c.g)().gid,e=new URLSearchParams(Object(c.f)().search),n=e.get("team")||"white",r=e.get("mode")||"local";return"online"===r?Object(d.jsx)(g,{gid:t,team:n}):"local"===r?Object(d.jsx)(k,{}):"ai"===r?Object(d.jsx)(S,{team:n}):Object(d.jsx)("div",{children:"Invalid Game"})}}}]);
//# sourceMappingURL=4.fce389ff.chunk.js.map