(function () {
  var d = document, root = d.documentElement;
  root.classList.add('js');

  // Start every new page at the top. Links to a section (#anchor) still land on
  // that section, and back/forward keeps the browser's own scroll restoration.
  (function () {
    var nav = window.performance && performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
    if (location.hash || (nav && nav.type === 'back_forward')) return;
    var userScrolled = false;
    function mark() { userScrolled = true; }
    ['wheel', 'touchmove', 'keydown', 'mousedown'].forEach(function (ev) { addEventListener(ev, mark, { passive: true, once: true }); });
    function top() {
      if (userScrolled) return;
      var prev = root.style.scrollBehavior;
      root.style.scrollBehavior = 'auto';
      window.scrollTo(0, 0);
      // when the page is shown inside a taller frame (as in a preview), bring the frame's top into view too
      try { if (window.top !== window.self) root.scrollIntoView({ block: 'start', behavior: 'auto' }); } catch (e) {}
      root.style.scrollBehavior = prev;
    }
    top();
    addEventListener('load', top);
    addEventListener('pageshow', function (e) { if (!e.persisted) top(); });
  })();

  // mobile menu
  var burger = d.querySelector('.burger'), nav = d.getElementById('nav');
  if (burger && nav) {
    var setMenu = function (open) {
      nav.classList.toggle('open', open);
      root.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    burger.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    addEventListener('resize', function () { if (innerWidth > 980 && nav.classList.contains('open')) setMenu(false); });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { setMenu(false); burger.focus(); }
    });
  }

  // reading progress + table of contents highlight (articles only)
  var bar = d.querySelector('.progress'), article = d.querySelector('.prose');
  var tocLinks = [].slice.call(d.querySelectorAll('.toc a'));
  var heads = tocLinks.map(function (a) { return d.getElementById(decodeURIComponent(a.hash.slice(1))); }).filter(Boolean);
  function onScroll() {
    if (bar && article) {
      var r = article.getBoundingClientRect();
      var total = r.height - innerHeight * 0.6;
      var p = Math.min(1, Math.max(0, -r.top / (total || 1)));
      bar.style.width = (p * 100).toFixed(1) + '%';
    }
    if (heads.length) {
      var cur = 0;
      for (var i = 0; i < heads.length; i++) if (heads[i].getBoundingClientRect().top < 140) cur = i;
      tocLinks.forEach(function (a, i) { a.classList.toggle('on', i === cur); });
    }
  }
  if (bar || heads.length) { addEventListener('scroll', onScroll, { passive: true }); onScroll(); }

  // reveal on scroll
  var els = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // copy link
  var copy = d.querySelector('[data-copy]');
  if (copy && navigator.clipboard) {
    copy.addEventListener('click', function () {
      navigator.clipboard.writeText(copy.getAttribute('data-copy')).then(function () {
        var t = copy.textContent; copy.textContent = 'Copied'; setTimeout(function () { copy.textContent = t; }, 1600);
      });
    });
  }

  // newsletter sign-up (Kit)
  [].forEach.call(d.querySelectorAll('form.signup'), function (f) {
    var msg = f.querySelector('.msg'), btn = f.querySelector('button'), em = f.querySelector('input[type=email]');
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      f.classList.remove('err', 'ok');
      if (f.website && f.website.value) return;
      if (!em.value || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em.value)) { f.classList.add('err'); msg.textContent = 'Please enter a valid email address.'; em.focus(); return; }
      if (!f.dataset.form) { f.classList.add('ok'); msg.textContent = 'Thanks! The newsletter launches very soon. Follow me on LinkedIn in the meantime.'; return; }
      btn.disabled = true; msg.textContent = 'Subscribing…';
      var body = new FormData(); body.append('email_address', em.value);
      fetch(f.action, { method: 'POST', body: body, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw r; f.classList.add('ok'); msg.textContent = 'Nearly there. Check your inbox and click the link to confirm.'; })
        .catch(function () { f.submit(); })
        .then(function () { btn.disabled = false; });
    });
  });
})();

