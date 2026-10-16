(function () {
  var d = document, root = d.documentElement;
  root.classList.add('js');

  // mobile menu
  var burger = d.querySelector('.burger'), nav = d.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); burger.focus(); }
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
