/* =========================================================================
   Infinite-canvas engine — rebuilt for smoothness.
   - one rAF render loop, never reads layout during interaction
   - inertial panning, anchored zoom, eased fit/home
   - card-level viewport culling with EXACT measured intrinsic sizes,
     so nothing ever reflows or shifts while you pan
   - videos are facades: at most ONE <video> element exists at any time
   ========================================================================= */
(function () {
'use strict';

var vp    = document.getElementById('vp'),
    world = document.getElementById('world'),
    lb    = document.getElementById('lb'),
    lbImg = lb.querySelector('img');

var MIN = 0.07, MAX = 2.6;
var x = 40, y = 40, s = 0.55;              // live transform
var W = 0, H = 0;                          // world size, unscaled css px
var raf = 0, lastGrid = '';

var NODRAG = 'video,button,.p-text,input,textarea,a,#zoom,#lb,#nb';

function clamp(v) { return v < MIN ? MIN : (v > MAX ? MAX : v); }

/* ---------------------------------------------------------- render loop */
var zoomT = null;   // eased zoom toward a target scale, anchored at ax/ay
var tween = null;   // eased move for fit / home
var vx = 0, vy = 0, coasting = false;

function schedule() { if (!raf) raf = requestAnimationFrame(frame); }

function frame() {
  raf = 0;
  var more = false, now = performance.now();

  if (tween) {
    var p = Math.min(1, (now - tween.t0) / tween.ms),
        e = 1 - Math.pow(1 - p, 3);
    x = tween.x0 + (tween.x1 - tween.x0) * e;
    y = tween.y0 + (tween.y1 - tween.y0) * e;
    s = tween.s0 + (tween.s1 - tween.s0) * e;
    if (p >= 1) tween = null; else more = true;
  }

  if (zoomT) {
    var ns = s + (zoomT.ts - s) * 0.3;
    if (Math.abs(zoomT.ts - s) < 0.0006) ns = zoomT.ts;
    x = zoomT.ax - (zoomT.ax - x) * ns / s;
    y = zoomT.ay - (zoomT.ay - y) * ns / s;
    s = ns;
    if (ns === zoomT.ts) zoomT = null; else more = true;
  }

  if (coasting) {
    x += vx; y += vy;
    vx *= 0.925; vy *= 0.925;
    if (Math.abs(vx) < 0.07 && Math.abs(vy) < 0.07) coasting = false;
    else more = true;
  }

  world.style.transform =
    'translate3d(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px,0) scale(' + s.toFixed(4) + ')';

  /* Miro-style canvas grid: the dots pan and zoom with the world instead of
     sitting still in screen space. The gradient's dot radius is absolute, so
     only the tile spacing scales - dots stay crisp at every zoom. Doubling /
     halving keeps the spacing inside a readable 15-60px band, which is how a
     real infinite canvas subdivides its grid. */
  var g = 26 * s;
  while (g < 15) g *= 2;
  while (g > 60) g /= 2;
  var gs = g.toFixed(2) + 'px';
  if (gs !== lastGrid) {
    lastGrid = gs;
    vp.style.backgroundSize = gs + ' ' + gs;
  }
  vp.style.backgroundPosition =
    (x % g).toFixed(1) + 'px ' + (y % g).toFixed(1) + 'px';

  if (more) schedule(); else idleSoon();
}

/* keep will-change only while something is actually moving */
var idleT = 0;
function busy() {
  if (!vp.classList.contains('moving')) vp.classList.add('moving');
  clearTimeout(idleT);
}
function idleSoon() {
  clearTimeout(idleT);
  idleT = setTimeout(function () { vp.classList.remove('moving'); }, 200);
}
function stopMotion() { tween = null; zoomT = null; coasting = false; vx = vy = 0; }


/* No row alignment is needed any more: the card header is clamped to a fixed
   height, the media tiles are a fixed 9:16 grid and everything else lives in
   the collapsible .det panel - so every collapsed card is exactly the same
   height and the rows line up by construction. The old alignRow() padded each
   anchor row to the tallest card ON THE WHOLE BOARD, which is what produced
   the large blank gaps inside short cards. */
function alignAll() {}

/* ------------------------------------------------------------- measuring */
function measureWorld() { W = world.offsetWidth; H = world.offsetHeight; }

/* Lock every card to its real rendered height and every lane to its real
   height BEFORE enabling culling, so culled cards reserve exactly the space
   they occupied and the board stays pixel-stable while panning. */
function lockSizes() {
  alignAll();
  var cards = world.querySelectorAll('.card,.cell'),
      lanes = world.querySelectorAll('.lane'),
      cw = [], ch = [], lh = [], i;
  for (i = 0; i < cards.length; i++) { cw[i] = cards[i].offsetWidth; ch[i] = cards[i].offsetHeight; }
  for (i = 0; i < lanes.length; i++) lh[i] = lanes[i].offsetHeight;
  for (i = 0; i < cards.length; i++)
    cards[i].style.containIntrinsicSize = cw[i] + 'px ' + ch[i] + 'px';
  for (i = 0; i < lanes.length; i++) lanes[i].style.height = lh[i] + 'px';
  world.classList.add('live');
  measureWorld();
}

/* re-lock one card + its lane after a prompt opens or closes */
function relock() {
  /* Opening a panel changes one card's height, which changes its lane's
     height. Clear and re-measure every card and lane so the culling
     placeholders stay exact and the board never jumps while panning.
     Culling must be OFF while measuring: a culled (off-screen) card with its
     intrinsic size cleared measures as empty, its lane shrinks, and after
     "Fit all" the lanes overlap. */
  var cards = world.querySelectorAll('.card,.cell'),
      lanes = world.querySelectorAll('.lane'), i;
  world.classList.remove('live');
  for (i = 0; i < cards.length; i++) cards[i].style.containIntrinsicSize = '';
  for (i = 0; i < lanes.length; i++) lanes[i].style.height = '';
  alignAll();
  var cw = [], ch = [], lh = [];
  for (i = 0; i < cards.length; i++) { cw[i] = cards[i].offsetWidth; ch[i] = cards[i].offsetHeight; }
  for (i = 0; i < lanes.length; i++) lh[i] = lanes[i].offsetHeight;
  for (i = 0; i < cards.length; i++)
    cards[i].style.containIntrinsicSize = cw[i] + 'px ' + ch[i] + 'px';
  for (i = 0; i < lanes.length; i++) lanes[i].style.height = lh[i] + 'px';
  world.classList.add('live');
  measureWorld();
}

/* ------------------------------------------------------------ navigation */
function tweenTo(nx, ny, ns, ms) {
  stopMotion();
  tween = { x0: x, y0: y, s0: s, x1: nx, y1: ny, s1: clamp(ns),
            t0: performance.now(), ms: ms || 430 };
  busy(); schedule();
}
function fit() {
  measureWorld();
  var L = nbw(), ns = clamp(Math.min((innerWidth - L - 50) / W, (innerHeight - 70) / H));
  tweenTo(L + (innerWidth - L - W * ns) / 2, (innerHeight - H * ns) / 2, ns);
}
/* columns layout: home frames the grid's rows from the video headings down to the final videos,
   at the left edge - the first videos at a readable size (the title and panels sit just above) */
function gridView() {
  var g = world.querySelector('section.cgrid');
  if (!g) return null;
  var outs = g.querySelectorAll('.cell.out'), bottom = g.offsetTop + g.offsetHeight, i;
  if (outs.length) { bottom = 0; for (i = 0; i < outs.length; i++) bottom = Math.max(bottom, outs[i].offsetTop + outs[i].offsetHeight); }
  var ns = clamp(Math.min(1, (innerHeight - 50) / (bottom - g.offsetTop + 20)));
  return { x: nbw() + 10 - g.offsetLeft * ns, y: 24 - g.offsetTop * ns, s: ns };
}
function home() {
  var gv = gridView();
  if (gv) { tweenTo(gv.x, gv.y, gv.s); return; }
  var l = world.querySelector('section.lane');
  if (!l) { fit(); return; }
  var ns = clamp(Math.min(0.95, (innerHeight - 40) / (l.offsetTop + l.offsetHeight + 30)));
  tweenTo(Math.max(nbw(), (innerWidth - (l.offsetLeft + l.offsetWidth + 70) * ns) / 2), 20, ns);
}
/* the newest video on the board - highest v<N> lane, so it follows the board
   as videos are added instead of being pinned to a hard-coded id */
function latestLane() {
  var ls = world.querySelectorAll('section.lane[id],.vh[id]'), best = null, bn = -1, m, i;
  for (i = 0; i < ls.length; i++) {
    m = /^v(\d+)$/.exec(ls[i].id);
    if (m && +m[1] > bn) { bn = +m[1]; best = ls[i]; }
  }
  return best || ls[ls.length - 1] || null;
}
function latest() {
  var l = latestLane();
  if (!l) { fit(); return; }
  /* columns layout: frame the newest video's whole column(s), heading to the last row */
  var g = l.classList.contains('vh') ? l.parentElement : null,
      lt = l.offsetTop, lh = g ? g.offsetTop + g.offsetHeight - l.offsetTop : l.offsetHeight;
  var L = nbw(), ns = clamp(Math.min(0.95, (innerWidth - L - 60) / (l.offsetWidth  + 40),
                                (innerHeight - 80) / (lh + 40)));
  tweenTo(Math.max(L + 20, L + (innerWidth - L - l.offsetWidth * ns) / 2) - l.offsetLeft * ns,
          40 - lt * ns, ns, 520);
}
function zoomBy(f, ax, ay) {
  var base = zoomT ? zoomT.ts : s;
  tween = null; coasting = false;
  zoomT = { ts: clamp(base * f),
            ax: ax === undefined ? innerWidth / 2 : ax,
            ay: ay === undefined ? innerHeight / 2 : ay };
  busy(); schedule();
}

/* ------------------------------------------------------------------ pan */
var panning = false, lx = 0, ly = 0, lt = 0, travel = 0, pid = null, dragged = false, downT = null;

/* touch: one finger pans (the pointer code below), two fingers pinch-zoom the
   board - not the page (#vp has touch-action:none). */
var tp = {}, tpn = 0, pinch = null;
function tpts() { var a = []; for (var k in tp) a.push(tp[k]); return a; }
function pinchStart() {
  var p = tpts(), dx = p[1].x - p[0].x, dy = p[1].y - p[0].y;
  stopMotion(); panning = false; vp.classList.remove('drag');
  pinch = { d0: Math.max(1, Math.hypot(dx, dy)), mx: (p[0].x + p[1].x) / 2, my: (p[0].y + p[1].y) / 2, s0: s, x0: x, y0: y };
  dragged = true;
}
function pinchMove() {
  var p = tpts(), dx = p[1].x - p[0].x, dy = p[1].y - p[0].y,
      mx = (p[0].x + p[1].x) / 2, my = (p[0].y + p[1].y) / 2,
      ns = clamp(pinch.s0 * Math.hypot(dx, dy) / pinch.d0);
  x = mx - (pinch.mx - pinch.x0) * ns / pinch.s0;
  y = my - (pinch.my - pinch.y0) * ns / pinch.s0;
  s = ns;
  busy(); schedule();
}
vp.addEventListener('pointerdown', function (e) {
  if (e.pointerType === 'touch') {
    if (!tp[e.pointerId]) tpn++;
    tp[e.pointerId] = { x: e.clientX, y: e.clientY };
    if (tpn === 2) { pinchStart(); e.preventDefault(); return; }
    if (tpn > 2) { e.preventDefault(); return; }
  }
  if (e.button !== 0 && e.button !== 1) return;
  if (e.target.closest(NODRAG)) return;
  stopMotion();
  panning = true; travel = 0; dragged = false; downT = e.target;
  lx = e.clientX; ly = e.clientY; lt = e.timeStamp;
  pid = e.pointerId;
  try { vp.setPointerCapture(pid); } catch (_) {}
  vp.classList.add('drag');
  e.preventDefault();
}, { passive: false });

vp.addEventListener('pointermove', function (e) {
  if (e.pointerType === 'touch' && tp[e.pointerId]) {
    tp[e.pointerId] = { x: e.clientX, y: e.clientY };
    if (pinch) { if (tpn === 2) pinchMove(); return; }
  }
  if (!panning) return;
  var pts = (e.getCoalescedEvents && e.getCoalescedEvents()) || [e];
  if (!pts.length) pts = [e];
  for (var i = 0; i < pts.length; i++) {
    var p = pts[i],
        dx = p.clientX - lx, dy = p.clientY - ly,
        dt = Math.max(1, p.timeStamp - lt);
    x += dx; y += dy;
    travel += Math.abs(dx) + Math.abs(dy);
    var f = Math.min(1, dt / 26);
    vx = vx * (1 - f) + (dx * 16 / dt) * f;
    vy = vy * (1 - f) + (dy * 16 / dt) * f;
    lx = p.clientX; ly = p.clientY; lt = p.timeStamp;
  }
  if (travel > 6) dragged = true;
  busy(); schedule();
}, { passive: true });

function endPan() {
  if (!panning) return;
  panning = false;
  /* a press on a picture that did not become a drag opens it full size. Done here, not in the click
     handler: with the pointer captured for panning, Chrome sends that click to #vp, not to the picture. */
  var dt = downT; downT = null;
  if (!dragged && dt && dt.closest) {
    var im = dt.closest('.mimg');
    if (im && im.getAttribute('data-full')) openLb(im.getAttribute('data-full'));
  }
  vp.classList.remove('drag');
  if (pid !== null) { try { vp.releasePointerCapture(pid); } catch (_) {} pid = null; }
  if (dragged && Math.abs(vx) + Math.abs(vy) > 0.9) {
    vx = Math.max(-70, Math.min(70, vx));
    vy = Math.max(-70, Math.min(70, vy));
    coasting = true; busy(); schedule();
  } else { vx = vy = 0; idleSoon(); }
}
function endTouch(e) {
  if (e.pointerType !== 'touch' || !tp[e.pointerId]) return;
  delete tp[e.pointerId]; tpn--;
  if (pinch && tpn < 2) { pinch = null; panning = false; vx = vy = 0; idleSoon(); }
}
['pointerup', 'pointercancel'].forEach(function (t) { vp.addEventListener(t, function (e) { endTouch(e); endPan(); }); });

/* swallow the click that ends a drag */
vp.addEventListener('click', function (e) {
  if (dragged) { dragged = false; e.stopPropagation(); e.preventDefault(); }
}, true);

vp.addEventListener('dragstart', function (e) { e.preventDefault(); });
vp.addEventListener('selectstart', function (e) {
  if (!e.target.closest('.p-text,textarea,input')) e.preventDefault();
});

/* --------------------------------------------------------- wheel / pinch */
vp.addEventListener('wheel', function (e) {
  e.preventDefault();
  stopMotion();
  if (e.ctrlKey || e.metaKey) {          // pinch or ctrl+wheel — direct, no easing
    var ns = clamp(s * Math.exp(-e.deltaY * 0.0022));
    x = e.clientX - (e.clientX - x) * ns / s;
    y = e.clientY - (e.clientY - y) * ns / s;
    s = ns;
  } else {
    var k = e.deltaMode === 1 ? 18 : (e.deltaMode === 2 ? innerHeight : 1);
    x -= e.deltaX * k;
    y -= e.deltaY * k;
  }
  busy(); schedule();
}, { passive: false });

vp.addEventListener('dblclick', function (e) {
  if (e.target.closest(NODRAG)) return;
  zoomBy(1.7, e.clientX, e.clientY);
});

document.getElementById('zfit').onclick  = fit;
document.getElementById('zlast').onclick = latest;

/* -------------------------------------------------------- video facades */
var live = [];      /* the mounted facades: one, or two for "side by side" */
function unmount() {
  for (var i = 0; i < live.length; i++) {
    var v = live[i].querySelector('video');
    if (v) { v.pause(); v.removeAttribute('src'); v.load(); v.remove(); }
    live[i].classList.remove('playing');
  }
  live = [];
}
function put(fac, muted) {
  var v = document.createElement('video');
  v.src = fac.dataset.src;
  v.controls = true; v.preload = 'auto'; v.muted = !!muted;
  v.setAttribute('playsinline', '');
  fac.appendChild(v);
  fac.classList.add('playing');
  live.push(fac);
  return v;
}
function go(v) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
function mount(fac) {
  /* a lost take has no data-src - never mount an empty <video> */
  if (!fac.dataset.src) return;
  unmount();
  go(put(fac, false));
}
/* columns layout: the reference reel (muted) and our clip start together and stay in step -
   our clip leads: play, pause and seek on it drive the reference */
function mountPair(btn) {
  var col = btn.getAttribute('data-col'),
      a = world.querySelector('.cell.ref[data-col="' + col + '"] .vfac'),
      b = btn.closest('.cell').querySelector('.vfac');
  if (!a || !b || !a.dataset.src || !b.dataset.src) return;
  unmount();
  var va = put(a, true), vb = put(b, false);
  vb.addEventListener('play', function () { va.currentTime = vb.currentTime; go(va); });
  vb.addEventListener('pause', function () { va.pause(); });
  vb.addEventListener('seeked', function () { va.currentTime = vb.currentTime; });
  vb.addEventListener('ended', function () { va.pause(); });
  go(vb);
}

/* -------------------------------------------------------------- lightbox */
function openLb(src) { lbImg.src = src; lb.classList.add('on'); }
function closeLb() { lb.classList.remove('on'); lbImg.removeAttribute('src'); }
lb.addEventListener('click', closeLb);

/* ---------------------------------------------------------------- clicks */
document.addEventListener('click', function (e) {
  var c = e.target.closest('.copy');
  if (c) {
    e.stopPropagation();
    var t = c.closest('.prompt').querySelector('.p-text'), txt = t.textContent;
    var done = function () {
      c.textContent = 'Copied'; c.classList.add('ok');
      setTimeout(function () { c.textContent = 'Copy'; c.classList.remove('ok'); }, 1200);
    };
    var fb = function () {
      var a = document.createElement('textarea');
      a.value = txt; a.style.cssText = 'position:fixed;opacity:0';
      document.body.appendChild(a); a.select();
      try { document.execCommand('copy'); } catch (_) {}
      a.remove(); done();
    };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(done, fb);
    else fb();
    return;
  }

  var pb = e.target.closest('.pair');
  if (pb) { mountPair(pb); return; }

  var f = e.target.closest('.vfac');
  if (f) { if (!f.classList.contains('playing')) mount(f); return; }

  var d = e.target.closest('.d-head');
  if (d) {
    var dc = d.closest('.card,.cell');
    dc.classList.toggle('open');
    relock(dc);
    return;
  }

  var h = e.target.closest('.p-head');
  if (h) {
    h.parentElement.classList.toggle('open');
    relock();
    return;
  }

  var im = e.target.closest('.mimg');
  if (im && im.getAttribute('data-full')) { openLb(im.getAttribute('data-full')); return; }
});

/* -------------------------------------------------------------- keyboard */
addEventListener('keydown', function (e) {
  if (e.target.matches && e.target.matches('input,textarea')) return;
  if (e.key === 'Escape') { if (lb.classList.contains('on')) closeLb(); else unmount(); return; }
  if (e.key === 'e' || e.key === 'E') {
    var cs = world.querySelectorAll('.card,.cell.drw:not(.empty)'),
        anyClosed = false, i;
    for (i = 0; i < cs.length; i++) if (!cs[i].classList.contains('open')) anyClosed = true;
    for (i = 0; i < cs.length; i++) cs[i].classList.toggle('open', anyClosed);
    relock(null);
    return;
  }
  if (e.key === '0') fit();
  else if (e.key === '1') home();
  else if (e.key === '2') latest();
  else if (e.key === '+' || e.key === '=') zoomBy(1.3);
  else if (e.key === '-' || e.key === '_') zoomBy(1 / 1.3);
});

addEventListener('resize', function () { measureWorld(); }, { passive: true });

/* ------------------------------------------------------------------ boot */
function boot() {
  lockSizes();
  var l = world.querySelector('section.lane'), gv = gridView();
  if (gv) { x = gv.x; y = gv.y; s = gv.s; }
  else if (l) {
    s = clamp(Math.min(0.95, (innerHeight - 40) / (l.offsetTop + l.offsetHeight + 30)));
    x = Math.max(nbw(), (innerWidth - (l.offsetLeft + l.offsetWidth + 70) * s) / 2);
    y = 20;
  }
  schedule();
}
/* ---- missing-thumbnail fallback -------------------------------------------
   If a .webp thumb is absent (a clip was added but not yet processed) the
   image silently falls back to the full-resolution original, so a card can
   never render blank. Final-lane posters have no original, so the facade just
   shows its black tile + play button and stays clickable.
   `error` does not bubble, hence capture phase.                              */
addEventListener('error', function (e) {
  var t = e.target;
  if (!t || t.tagName !== 'IMG' || t.dataset.fb) return;
  t.dataset.fb = '1';
  var full = t.getAttribute('data-full');
  if (full) { t.src = full; }
  else { t.style.visibility = 'hidden'; }
}, true);

if (document.readyState === 'complete') boot();
else addEventListener('load', boot);

})();