/* Featured in coverflow: rotates every 8s, pauses on hover/focus, honours reduced motion, has pause button */
(function () {
  var cf = document.querySelector('.cf');
  if (!cf) return;
  var stage = cf.querySelector('.cf-stage');
  var cards = [].slice.call(cf.querySelectorAll('.cf-card'));
  var dots = [].slice.call(cf.querySelectorAll('[data-cf-dot]'));
  var status = cf.querySelector('.cf-status');
  var n = cards.length, i = 0, paused = false, hover = false, swiped = false;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { paused = true; cf.classList.add('is-paused'); }
  cf.classList.add('is-ready');
  cf.querySelector('.cf-controls').hidden = false;
  function layout() {
    var w = stage.clientWidth, cw = cards[0].offsetWidth;
    var step = Math.min(150, Math.max(70, (w - cw) / 2 + 20));
    cards.forEach(function (c, k) {
      var o = k - i; if (o > n / 2) o -= n; if (o < -n / 2) o += n;
      var a = Math.abs(o), s = o < 0 ? -1 : 1;
      var x = o === 0 ? 0 : s * (step + (a - 1) * step * 0.45);
      c.style.transform = 'translateX(' + x + 'px) scale(' + (o === 0 ? 1 : a === 1 ? 0.78 : 0.62) + ') rotateY(' + (o === 0 ? 0 : -s * 38) + 'deg)';
      c.style.zIndex = 10 - a;
      c.style.opacity = a > 2 ? 0 : a === 2 ? 0.45 : 1;
      c.style.filter = 'brightness(' + (o === 0 ? 1 : a === 1 ? 0.7 : 0.5) + ')';
      c.style.pointerEvents = a > 2 ? 'none' : 'auto';
      c.classList.toggle('is-active', o === 0);
      c.setAttribute('aria-hidden', a > 1 ? 'true' : 'false');
      c.tabIndex = a > 1 ? -1 : 0;
    });
    dots.forEach(function (d, k) { d.setAttribute('aria-current', k === i ? 'true' : 'false'); });
    var t = cards[i].querySelector('.cf-outlet');
    status.textContent = (t ? t.textContent : '') + ' (' + (i + 1) + ' of ' + n + ')';
  }
  function go(k) { i = ((k % n) + n) % n; layout(); }
  cards.forEach(function (c, k) {
    c.addEventListener('click', function (e) {
      if (swiped) { e.preventDefault(); swiped = false; return; }
      if (k !== i) { e.preventDefault(); go(k); }
    });
  });
  dots.forEach(function (d, k) { d.addEventListener('click', function () { go(k); }); });
  cf.addEventListener('click', function (e) {
    var b = e.target.closest('[data-cf]'); if (!b) return;
    var a = b.getAttribute('data-cf');
    if (a === 'prev') go(i - 1);
    if (a === 'next') go(i + 1);
    if (a === 'toggle') {
      paused = !paused; cf.classList.toggle('is-paused', paused);
      b.setAttribute('aria-label', paused ? 'Play rotation' : 'Pause rotation');
      status.setAttribute('aria-live', paused ? 'polite' : 'off');
    }
  });
  cf.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { go(i - 1); e.preventDefault(); }
    if (e.key === 'ArrowRight') { go(i + 1); e.preventDefault(); }
  });
  cf.addEventListener('mouseenter', function () { hover = true; });
  cf.addEventListener('mouseleave', function () { hover = false; });
  cf.addEventListener('focusin', function () { hover = true; });
  cf.addEventListener('focusout', function (e) { if (!cf.contains(e.relatedTarget)) hover = false; });
  var sx = null, sy = null, touchTimer;
  stage.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; sy = e.touches[0].clientY; swiped = false; hover = true; clearTimeout(touchTimer); }, { passive: true });
  stage.addEventListener('touchend', function (e) {
    if (sx === null) return;
    var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
    if (Math.abs(dx) > 35 && Math.abs(dx) > Math.abs(dy)) { swiped = true; go(i + (dx < 0 ? 1 : -1)); }
    sx = null;
    touchTimer = setTimeout(function () { hover = false; }, 6000); // let the reader finish before rotating again
  });
  addEventListener('resize', layout);
  setInterval(function () { if (!paused && !hover && !document.hidden) go(i + 1); }, 8000);
  layout();
})();

