(function () {
  var d = document, root = d.documentElement;
  root.classList.add('js');

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