/* ---------- notes: autosave to the browser AND to board_notes.txt next to this board ---------- */
(function () {
  var nb = document.getElementById('nb'); if (!nb) return;
  var slug = nb.getAttribute('data-key') || 'board', KEY = 'vb.notes.' + slug, TKEY = KEY + '.t', OKEY = KEY + '.open',
      FNAME = 'board_notes.txt',
      ta = nb.querySelector('textarea'), head = nb.querySelector('.nb-h'), st = nb.querySelector('.nb-st'),
      cnt = nb.querySelector('.nb-c'), linkB = document.getElementById('nblink'), fileL = nb.querySelector('.nb-file'),
      t = 0, handle = null, perm = 'none', asking = false;
  function get(k) { try { return localStorage.getItem(k); } catch (_) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); return true; } catch (_) { return false; } }
  function stamp() { var d = new Date(); return ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2); }
  function say(s, cls) { st.textContent = s; st.className = 'nb-st' + (cls ? ' ' + cls : ''); }
  function count() { var v = ta.value, w = v.trim() ? v.trim().split(/\s+/).length : 0; cnt.textContent = w + (w === 1 ? ' word' : ' words'); }
  function idb(mode, fn) {
    try { var r = indexedDB.open('vb-notes', 1);
      r.onupgradeneeded = function () { r.result.createObjectStore('h'); };
      r.onsuccess = function () { var tx = r.result.transaction('h', mode); fn(tx.objectStore('h')); };
    } catch (_) {}
  }
  function show() {
    if (!window.showOpenFilePicker) { linkB.style.display = 'none'; fileL.textContent = ''; return; }
    if (!handle) { linkB.style.display = ''; linkB.textContent = 'Connect ' + FNAME + ' (once)'; fileL.textContent = ''; return; }
    linkB.style.display = 'none';
    fileL.textContent = perm === 'granted' ? '✓ ' + handle.name : '⟳ click here to reconnect ' + handle.name;
  }
  /* Every read and write of board_notes.txt goes through ONE queue, so a merge
     always finishes before the next save starts and two saves never overlap
     (an autosave landing in the middle of a reconnect merge used to be able to
     overwrite the file's text). */
  var q = Promise.resolve();
  function serial(fn) { var p = q.then(fn, fn); q = p.then(function () {}, function () {}); return p; }
  async function rawWrite(text) {
    if (!handle || perm !== 'granted') return false;
    try { var w = await handle.createWritable(); await w.write(text); await w.close(); return true; } catch (_) { return false; }
  }
  function writeFile() { return serial(function () { return rawWrite(ta.value); }); }
  /* on connect / reconnect: never lose text - if both copies changed, both are kept */
  function sync() {
    return serial(async function () {
      try {
        var f = await handle.getFile(), ft = await f.text(), lt = +(get(TKEY) || 0), lv = ta.value;
        if (ft === lv) { }
        else if (!lv.trim() || ft.indexOf(lv) !== -1) { ta.value = ft; }            /* file already holds everything */
        else if (!ft.trim() || lv.indexOf(ft) !== -1) { await rawWrite(ta.value); }  /* browser copy holds everything */
        else {                                                                      /* both changed: keep both */
          ta.value = f.lastModified > lt ? ft + '\n\n— also typed in this browser —\n' + lv
                                         : lv + '\n\n— also in ' + handle.name + ' —\n' + ft;
          await rawWrite(ta.value);
        }
        set(KEY, ta.value); set(TKEY, String(Date.now())); count();
        say('Synced with ' + handle.name + ' ' + stamp(), 'ok');
      } catch (_) { say('Could not read ' + (handle ? handle.name : FNAME), 'warn'); }
    });
  }
  async function ensure() {
    if (!handle || perm === 'granted' || asking) return;
    asking = true;
    try { perm = await handle.requestPermission({ mode: 'readwrite' }); } catch (_) {}
    asking = false; show(); if (perm === 'granted') sync();
  }
  async function flush() {
    clearTimeout(t); t = 0;
    var ok = set(KEY, ta.value); set(TKEY, String(Date.now()));
    if (handle && perm !== 'granted') await ensure();
    var f = await writeFile();
    if (f) say('Autosaved ' + stamp() + ' · ' + handle.name, 'ok');
    else if (ok) say('Autosaved ' + stamp() + (handle ? '' : ' · browser only'), handle ? 'warn' : 'ok');
    else say('Could not save — copy your text somewhere', 'warn');
  }
  ta.value = get(KEY) || ''; count();
  /* folded by default on a phone (the panel sits at the bottom there and would cover the board) */
  var o = get(OKEY);
  if (o === '0' || (o === null && innerWidth <= 700)) nb.classList.remove('open'); else nb.classList.add('open');
  show();
  idb('readonly', function (s) { var q = s.get(slug); q.onsuccess = async function () {
    if (!q.result) { show(); return; }
    handle = q.result;
    try { perm = await handle.queryPermission({ mode: 'readwrite' }); } catch (_) {}
    show(); if (perm === 'granted') sync();
  }; });
  linkB.addEventListener('click', async function () {
    try {
      var hs = await window.showOpenFilePicker({ multiple: false, types: [{ description: 'Board notes', accept: { 'text/plain': ['.txt'] } }] });
      handle = hs[0]; perm = await handle.requestPermission({ mode: 'readwrite' });
      idb('readwrite', function (s) { try { s.put(handle, slug); } catch (_) {} });
      show(); if (perm === 'granted') sync();
    } catch (_) {}
  });
  fileL.addEventListener('click', ensure);
  nb.addEventListener('pointerdown', function () { if (handle && perm !== 'granted') ensure(); });
  head.addEventListener('click', function () { var open = !nb.classList.contains('open');
    nb.classList.toggle('open', open); set(OKEY, open ? '1' : '0'); dispatchEvent(new Event('resize')); });
  ta.addEventListener('input', function () { count(); say('Saving…'); clearTimeout(t); t = setTimeout(flush, 400); });
  ta.addEventListener('blur', function () { if (t) flush(); });
  addEventListener('pagehide', function () { if (t) { clearTimeout(t); set(KEY, ta.value); set(TKEY, String(Date.now())); writeFile(); } });
  document.addEventListener('visibilitychange', function () { if (document.hidden && t) flush(); });
  ta.addEventListener('wheel', function (e) { e.stopPropagation(); });
})();