/* Learning paths: progress saved in this browser only (no account, nothing sent anywhere) */
(function () {
  var el = document.getElementById('lp-data');
  if (!el) return;
  var PATHS = JSON.parse(el.textContent), BASE = (window.LP_BASE || '').replace(/\/\.$/, '');
  var byId = {}; PATHS.forEach(function (p) { byId[p.id] = p; });
  var KEY = 'sm-paths-v1';
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || { read: {}, last: null }; } catch (e) { return { read: {}, last: null }; } }
  function save(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
  var S = load(); S.read = S.read || {};
  function isRead(slug) { return !!S.read[slug]; }
  function doneCount(p) { return p.slugs.filter(isRead).length; }
  function nextIndex(p) { for (var i = 0; i < p.slugs.length; i++) if (!isRead(p.slugs[i])) return i; return -1; }
  function postUrl(slug, pid) { return BASE + '/post/' + slug + (window.LP_EXT || '') + '?path=' + pid; }
  function current() {
    if (S.last && byId[S.last]) { var p = byId[S.last], d = doneCount(p); if (d > 0 && d < p.slugs.length) return p; }
    var best = null; PATHS.forEach(function (p) { var d = doneCount(p); if (d > 0 && d < p.slugs.length && (!best || d > doneCount(best))) best = p; });
    return best;
  }
  function setRead(slug, on, pid) { if (on) S.read[slug] = Date.now(); else delete S.read[slug]; if (pid) S.last = pid; save(S); }

  // ---------- home teaser ----------
  var teaser = document.querySelector('.lp-teaser');
  if (teaser) {
    var cur = current();
    if (cur) {
      var ni = nextIndex(cur), d = doneCount(cur);
      teaser.href = postUrl(cur.slugs[ni], cur.id);
      teaser.querySelector('[data-lp-teaser-msg]').textContent = "Welcome back. You're " + d + ' of ' + cur.slugs.length + ' articles into ' + cur.title + '. Next up: ' + cur.titles[ni] + '.';
      teaser.querySelector('[data-lp-teaser-cta]').textContent = 'Continue your path';
    }
  }

  // ---------- hub map ----------
  var map = document.querySelector('.lp-map');
  if (map) {
    var lines = [].slice.call(map.querySelectorAll('.lp-line'));
    function pick(id) {
      lines.forEach(function (l) {
        var on = l.dataset.line === id;
        l.classList.toggle('on', on);
        l.querySelector('.lp-tag').setAttribute('aria-pressed', on ? 'true' : 'false');
        [].forEach.call(l.querySelectorAll('.lp-stn'), function (a) { a.tabIndex = on ? 0 : -1; });
      });
      [].forEach.call(document.querySelectorAll('[data-detail]'), function (d) { d.hidden = d.dataset.detail !== id; });
    }
    PATHS.forEach(function (p) {
      var ni = nextIndex(p), d = doneCount(p);
      [].forEach.call(map.querySelectorAll('[data-line="' + p.id + '"] .lp-stn'), function (a, k) {
        a.classList.toggle('done', isRead(a.dataset.slug));
        a.classList.toggle('here', k === ni);
      });
      [].forEach.call(document.querySelectorAll('[data-detail="' + p.id + '"] li'), function (li) { li.classList.toggle('done', isRead(li.dataset.slug)); });
      var cta = document.querySelector('[data-path-cta="' + p.id + '"]');
      if (cta) cta.textContent = d === p.slugs.length ? 'Read it again' : d ? 'Continue this path' : 'Start this path';
    });
    lines.forEach(function (l) { l.querySelector('.lp-tag').addEventListener('click', function () { pick(l.dataset.line); }); });
    var c = current();
    pick(c ? c.id : 'foundations');
    var w = document.querySelector('.lp-welcome');
    if (c && w) {
      var ni = nextIndex(c);
      w.querySelector('[data-lp-welcome]').textContent = "You're " + doneCount(c) + ' article' + (doneCount(c) === 1 ? '' : 's') + ' into ' + c.title + '.';
      var a = w.querySelector('[data-lp-continue]'); a.href = postUrl(c.slugs[ni], c.id); a.textContent = 'Continue: ' + c.titles[ni];
      w.hidden = false;
    }
  }

  // ---------- path page ----------
  var page = document.querySelector('.lp-page');
  if (page) {
    var P = byId[page.dataset.path];
    function paint() {
      var d = doneCount(P), n = P.slugs.length, ni = nextIndex(P);
      page.querySelector('[data-lp-count]').textContent = d;
      var mins = 0;
      [].forEach.call(page.querySelectorAll('.lp-st'), function (li, k) {
        var r = isRead(li.dataset.slug);
        li.classList.toggle('done', r); li.classList.toggle('here', k === ni);
        li.querySelector('[data-state]').textContent = r ? 'Read' : k === ni ? 'Up next' : 'Not started';
        var b = li.querySelector('.lp-mark'); b.textContent = r ? 'Read' : 'Mark as read'; b.setAttribute('aria-pressed', r ? 'true' : 'false');
        if (!r) mins += parseInt((li.querySelector('.meta').textContent.match(/(\d+) min/) || [0, 0])[1], 10);
      });
      [].forEach.call(page.querySelectorAll('.lp-rail li'), function (li, k) { li.classList.toggle('done', isRead(li.dataset.slug)); li.classList.toggle('here', k === ni); });
      var circ = 2 * Math.PI * 58;
      page.querySelector('[data-lp-ring]').style.strokeDasharray = (circ * d / n).toFixed(1) + ' ' + circ.toFixed(1);
      page.querySelector('[data-lp-left]').textContent = d === n ? 'Path complete' : mins + ' min to go';
      var f = page.querySelector('[data-lp-fill]');
      if (f) f.style.width = (d ? Math.min(100, ((d - 1 + (d < n ? .5 : 0)) / (n - 1)) * 100) : 0) + '%';
      var nx = page.querySelector('[data-lp-next]');
      if (d === n) { nx.textContent = 'Choose your next path'; nx.href = BASE + '/paths/'; }
      else { nx.textContent = d ? 'Continue: ' + P.titles[ni] : 'Start the first article'; nx.href = postUrl(P.slugs[ni], P.id); }
      var ey = page.querySelector('[data-lp-reward-eyebrow]'); if (ey) ey.textContent = d === n ? 'Path complete. Nice work.' : 'When you finish the path';
    }
    page.addEventListener('click', function (e) {
      var b = e.target.closest('[data-mark]'); if (!b) return;
      setRead(b.dataset.mark, !isRead(b.dataset.mark), P.id); paint();
    });
    paint();
  }

  // ---------- article inside a path ----------
  var bars = document.querySelectorAll('[data-lp-bar]');
  if (bars.length) {
    var slug = location.pathname.split('/').pop().replace(/\.html$/, '');
    var want = new URLSearchParams(location.search).get('path');
    var ids = [].map.call(bars, function (b) { return b.dataset.lpBar; });
    var pid = ids.indexOf(want) >= 0 ? want : (S.last && ids.indexOf(S.last) >= 0 && doneCount(byId[S.last]) > 0 ? S.last : null);
    if (pid) {
      S.last = pid; save(S);
      var bar = document.querySelector('[data-lp-bar="' + pid + '"]'); bar.hidden = false;
      [].forEach.call(bar.querySelectorAll('i[data-slug]'), function (i) { if (isRead(i.dataset.slug) && !i.classList.contains('here')) i.classList.add('done'); });
      var card = document.querySelector('[data-lp-next-card="' + pid + '"]'); if (card) card.hidden = false;
      [].forEach.call(document.querySelectorAll('[data-pn]'), function (n) { n.hidden = true; });
      var done = card && card.querySelector('[data-lp-done]');
      if (done) {
        // recommend the first path in the sequence that isn't finished yet, then two more
        var picks = [].slice.call(done.querySelectorAll('[data-pick]')), alts = [].slice.call(done.querySelectorAll('[data-alt]'));
        var open = picks.map(function (a) { return a.dataset.pick; }).filter(function (id) { var q = byId[id]; return q && doneCount(q) < q.slugs.length; });
        if (open.length) {
          picks.forEach(function (a) { a.hidden = a.dataset.pick !== open[0]; });
          alts.forEach(function (a) { a.hidden = open.slice(1, 3).indexOf(a.dataset.alt) < 0; });
          var p0 = byId[open[0]], ni = nextIndex(p0);
          if (ni > 0) { var a0 = done.querySelector('[data-pick="' + open[0] + '"]'); a0.href = postUrl(p0.slugs[ni], p0.id); a0.querySelector('em').textContent = 'Carry on with this path →'; }
        }
        var burst = function () {
          done.classList.add('go');
          if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
          var box = done.querySelector('.lp-confetti'), cols = [getComputedStyle(card).getPropertyValue('--c').trim() || '#a594ff', '#33d4e0', '#ff7ac6', '#ffd36e', '#ffffff'];
          for (var i = 0; i < 90; i++) {
            var c = document.createElement('i');
            c.style.cssText = 'left:' + (Math.random() * 100) + '%;background:' + cols[i % cols.length] + ';--x:' + (Math.random() * 160 - 80) + 'px;--r:' + (Math.random() * 720 - 360) + 'deg;--t:' + (1.6 + Math.random() * 1.6) + 's;--dl:' + (Math.random() * .6) + 's';
            box.appendChild(c);
          }
        };
        if ('IntersectionObserver' in window) new IntersectionObserver(function (es, o) { es.forEach(function (en) { if (en.isIntersecting) { burst(); o.disconnect(); } }); }, { threshold: .4 }).observe(done.querySelector('.lp-done-hero'));
        else burst();
      }
      // reaching the end of the article counts as read
      var end = document.querySelector('.post-end');
      if (end && 'IntersectionObserver' in window) {
        new IntersectionObserver(function (es, o) { es.forEach(function (en) { if (en.isIntersecting) { setRead(slug, true, pid); o.disconnect(); } }); }, { rootMargin: '0px 0px -20% 0px' }).observe(end);
      }
    }
  }
})();

