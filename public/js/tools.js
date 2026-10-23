/* Shopfloor Matters tools: readiness check, 1% calculator, systems picker, vendor scorecard, email gates, Ask Matt */
(function () {
  var d = document;
  var BASE = window.LP_BASE || '';
  function $(s, r) { return (r || d).querySelector(s); }
  function $$(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem('sm-tool-' + k) || 'null'); localStorage.setItem('sm-tool-' + k, JSON.stringify(v)); } catch (e) { return null; } }
  function forget(k) { try { localStorage.removeItem('sm-tool-' + k); } catch (e) {} }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function url(path) { return BASE + path + (/^\./.test(BASE) && !/\/$/.test(path) ? '.html' : ''); }
  function csv(name, rows) {
    var body = rows.map(function (r) { return r.map(function (c) { c = String(c == null ? '' : c); return /[",\n]/.test(c) ? '"' + c.replace(/"/g, '""') + '"' : c; }).join(','); }).join('\n');
    var a = d.createElement('a');
    a.href = URL.createObjectURL(new Blob(['﻿' + body], { type: 'text/csv;charset=utf-8' }));
    a.download = 'shopfloor-matters-' + name + '.csv';
    d.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  var dataEl = $('#tk-data');
  var DATA = dataEl ? JSON.parse(dataEl.textContent) : null;
  var tool = $('[data-tool]');
  var csvRows = null;
  $$('[data-print]').forEach(function (b) { b.addEventListener('click', function () { print(); }); });
  $$('[data-csv]').forEach(function (b) { b.addEventListener('click', function () { if (csvRows) csv(b.getAttribute('data-csv'), csvRows()); }); });

  /* ---------- email gates (Kit). Without a Kit form the download is simply shown. */
  $$('form.gate').forEach(function (f) {
    var res = f.getAttribute('data-gate');
    var reveal = $('[data-gate-reveal="' + res + '"]');
    var done = store('gate-' + res);
    if (!f.dataset.form) { f.hidden = true; if (reveal) reveal.hidden = false; return; }
    if (done && reveal) { reveal.hidden = false; }
    var msg = $('.msg', f), btn = $('button', f), em = $('input[type=email]', f);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      f.classList.remove('err', 'ok');
      if (f.website && f.website.value) return;
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em.value)) { f.classList.add('err'); msg.textContent = 'Please enter a valid email address.'; em.focus(); return; }
      if (f._extra) f._extra(f);
      btn.disabled = true; msg.textContent = 'Sending…';
      var body = new FormData(f); body.delete('website');
      fetch(f.action, { method: 'POST', body: body, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw r; })
        .catch(function () { /* still let them have it; Kit may need confirmation */ })
        .then(function () {
          btn.disabled = false; f.classList.add('ok'); store('gate-' + res, 1);
          msg.textContent = reveal ? 'Done. Your download is below, and the link is on its way. Check your inbox to confirm your email.' : 'Done. Check your inbox and confirm your email, and it will be with you shortly.';
          if (reveal) { reveal.hidden = false; var a = $('a[download]', reveal); if (a) a.click(); }
        });
    });
  });

  /* ---------- Ask Matt */
  $$('form.ask-form').forEach(function (f) {
    var msg = $('.msg', f), q = $('textarea', f), btn = $('button[type=submit]', f);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (f.website && f.website.value) return;
      if (q.value.trim().length < 10) { msg.textContent = 'Add a little more detail so I can give you a useful answer.'; q.focus(); return; }
      var ep = f.getAttribute('data-ask');
      if (!ep) {
        var text = q.value.trim();
        var go = function () { window.open(f.getAttribute('data-linkedin'), '_blank', 'noopener'); };
        if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () { msg.textContent = 'Copied. Paste it into a LinkedIn message to me and I\'ll reply there.'; go(); }, go);
        else { msg.textContent = 'Copy your question, then send it to me on LinkedIn.'; go(); }
        return;
      }
      btn.disabled = true; msg.textContent = 'Sending…';
      var body = new FormData(f); body.delete('website'); body.append('page', location.pathname);
      fetch(ep, { method: 'POST', body: body, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw r; f.reset(); msg.textContent = 'Thanks. Your question is with me. If you left an email, I\'ll reply directly.'; })
        .catch(function () { msg.textContent = 'That didn\'t send. Try again, or message me on LinkedIn.'; })
        .then(function () { btn.disabled = false; });
    });
  });

  $$('[data-copy-text]').forEach(function (b) { b.addEventListener('click', function () { var el = d.getElementById(b.getAttribute('data-copy-text')); if (el && navigator.clipboard) navigator.clipboard.writeText(el.textContent.trim()).then(function () { var t = b.textContent; b.textContent = 'Copied'; setTimeout(function () { b.textContent = t; }, 1600); }); }); });
  if (!tool) return;
  $$('form', tool).forEach(function (f) { if (!f.classList.contains('gate')) f.addEventListener('submit', function (e) { e.preventDefault(); }); });
  var id = tool.getAttribute('data-tool');

  /* ---------- readiness check */
  if (id === 'readiness-check' && DATA) {
    var form = $('#rc-form'), out = $('#rc-result');
    var radios = $$('input[type=radio]', form);
    var nq = $$('.rc-q', form).length;
    var saved = store('readiness') || {};
    radios.forEach(function (r) { if (saved[r.name] == r.value) r.checked = true; });
    function answers() { var a = {}; radios.forEach(function (r) { if (r.checked) a[r.name] = +r.value; }); return a; }
    function progress() {
      var a = answers(), n = Object.keys(a).length;
      $('[data-rc-count]').textContent = n;
      $('[data-rc-fill]').style.width = (n / nq * 100) + '%';
      $('[data-rc-show]').disabled = n < nq;
      $('[data-rc-show]').textContent = n < nq ? (nq - n) + ' to go' : 'See my result';
      store('readiness', a);
      return n;
    }
    var result = null;
    function stage(a) { return a < 1.57 ? 1 : a < 2.14 ? 2 : a < 2.71 ? 3 : a < 3.29 ? 4 : a < 3.86 ? 5 : a < 4.43 ? 6 : 7; }
    function compute() {
      var a = answers(), areas = DATA.areas.map(function (ar) {
        var vals = $$('input[data-area="' + ar.id + '"]:checked', form).map(function (i) { return +i.value; });
        var avg = vals.reduce(function (s, v) { return s + v; }, 0) / (vals.length || 1);
        return { ar: ar, avg: avg };
      });
      var all = Object.keys(a).map(function (k) { return a[k]; });
      var avg = all.reduce(function (s, v) { return s + v; }, 0) / all.length;
      var lvl = stage(avg);
      var weak = areas.slice().sort(function (x, y) { return x.avg - y.avg; })[0];
      return { avg: avg, lvl: lvl, L: DATA.levels[lvl - 1], areas: areas, weak: weak };
    }
    function link(p) { return '<a class="rc-r" href="' + url('/post/' + p.slug) + '"><span class="micro">' + esc(p.cat) + '</span><b>' + esc(p.title) + '</b></a>'; }
    function show(scroll) {
      result = compute();
      var R = result;
      $('[data-rc-level]').textContent = R.lvl;
      $('[data-rc-ring]').style.setProperty('--p', (R.avg - 1) / 4 * 100);
      $('[data-rc-name]').textContent = R.L.name;
      $('[data-rc-state]').textContent = R.L.state;
      $$('[data-rc-stages] li').forEach(function (li) { var n = +li.dataset.n; li.classList.toggle('on', n === R.lvl); li.classList.toggle('past', n < R.lvl); });
      $('[data-rc-line]').textContent = R.L.line;
      $('[data-rc-avg]').textContent = R.avg.toFixed(1);
      $('[data-rc-areas]').innerHTML = R.areas.map(function (x) {
        return '<div class="rc-ar' + (x === R.weak ? ' weak' : '') + '"><span>' + esc(x.ar.name) + (x === R.weak ? ' <em>slowest</em>' : '') + '</span><div class="rc-track"><i style="width:' + ((x.avg - 1) / 4 * 100).toFixed(0) + '%"></i></div><b>' + esc(DATA.levels[stage(x.avg) - 1].name) + '</b></div>';
      }).join('');
      $('[data-rc-next]').textContent = R.L.next;
      $('[data-rc-weak]').innerHTML = esc(R.weak.ar.advice) + ' <a href="' + url('/post/' + R.weak.ar.post.slug) + '">Read: ' + esc(R.weak.ar.post.title) + ' →</a>';
      var byId = {}; R.areas.forEach(function (x) { byId[x.ar.id] = x.avg; });
      var warn = $('[data-rc-warn]');
      if (byId.analytics - byId.data >= 1) { warn.hidden = false; warn.innerHTML = '<b>The truth has to arrive first.</b> Your analytics and AI score is well ahead of your data score. AI on spreadsheets and ERP data can help a little today, but AI that learns from your operations needs data captured right now, with its context. That\'s where most of the value is. <a href="' + url('/post/time-to-truth') + '">Why truth arrives in order →</a>'; }
      else if (byId.systems - byId.process >= 1) { warn.hidden = false; warn.innerHTML = '<b>Technology ahead of process.</b> Your systems score is well ahead of your process score. That usually means the systems are automating workarounds. <a href="' + url('/post/manufacturing-process-mapping') + '">Process before technology →</a>'; }
      else warn.hidden = true;
      $('[data-rc-read]').innerHTML = R.L.posts.map(link).join('');
      out.hidden = false;
      var gf = $('form.gate', out);
      if (gf) gf._extra = function (f) {
        [['readiness_level', R.L.name], ['readiness_score', R.avg.toFixed(1)], ['readiness_weakest', R.weak.ar.name]].concat(R.areas.map(function (x) { return ['readiness_' + x.ar.id, x.avg.toFixed(1)]; }))
          .forEach(function (kv) { var i = $('input[name="fields[' + kv[0] + ']"]', f) || f.appendChild(Object.assign(d.createElement('input'), { type: 'hidden', name: 'fields[' + kv[0] + ']' })); i.value = kv[1]; });
      };
      if (scroll) { out.focus({ preventScroll: true }); out.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    }
    csvRows = function () {
      var rows = [['Shopfloor Matters readiness check', new Date().toISOString().slice(0, 10)], ['Time to truth', result.L.name], ['Average', result.avg.toFixed(2)], [], ['Area', 'Question', 'Score']];
      var i = 0;
      DATA.areas.forEach(function (ar) { ar.items.forEach(function (it) { i++; var r = $('input[name=q' + i + ']:checked', form); rows.push([ar.name, it.q, r ? r.value : '']); }); });
      return rows;
    };
    form.addEventListener('change', function () { if (progress() === nq && !out.hidden) show(false); });
    $('[data-rc-show]').addEventListener('click', function () { show(true); });
    $$('[data-reset]', out).forEach(function (b) { b.addEventListener('click', function () { form.reset(); forget('readiness'); out.hidden = true; progress(); form.scrollIntoView({ behavior: 'smooth' }); }); });
    if (progress() === nq) show(false);
  }

  /* ---------- 1% of OEE */
  if (id === 'oee-one-percent') {
    var of = $('#oc-form');
    var defaults = {};
    $$('input,select', of).forEach(function (i) { defaults[i.name] = i.value; });
    var s = store('oee') || {};
    $$('input,select', of).forEach(function (i) { if (s[i.name] != null) i.value = s[i.name]; });
    var last;
    function money(v, cur) { var a = Math.abs(v); var t = a >= 1e6 ? (a / 1e6).toFixed(a >= 1e7 ? 1 : 2) + 'm' : a >= 1e4 ? Math.round(a / 1e3) + 'k' : Math.round(a).toLocaleString('en-GB'); return (v < 0 ? '−' : '') + cur + t; }
    function val(o, pts) {
      var cur = o.oee / 100, nw = Math.min(1, cur + pts / 100), gain = nw / cur - 1;
      var sold = o.rev * gain * (o.sell / 100) * (o.margin / 100);
      var hrs = o.hours * (1 - cur / nw) * (1 - o.sell / 100);
      return { nw: nw, sold: sold, hrs: hrs, save: hrs * o.cost, total: sold + hrs * o.cost };
    }
    function calc() {
      var o = {}; $$('input,select', of).forEach(function (i) { o[i.name] = i.tagName === 'SELECT' ? i.value : Math.max(0, parseFloat(i.value) || 0); });
      store('oee', o);
      if (!o.oee) return;
      var one = val(o, 1);
      last = { o: o, one: one };
      $('[data-oc=point]').textContent = money(one.total, o.cur);
      $('[data-oc=oee]').textContent = o.oee + '%';
      $('[data-oc=sell]').textContent = money(one.sold, o.cur);
      $('[data-oc=save]').textContent = money(one.save, o.cur);
      $('[data-oc=hrs]').textContent = Math.round(o.hours * (1 - o.oee / 100 / one.nw)).toLocaleString('en-GB');
      $('[data-oc=table]').innerHTML = [1, 3, 5, 10].filter(function (p) { return o.oee + p <= 100; }).map(function (p) {
        var v = val(o, p); return '<tr><td>+' + p + ' point' + (p > 1 ? 's' : '') + '</td><td>' + (v.nw * 100).toFixed(0) + '%</td><td><b>' + money(v.total, o.cur) + '</b></td></tr>';
      }).join('');
    }
    csvRows = function () {
      var o = last.o, rows = [['Shopfloor Matters: what is 1% of OEE worth?', new Date().toISOString().slice(0, 10)], ['Revenue in scope', o.rev], ['Contribution margin %', o.margin], ['Current OEE %', o.oee], ['Share of extra output sellable %', o.sell], ['Planned hours / year', o.hours], ['Running cost per hour', o.cost], [], ['Gain (points)', 'New OEE %', 'From selling more', 'From hours saved', 'Total per year']];
      [1, 3, 5, 10].forEach(function (p) { if (o.oee + p <= 100) { var v = val(o, p); rows.push([p, (v.nw * 100).toFixed(1), Math.round(v.sold), Math.round(v.save), Math.round(v.total)]); } });
      return rows;
    };
    of.addEventListener('input', calc);
    of.addEventListener('change', calc);
    $$('[data-reset]').forEach(function (b) { b.addEventListener('click', function () { $$('input,select', of).forEach(function (i) { i.value = defaults[i.name]; }); calc(); }); });
    calc();
  }

  /* ---------- which systems */
  if (id === 'which-systems' && DATA) {
    var wf = $('#ws-form'), boxes = $$('input[type=checkbox]', d).filter(function (i) { return i.form === wf || wf.contains(i); });
    var ws = store('systems') || {};
    boxes.forEach(function (b) { if (ws[b.name]) b.checked = true; });
    var picked = [];
    function run() {
      var st = {}; boxes.forEach(function (b) { st[b.name] = b.checked; }); store('systems', st);
      var probs = $$('.ws-p input:checked', wf), count = {}, from = {};
      probs.forEach(function (p) { var txt = p.nextElementSibling.textContent; p.value.split(',').forEach(function (c) { count[c] = (count[c] || 0) + 1; (from[c] = from[c] || []).push(txt); }); });
      picked = Object.keys(count).sort(function (a, b) { return count[b] - count[a] || DATA.order.indexOf(a) - DATA.order.indexOf(b); });
      $('[data-ws-empty]').hidden = probs.length > 0;
      $('[data-ws-out]').hidden = probs.length === 0;
      if (!probs.length) return;
      $('[data-ws-n]').textContent = picked.length;
      $('[data-ws-p]').textContent = probs.length;
      var inMom = picked.filter(function (c) { return /^MES\/MOM/.test(DATA.caps[c].where); }).length;
      $('[data-ws-summary]').textContent = inMom >= 3 ? inMom + ' of these usually live in MES/MOM. That points towards one operational platform rather than a tool per problem.' : inMom ? inMom + ' of these usually live in MES/MOM, the rest in specialist systems connected to it.' : 'These mostly live in specialist systems. Plan how they connect to the shopfloor before you choose any of them.';
      $('[data-ws-caps]').innerHTML = picked.map(function (c, i) {
        var C = DATA.caps[c];
        return '<article class="ws-cap' + (i < 3 ? ' top' : '') + '"><div class="ws-cap-h"><span class="ws-n">' + count[c] + '</span><div><h3>' + esc(C.name) + '</h3><span class="ws-where">' + esc(C.where) + '</span></div></div><p>' + esc(C.what) + '</p><p class="ws-from">Solves: ' + from[c].map(esc).join(' · ') + '</p>' + (C.post ? '<a href="' + url('/post/' + C.post.slug) + '">' + esc(C.post.title) + ' →</a>' : '') + '</article>';
      }).join('');
      var notes = [];
      var ctx = function (n) { var b = boxes.filter(function (x) { return x.name === n; })[0]; return b && b.checked; };
      if (ctx('regulated')) notes.push('<b>Regulated.</b> Ask every vendor to show audit trails and electronic signatures working through configuration, in a demo built for your industry. <a href="' + url('/post/mes-in-regulated-industries') + '">MES in regulated industries →</a>');
      if (ctx('multisite')) notes.push('<b>More than one site.</b> Design a template from day one, and decide what each site may change. Local customisation is how a programme turns into five different systems. <a href="' + url('/post/mes-multi-site-rollout') + '">Rolling out across sites →</a>');
      if (ctx('onevendor')) notes.push('<b>ERP and MES from one vendor.</b> It can work well, and it isn\'t a reason to skip the evaluation. Very few vendors genuinely offer both at depth, and "integrated" can still mean two products joined together. Check the integration and the shopfloor depth as hard as you would for anyone else. <a href="' + url('/post/mes-vs-erp') + '">MES vs ERP →</a>');
      if (picked.indexOf('data') > -1 && picked.indexOf('connectivity') > -1) notes.push('<b>Data first, then AI.</b> Several of your problems come down to data that isn\'t captured or has no context. Fix that at the point of work before buying analytics on top. <a href="' + url('/post/contextualised-manufacturing-data') + '">Contextualised data →</a>');
      notes.push('<b>Next step.</b> Map one order through the factory before you write requirements. The problems you ticked become specific, and vendors can answer properly. <a href="' + url('/tools/vendor-scorecard') + '">Then use the vendor scorecard →</a>');
      $('[data-ws-notes]').innerHTML = notes.map(function (n) { return '<p>' + n + '</p>'; }).join('');
    }
    csvRows = function () {
      var rows = [['Shopfloor Matters: which systems do I need?', new Date().toISOString().slice(0, 10)], [], ['Capability', 'Usually lives in', 'Problems it solves']];
      picked.forEach(function (c) { rows.push([DATA.caps[c].name, DATA.caps[c].where, $$('.ws-p input:checked', wf).filter(function (p) { return p.value.split(',').indexOf(c) > -1; }).map(function (p) { return p.nextElementSibling.textContent; }).join('; ')]); });
      return rows;
    };
    boxes.forEach(function (b) { b.addEventListener('change', run); });
    $$('[data-reset]').forEach(function (b) { b.addEventListener('click', function () { boxes.forEach(function (x) { x.checked = false; }); run(); }); });
    run();
  }

  /* ---------- vendor scorecard */
  if (id === 'vendor-scorecard') {
    var vf = $('#vs-form'), names = $$('[data-vname]');
    var fields = $$('input[type=number],select', d).filter(function (i) { return i.form === vf; });
    var vs = store('vendors') || {};
    fields.forEach(function (i) { if (vs[i.name] != null) i.value = vs[i.name]; });
    names.forEach(function (n) { if (vs['name' + n.dataset.vname]) n.value = vs['name' + n.dataset.vname]; });
    var nQ = $$('.vs-q', vf).length, scores = [];
    function vname(k) { return (names[k].value || '').trim() || 'Vendor ' + 'ABC'[k]; }
    function run() {
      var st = {}; fields.forEach(function (i) { st[i.name] = i.value; }); names.forEach(function (n) { st['name' + n.dataset.vname] = n.value; }); store('vendors', st);
      $$('[data-vlabel]').forEach(function (el) { el.textContent = vname(+el.dataset.vlabel); });
      scores = [0, 1, 2].map(function (k) {
        var tw = 0, ts = 0, n = 0;
        for (var q = 1; q <= nQ; q++) {
          var w = +vf['w' + q].value, sEl = vf['s' + q + '_' + k], s = parseFloat(sEl.value);
          if (s) { s = Math.max(1, Math.min(5, s)); tw += w; ts += w * s; n++; }
        }
        return { k: k, n: n, score: tw ? Math.round(ts / (tw * 5) * 100) : null };
      });
      var best = Math.max.apply(null, scores.map(function (s) { return s.score || 0; }));
      $('[data-vs-bars]').innerHTML = scores.map(function (s) {
        return '<div class="vs-bar' + (s.score && s.score === best ? ' lead' : '') + '"><span>' + esc(vname(s.k)) + '</span><div class="vs-track"><i style="width:' + (s.score || 0) + '%"></i></div><b>' + (s.score == null ? '–' : s.score) + '</b><small>' + s.n + ' of ' + nQ + ' scored</small></div>';
      }).join('');
    }
    csvRows = function () {
      var rows = [['Shopfloor Matters MES vendor scorecard', new Date().toISOString().slice(0, 10)], [], ['#', 'Question', 'Weight', vname(0), vname(1), vname(2)]];
      $$('.vs-q', vf).forEach(function (q, i) { var n = i + 1; rows.push([n, $('.vs-qt p', q).textContent.replace(/^\d+/, ''), vf['w' + n].value, vf['s' + n + '_0'].value, vf['s' + n + '_1'].value, vf['s' + n + '_2'].value]); });
      rows.push(['', 'Weighted score out of 100', '', scores[0].score, scores[1].score, scores[2].score], [], ['Demo scenario', '', '', vname(0), vname(1), vname(2)]);
      $$('.vs-table tbody tr').forEach(function (tr) { var s = $$('select', tr).map(function (x) { return x.value; }); rows.push([tr.cells[0].textContent, '', ''].concat(s)); });
      return rows;
    };
    d.addEventListener('input', function (e) { if (e.target.form === vf || e.target.hasAttribute('data-vname')) run(); });
    d.addEventListener('change', function (e) { if (e.target.form === vf) run(); });
    $$('[data-reset]').forEach(function (b) { b.addEventListener('click', function () { vf.reset(); $$('.vs-table select').forEach(function (s) { s.value = ''; }); names.forEach(function (n) { n.value = ''; }); forget('vendors'); run(); }); });
    run();
  }
})();