function nbw() { var n = document.getElementById('nb'); if (!n || innerWidth <= 700) return 0; var r = n.getBoundingClientRect(); return r.right + 20; }
/* ---------- notes panel: remember its size ---------- */
(function () {
  var nb = document.getElementById('nb'); if (!nb) return;
  var K = 'vb.notes.' + (nb.getAttribute('data-key') || 'board') + '.size';
  try { var s = JSON.parse(localStorage.getItem(K) || 'null'); if (s) { nb.style.width = s.w + 'px'; nb.style.height = s.h + 'px'; } } catch (_) {}
  if (window.ResizeObserver) new ResizeObserver(function () {
    if (!nb.classList.contains('open')) return;
    try { localStorage.setItem(K, JSON.stringify({ w: nb.offsetWidth, h: nb.offsetHeight })); } catch (_) {}
  }).observe(nb);
  ['wheel', 'pointerdown', 'dblclick'].forEach(function (t) { nb.addEventListener(t, function (e) { e.stopPropagation(); }); });
})();
/* ---------- review: approve / reject lines for Claude, review filter ---------- */
(function () {
  var nbk = document.getElementById('nb'), KEY = 'vb.review.' + ((nbk && nbk.getAttribute('data-key')) || 'board'), dec = {};
  try { dec = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (_) { dec = {}; }
  var toast = document.getElementById('toast'), tt = 0;
  function say(m) { toast.textContent = m; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('on'); }, 2600); }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(dec)); } catch (_) {} }
  function copy(txt) {
    var fb = function () { var a = document.createElement('textarea'); a.value = txt; a.style.cssText = 'position:fixed;opacity:0';
      document.body.appendChild(a); a.select(); try { document.execCommand('copy'); } catch (_) {} a.remove(); };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(function () {}, fb); else fb();
  }
  function paint(card) {
    var d = dec[card.getAttribute('data-shot')];
    card.classList.toggle('dec-ok', !!d && d.v === 'ok');
    card.classList.toggle('dec-no', !!d && d.v === 'no');
  }
  function line(card, v, why) {
    var file = card.getAttribute('data-file') || '';
    return (v === 'ok' ? 'APPROVE ' : 'REJECT ') + file + (why ? ' — ' + why : '');
  }
  var cards = document.querySelectorAll('[data-shot][data-status]'), dirty = false;
  for (var i = 0; i < cards.length; i++) {
    var sh = cards[i].getAttribute('data-shot');
    /* a decision only matters while the card is FOR REVIEW with the same file - drop leftovers
       (card approved/rejected since, or a new take is under review now) */
    if (dec[sh] && (cards[i].getAttribute('data-status') !== 'review' ||
        (dec[sh].file || '') !== (cards[i].getAttribute('data-file') || ''))) { delete dec[sh]; dirty = true; }
    paint(cards[i]);
  }
  if (dirty) save();
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.rv-b');
    if (!b) return;
    e.stopPropagation();
    var card = b.closest('[data-shot]'), shot = card.getAttribute('data-shot'), v = b.classList.contains('ok') ? 'ok' : 'no', why = '';
    if (dec[shot] && dec[shot].v === v) { delete dec[shot]; save(); paint(card); say('Cleared ' + shot); return; }
    if (v === 'no') {
      why = window.prompt('What is wrong with ' + shot + '? (one line)', '');
      if (why === null) return;          /* Cancel means no decision */
    }
    dec[shot] = { v: v, why: why, file: card.getAttribute('data-file') || '', line: line(card, v, why) };
    save(); paint(card); copy(dec[shot].line);
    say('Copied: ' + dec[shot].line);
  }, true);
  document.getElementById('zcopy').onclick = function () {
    var ks = Object.keys(dec);
    if (!ks.length) { say('No decisions yet — use Approve / Reject on a card'); return; }
    copy(ks.map(function (k) { return dec[k].line; }).join('\n'));
    say('Copied ' + ks.length + ' decision' + (ks.length > 1 ? 's' : '') + ' — paste them to Claude');
  };
  var rb = document.getElementById('zreview');
  var waiting = document.querySelectorAll('[data-shot][data-status="review"]'), n = waiting.length,
      nf = document.querySelectorAll('[data-shot][data-status="review"][data-stage="frame"]').length,
      nr = document.querySelectorAll('[data-shot][data-status="review"][data-stage="refs"]').length,
      nc = n - nf - nr, kinds = [];
  if (nr) kinds.push('references');
  if (nf) kinds.push('frames');
  if (nc) kinds.push('clips');
  rb.textContent = 'Review ' + n + (n ? ' · ' + kinds.join(' + ') : '');
  rb.onclick = function () {
    if (!n) { say('Nothing is waiting for review'); return; }
    var on = !document.body.classList.contains('review-mode');
    document.body.classList.toggle('review-mode', on); rb.classList.toggle('on', on);
  };
})();
/* ---------- dark / light switch (button #ztheme, key D; remembered per board) ---------- */
(function () {
  var b = document.getElementById('ztheme'); if (!b) return;
  var nbk = document.getElementById('nb'), K = 'vb.theme.' + ((nbk && nbk.getAttribute('data-key')) || 'board'),
      root = document.documentElement;
  function paint() { var d = root.getAttribute('data-theme') === 'dark'; b.textContent = d ? 'Light' : 'Dark'; b.classList.toggle('on', d); }
  function flip() {
    var d = root.getAttribute('data-theme') !== 'dark';
    if (d) root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
    try { localStorage.setItem(K, d ? 'dark' : 'light'); } catch (_) {}
    paint();
  }
  b.addEventListener('click', flip);
  addEventListener('keydown', function (e) {
    if (e.target.matches && e.target.matches('input,textarea')) return;
    if ((e.key === 'd' || e.key === 'D') && !e.ctrlKey && !e.metaKey && !e.altKey) flip();
  });
  paint();
})();