/* Integration map: modes, animated data flow, app details */
(function () {
  var maps = document.querySelectorAll('.imap');
  if (!maps.length) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';
  [].forEach.call(maps, function (fig) {
    var D = JSON.parse(fig.querySelector('.imap-data').textContent);
    var svg = fig.querySelector('svg'), dotsG = fig.querySelector('.imap-dots');
    var edges = [].slice.call(fig.querySelectorAll('.imap-edge'));
    var note = fig.querySelector('.imap-mode-note'), info = fig.querySelector('.imap-info');
    var mode = fig.dataset.mode || 'hybrid', sel = null, dots = [];
    edges.forEach(function (e) { e._len = e.getTotalLength(); e.classList.add('r-' + e.dataset.route); });
    function active(e) {
      var a = e.dataset.app, r = e.dataset.route;
      if (a === 'core' || a === 'floor') return true;
      return (D.modes[mode].routes[a] || []).indexOf(r) >= 0;
    }
    function spawn() {
      dots.forEach(function (d) { d.el.remove(); }); dots = [];
      if (reduce) return;
      edges.forEach(function (e) {
        if (!active(e)) return;
        var col = e.dataset.route === 'erp' ? '#ffb86b' : e.dataset.route === 'mes' ? '#33d4e0' : '#c9bcff';
        var n = e.dataset.app === 'core' ? 4 : e.dataset.app === 'floor' ? 3 : 2;
        for (var k = 0; k < n; k++) {
          var c = document.createElementNS(NS, 'circle');
          c.setAttribute('r', e.dataset.app === 'core' ? 4.5 : 3.5); c.setAttribute('fill', col); c.style.color = col;
          dotsG.appendChild(c);
          dots.push({ el: c, e: e, t: k / n + Math.random() * .1, dir: k % 2 ? -1 : 1, v: (e.dataset.app === 'core' ? .0038 : .0026) * (0.8 + Math.random() * .4) });
        }
      });
    }
    function paint() {
      fig.dataset.mode = mode;
      [].forEach.call(fig.querySelectorAll('.imap-modes button'), function (b) { b.setAttribute('aria-pressed', b.dataset.mode === mode ? 'true' : 'false'); });
      note.textContent = D.modes[mode].note;
      edges.forEach(function (e) { e.classList.toggle('on', active(e)); e.classList.toggle('sel', !!sel && e.dataset.app === sel); });
      fig.classList.toggle('focus', !!sel);
      [].forEach.call(fig.querySelectorAll('.imap-app'), function (g) { g.classList.toggle('sel', g.dataset.app === sel); g.setAttribute('aria-pressed', g.dataset.app === sel ? 'true' : 'false'); });
      if (sel) {
        var A = D.apps[sel], R = D.modes[mode].routes[sel] || [];
        info.innerHTML = '<h4></h4><p></p><div class="imap-routes"><div class="erp"><b></b><span></span></div><div class="mes"><b></b><span></span></div></div><a></a>';
        info.querySelector('h4').textContent = A.name;
        info.querySelector('p').textContent = A.what;
        ['erp', 'mes'].forEach(function (r) {
          var d = info.querySelector('.imap-routes .' + r), on = A.module || R.indexOf(r) >= 0;
          d.classList.add(on ? 'on' : 'off');
          d.querySelector('b').textContent = A.labels ? A.labels[r === 'erp' ? 0 : 1] : A.module ? (r === 'erp' ? 'Where ERP fits' : 'What it replaces') : (r === 'erp' ? 'Via ERP' : 'Direct to MOM');
          d.querySelector('span').textContent = (on ? '' : 'Not used in this pattern. ') + A[r];
        });
        var a = info.querySelector('a'); a.href = (window.LP_BASE || '').replace(/\/\.$/, '') + A.link + (window.LP_EXT || ''); a.textContent = 'Read: ' + A.read + ' →';
      }
      spawn();
    }
    fig.addEventListener('click', function (e) {
      var b = e.target.closest('[data-mode]');
      if (b && b.tagName === 'BUTTON') { mode = b.dataset.mode; paint(); return; }
      var g = e.target.closest('.imap-app');
      if (g) { sel = sel === g.dataset.app ? null : g.dataset.app; paint(); }
    });
    fig.addEventListener('keydown', function (e) {
      var g = e.target.closest && e.target.closest('.imap-app');
      if (g && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); sel = sel === g.dataset.app ? null : g.dataset.app; paint(); }
    });
    var visible = true;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(fig);
    function tick() {
      if (visible && !document.hidden) dots.forEach(function (d) {
        d.t += d.v; if (d.t > 1) d.t -= 1;
        var p = d.e._len * (d.dir > 0 ? d.t : 1 - d.t), pt = d.e.getPointAtLength(p);
        d.el.setAttribute('cx', pt.x); d.el.setAttribute('cy', pt.y);
        d.el.style.opacity = (sel && d.e.dataset.app !== sel && d.e.dataset.app !== 'core' && d.e.dataset.app !== 'floor') ? .15 : Math.min(1, Math.sin(d.t * Math.PI) * 1.6);
      });
      requestAnimationFrame(tick);
    }
    paint();
    if (!reduce) requestAnimationFrame(tick);
  });
})();

/* Time to truth graphic: hover a stage to preview it, click or tap to pin it */
(function () {
  [].forEach.call(document.querySelectorAll('[data-ttt]'), function (fig) {
    var rows = [].slice.call(fig.querySelectorAll('.ttt-row'));
    var infos = [].slice.call(fig.querySelectorAll('.ttt-info'));
    var hover = window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches;
    var cur = 0, pinned = 0, dwell = null;
    if (hover) fig.addEventListener('mouseleave', function () { clearTimeout(dwell); show(pinned); });
    function show(n) {
      cur = n;
      fig.classList.toggle('has-active', n > 0);
      rows.forEach(function (r) { var on = +r.dataset.s === n; r.classList.toggle('on', on); r.querySelector('.ttt-label').setAttribute('aria-pressed', on ? 'true' : 'false'); });
      infos.forEach(function (i) { var on = +i.dataset.s === n; i.hidden = !on; if (on) i.style.setProperty('--rc', getComputedStyle(rows[n - 1]).getPropertyValue('--rc')); });
    }
    var panel = fig.querySelector('.ttt-panel');
    function reveal() { if (cur && innerWidth < 760) { var r = panel.getBoundingClientRect(); if (r.top > innerHeight - 120) panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); } }
    function pick(n) { pinned = pinned === n ? 0 : n; show(pinned); reveal(); }
    rows.forEach(function (r) {
      var n = +r.dataset.s;
      r.querySelector('.ttt-label').addEventListener('click', function () { pick(n); });
      r.querySelector('.ttt-track').addEventListener('click', function () { pick(n); });
      if (hover) {
        // a short dwell, so sweeping the mouse down to the detail panel doesn't flick through every stage
        r.addEventListener('mouseenter', function () { clearTimeout(dwell); dwell = setTimeout(function () { show(n); }, 140); });
        r.addEventListener('mouseleave', function () { clearTimeout(dwell); });
      }
      r.querySelector('.ttt-label').addEventListener('focus', function () { if (!pinned) show(n); });
    });
  });
})();

// recommendations: open the full text in a dialog
(function(){
  document.querySelectorAll('.recs').forEach(function(sec){
    var dlg=sec.querySelector('.rec-dlg'), box=dlg&&dlg.querySelector('.rec-dlg-in');
    if(!dlg) return;
    var last=null;
    sec.querySelectorAll('[data-rec]').forEach(function(b){
      b.addEventListener('click',function(){
        var t=document.getElementById('rec-'+b.dataset.rec); if(!t) return;
        box.innerHTML=''; box.appendChild(t.content.cloneNode(true)); last=b;
        if(dlg.showModal) dlg.showModal(); else dlg.setAttribute('open','');
        dlg.scrollTop=0;
      });
    });
    dlg.querySelector('.rec-x').addEventListener('click',function(){dlg.close()});
    dlg.addEventListener('click',function(e){if(e.target===dlg) dlg.close()});
    dlg.addEventListener('close',function(){if(last) last.focus()});
  });
})();

// articles page: multi-select topic filter (articles must have every selected tag)
(function(){
  var box=document.querySelector('[data-tagfilter]'); if(!box) return;
  var chips=[].slice.call(box.querySelectorAll('[data-tag]'));
  var cards=[].slice.call(document.querySelectorAll('.card[data-tags]'));
  var count=document.querySelector('[data-tag-count]'), empty=document.querySelector('[data-tag-empty]'), clear=box.querySelector('[data-tag-clear]');
  var tagsOf=function(c){return (c.getAttribute('data-tags')||'').split(' ')};
  var sel=[];
  try{var q=new URLSearchParams(location.search).get('tags'); if(q) sel=q.split(',').filter(function(t){return chips.some(function(c){return c.dataset.tag===t})});}catch(e){}
  function matches(c,s){var t=tagsOf(c);return s.every(function(x){return t.indexOf(x)>-1})}
  function apply(push){
    var shown=0;
    cards.forEach(function(c){var ok=matches(c,sel);c.hidden=!ok;if(ok){shown++;c.classList.add('in','vis','show')}});
    document.querySelectorAll('.wrap > section.section').forEach(function(s){
      var cs=s.querySelectorAll('.card[data-tags]'); if(!cs.length) return;
      s.hidden=![].some.call(cs,function(c){return !c.hidden});
      var h=s.querySelector('h2.label'); if(h) h.hidden=sel.length>0;
    });
    chips.forEach(function(ch){
      var on=sel.indexOf(ch.dataset.tag)>-1; ch.setAttribute('aria-pressed',on);
      var n=on?shown:cards.filter(function(c){return matches(c,sel.concat(ch.dataset.tag))}).length;
      ch.querySelector('span').textContent=n; ch.disabled=!on&&n===0;
    });
    if(count){count.hidden=!sel.length;count.textContent=shown+(shown===1?' article':' articles')+' match';}
    if(empty) empty.hidden=!(sel.length&&!shown);
    if(clear) clear.hidden=!sel.length;
    if(push){try{var u=new URL(location.href);if(sel.length)u.searchParams.set('tags',sel.join(','));else u.searchParams.delete('tags');history.replaceState(null,'',u)}catch(e){}}
  }
  chips.forEach(function(ch){ch.addEventListener('click',function(){
    var t=ch.dataset.tag,i=sel.indexOf(t); if(i>-1) sel.splice(i,1); else sel.push(t); apply(true);
  })});
  if(clear) clear.addEventListener('click',function(){sel=[];apply(true)});
  apply(false);
})();

// glossary: highlight the letter you're currently reading in the A-Z bar
(function(){
  var bar=document.querySelector('.gl-az'); if(!bar) return;
  var links=[].slice.call(bar.querySelectorAll('a[href^="#gl-"]'));
  var groups=links.map(function(a){return document.getElementById(a.getAttribute('href').slice(1))});
  var cur=-1, ticking=false, lock=-1;
  // a letter you click stays highlighted until the jump finishes, even if the section can't reach the top (e.g. near the end of the page)
  links.forEach(function(a,k){a.addEventListener('click',function(){lock=k;set(k);});});
  function unlock(){if(lock>-1){lock=-1;requestAnimationFrame(update);}}
  addEventListener('wheel',unlock,{passive:true});
  addEventListener('touchmove',unlock,{passive:true});
  addEventListener('keydown',function(e){if(/^(Arrow|Page|Home|End| )/.test(e.key))unlock();});
  function set(i){
    if(i===cur) return;
    if(cur>-1) links[cur].removeAttribute('aria-current');
    cur=i;
    if(i>-1){
      var a=links[i]; a.setAttribute('aria-current','true');
      if(bar.scrollWidth>bar.clientWidth){var l=a.offsetLeft-bar.clientWidth/2+a.offsetWidth/2;bar.scrollLeft=Math.max(0,l);}
    }
  }
  function update(){
    ticking=false;
    if(lock>-1) return;
    var line=bar.getBoundingClientRect().bottom+80, i=-1;
    for(var k=0;k<groups.length;k++){ if(groups[k] && groups[k].getBoundingClientRect().top<=line) i=k; else break; }
    set(i);
  }
  addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(update);}},{passive:true});
  addEventListener('resize',update);
  update();
})();
