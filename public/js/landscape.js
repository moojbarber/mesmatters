/* Systems landscape builder: pick your systems, say how they connect, see the map and what to look at first */
(function () {
  var root = document.getElementById('ls');
  if (!root) return;
  var BASE = (window.LP_BASE || '').replace(/\/\.$/, ''), EXT = window.LP_EXT || '';
  var NS = 'http://www.w3.org/2000/svg';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function link(slug) { return BASE + '/post/' + slug + EXT; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  var MODULES = [
    { id: 'mes', name: 'MES', sub: 'Production' },
    { id: 'qms', name: 'QMS', sub: 'Quality' },
    { id: 'ims', name: 'IMS', sub: 'Inventory' },
    { id: 'cmms', name: 'CMMS', sub: 'Maintenance' },
    { id: 'cw', name: 'Connected worker', sub: 'Frontline apps', wide: true }
  ];
  var APPS = [
    { id: 'crm', name: 'CRM', sub: 'Customers and sales', side: 'L', erpOnly: true },
    { id: 'plm', name: 'PLM', sub: 'Product definition', side: 'L' },
    { id: 'cpq', name: 'CPQ', sub: 'Configure and quote', side: 'L', erpOnly: true },
    { id: 'aps', name: 'APS', sub: 'Advanced scheduling', side: 'L' },
    { id: 'hcm', name: 'HR / WFM', sub: 'People, time and shifts', side: 'L' },
    { id: 'tms', name: 'TMS', sub: 'Transport', side: 'L' },
    { id: 'wms', name: 'WMS', sub: 'Complex warehousing', side: 'R' },
    { id: 'lims', name: 'LIMS', sub: 'Regulated labs', side: 'R' },
    { id: 'eam', name: 'EAM', sub: 'Asset lifecycle', side: 'R' },
    { id: 'xqms', name: 'Separate QMS', sub: 'Enterprise quality', side: 'R' },
    { id: 'xcmms', name: 'Separate CMMS', sub: 'Maintenance', side: 'R' },
    { id: 'xcw', name: 'Connected worker app', sub: 'Standalone', side: 'R' },
    { id: 'scada', name: 'SCADA', sub: 'Supervisory control', side: 'R' },
    { id: 'hist', name: 'Historian', sub: 'Time-series data', side: 'R' },
    { id: 'xls', name: 'Spreadsheets', sub: 'The unofficial systems', side: 'R' }
  ];
  var LINKS = [['off', 'Not used'], ['alone', 'Used, not connected'], ['erp', 'Connected to ERP'], ['mom', 'Connected to MOM'], ['both', 'Connected to both']];
  var DEFAULT = { erp: true, approach: 'mom', modules: { mes: 1, qms: 1, ims: 1, cmms: 1, cw: 0 }, apps: { plm: 'erp', xls: 'alone' }, custom: [], data: false, machines: 'auto' };

  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function load() {
    try {
      var h = location.hash.match(/s=([^&]+)/);
      if (h) return Object.assign(clone(DEFAULT), JSON.parse(decodeURIComponent(escape(atob(h[1])))));
    } catch (e) {}
    try { var v = JSON.parse(localStorage.getItem('sm-tool-landscape')); if (v) return Object.assign(clone(DEFAULT), v); } catch (e) {}
    return clone(DEFAULT);
  }
  var S = load();
  function save() { try { localStorage.setItem('sm-tool-landscape', JSON.stringify(S)); } catch (e) {} }
  function hasMom() { return S.approach !== 'none'; }
  function linkOf(id) { var v = S.apps[id] || 'off'; if (!hasMom() && (v === 'mom' || v === 'both')) v = S.erp ? 'erp' : 'alone'; if (!S.erp && (v === 'erp' || v === 'both')) v = hasMom() ? 'mom' : 'alone'; return v; }

  /* ---------- controls */
  var panel = document.getElementById('ls-panel');
  function select(name, val, opts) {
    return '<select data-k="' + name + '">' + opts.map(function (o) { return '<option value="' + o[0] + '"' + (o[0] === val ? ' selected' : '') + (o[2] ? ' disabled' : '') + '>' + o[1] + '</option>'; }).join('') + '</select>';
  }
  function linkOpts(erpOnly) {
    return LINKS.map(function (l) {
      var dis = (!hasMom() && (l[0] === 'mom' || l[0] === 'both')) || (!S.erp && (l[0] === 'erp' || l[0] === 'both')) || (erpOnly && (l[0] === 'mom' || l[0] === 'both'));
      return [l[0], l[1], dis];
    });
  }
  function renderPanel() {
    var h = '';
    h += '<fieldset><legend>Your core</legend>';
    h += '<label class="ls-row"><span><b>ERP</b><small>Runs the business</small></span>' + select('erp', S.erp ? 'yes' : 'no', [['yes', 'We have one'], ['no', 'Not yet']]) + '</label>';
    h += '<label class="ls-row"><span><b>On the shopfloor</b><small>What runs the operation</small></span>' + select('approach', S.approach, [['mom', 'A MOM platform'], ['mes', 'An MES for production'], ['none', 'Paper and spreadsheets']]) + '</label>';
    if (S.approach === 'mom') {
      h += '<div class="ls-mods"><span class="micro">Inside your MOM</span>' + MODULES.map(function (m) {
        return '<label class="ls-chip"><input type="checkbox" data-mod="' + m.id + '"' + (S.modules[m.id] ? ' checked' : '') + '><span>' + m.name + ' <i>' + m.sub + '</i></span></label>';
      }).join('') + '</div>';
    }
    h += '<label class="ls-row"><span><b>Machines</b><small>How machine data arrives</small></span>' + select('machines', S.machines, [['auto', 'Automatically'], ['manual', 'Typed in by hand']]) + '</label>';
    h += '<label class="ls-row"><span><b>Data and AI</b><small>A data platform across your systems</small></span>' + select('data', S.data ? 'yes' : 'no', [['no', 'Not yet'], ['yes', 'We have one']]) + '</label>';
    h += '</fieldset>';
    ['L', 'R'].forEach(function (side) {
      h += '<fieldset><legend>' + (side === 'L' ? 'Business and engineering' : 'Operations and the plant') + '</legend>';
      APPS.filter(function (a) { return a.side === side; }).forEach(function (a) {
        h += '<label class="ls-row' + (linkOf(a.id) !== 'off' ? ' used' : '') + '"><span><b>' + a.name + '</b><small>' + a.sub + '</small></span>' + select('app:' + a.id, linkOf(a.id), linkOpts(a.erpOnly)) + '</label>';
      });
      h += '</fieldset>';
    });
    h += '<fieldset><legend>Anything else</legend>';
    S.custom.forEach(function (c, i) {
      h += '<div class="ls-row used"><span><b>' + esc(c.name) + '</b><small>' + (c.side === 'L' ? 'Business side' : 'Operations side') + ' <button type="button" class="ls-x" data-del="' + i + '">Remove</button></small></span>' + select('cust:' + i, c.link, linkOpts(false)) + '</div>';
    });
    h += '<form class="ls-add" id="ls-add"><input type="text" name="n" maxlength="28" placeholder="Add a system, e.g. MRP, BI, SCADA"><select name="side"><option value="L">Business side</option><option value="R">Operations side</option></select><button class="btn ghost sm" type="submit">Add</button></form>';
    h += '</fieldset>';
    panel.innerHTML = h;
  }
  panel.addEventListener('change', function (e) {
    var t = e.target, k = t.getAttribute('data-k');
    if (t.dataset.mod) S.modules[t.dataset.mod] = t.checked ? 1 : 0;
    else if (k === 'erp') S.erp = t.value === 'yes';
    else if (k === 'data') S.data = t.value === 'yes';
    else if (k === 'approach' || k === 'machines') S[k] = t.value;
    else if (k && k.indexOf('app:') === 0) S.apps[k.slice(4)] = t.value;
    else if (k && k.indexOf('cust:') === 0) S.custom[+k.slice(5)].link = t.value;
    else return;
    update(k === 'approach' || k === 'erp' || !!t.dataset.mod);
  });
  panel.addEventListener('click', function (e) {
    var b = e.target.closest('[data-del]'); if (!b) return;
    e.preventDefault(); S.custom.splice(+b.dataset.del, 1); update(true);
  });
  panel.addEventListener('submit', function (e) {
    e.preventDefault();
    var f = e.target, n = f.n.value.trim();
    if (!n) return;
    S.custom.push({ name: n.slice(0, 28), side: f.side.value, link: S.erp ? 'erp' : (hasMom() ? 'mom' : 'alone') });
    update(true);
    var inp = panel.querySelector('#ls-add input'); if (inp) inp.focus();
  });

  /* ---------- map */
  var stage = document.getElementById('ls-stage'), dots = [], svg = null;
  var C = { erp: '#ffb86b', mom: '#33d4e0', core: '#c9bcff', alone: '#ff9b9b', text: '#ffffff', sub: '#a9a4d6' };
  function el(tag, attrs, parent) { var e = document.createElementNS(NS, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
  function txt(parent, x, y, s, size, fill, weight) { var t = el('text', { x: x, y: y, 'text-anchor': 'middle', 'font-family': 'Space Grotesk, Inter, Arial, sans-serif', 'font-size': size, fill: fill, 'font-weight': weight || 400 }, parent); t.textContent = s; return t; }
  function box(parent, x, y, w, h, o) {
    el('rect', { x: x, y: y, width: w, height: h, rx: o.rx || 14, fill: o.fill, stroke: o.stroke, 'stroke-width': o.sw || 1.5, 'stroke-dasharray': o.dash || 'none' }, parent);
    txt(parent, x + w / 2, y + (o.sub ? h / 2 - 2 : h / 2 + 5), o.name, o.size || 15, C.text, 700);
    if (o.sub) txt(parent, x + w / 2, y + h / 2 + 15, o.sub, 11, o.subFill || C.sub);
  }

  function draw() {
    dots.forEach(function (d) { d.el.remove(); }); dots = [];
    var W = 1000, off = S.data ? 64 : 0;
    var left = [], right = [];
    APPS.forEach(function (a) { var v = linkOf(a.id); if (v !== 'off') (a.side === 'L' ? left : right).push({ name: a.name, sub: a.sub, link: v }); });
    S.custom.forEach(function (c) { if (c.link !== 'off') (c.side === 'L' ? left : right).push({ name: c.name, sub: 'Added by you', link: c.link }); });

    var mods = S.approach === 'mom' ? MODULES.filter(function (m) { return S.modules[m.id] && !m.wide; }) : S.approach === 'mes' ? [MODULES[0]] : [];
    var cwIn = S.approach === 'mom' && S.modules.cw;
    var rows = Math.ceil(mods.length / 2) || 0;
    var momTop = S.erp ? 200 : 110, momH = S.approach === 'none' ? 110 : 66 + rows * 86 + (cwIn ? 52 : 0) + (rows || cwIn ? 4 : 30);
    var momBot = momTop + momH;
    var n = Math.max(left.length, right.length, 1);
    var sideTop = S.erp ? 70 : 60, gap = Math.max(76, (momBot + 40 - sideTop) / n);
    var sideBot = sideTop + (n - 1) * gap + 56;
    var floorY = Math.max(momBot + 90, sideBot + 30);
    var H = floorY + 52 + 34 + off;

    stage.innerHTML = '';
    svg = el('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': 'Your systems landscape', xmlns: NS }, stage);
    el('rect', { x: 0, y: 0, width: W, height: H, fill: '#0b0a22' }, svg);
    var defs = el('defs', {}, svg);
    var lg = el('linearGradient', { id: 'lsMom', x1: 0, y1: 0, x2: 1, y2: 1 }, defs);
    el('stop', { offset: 0, 'stop-color': '#8b6cff' }, lg); el('stop', { offset: 1, 'stop-color': '#33d4e0' }, lg);
    if (S.data) {
      el('rect', { x: 8, y: 26, width: W - 16, height: H - 34, rx: 30, fill: 'rgba(51,212,224,0.03)', stroke: 'rgba(51,212,224,0.45)', 'stroke-width': 1.5, 'stroke-dasharray': '7 7' }, svg);
      box(svg, 370, 6, 260, 42, { name: 'Data and AI', sub: 'Connects to everything', fill: '#0c2a36', stroke: '#33d4e0', rx: 21, size: 14, subFill: '#9fe9ef' });
    }
    var g = el('g', { transform: 'translate(0,' + off + ')' }, svg);
    var eg = el('g', {}, g), dg = el('g', {}, g), ng = el('g', {}, g);
    var edges = [];
    function edge(d, kind) { var p = el('path', { d: d, fill: 'none', stroke: kind === 'erp' ? 'rgba(255,184,107,0.55)' : kind === 'mom' ? 'rgba(51,212,224,0.6)' : kind === 'core' ? 'rgba(165,148,255,0.8)' : 'rgba(165,148,255,0.45)', 'stroke-width': kind === 'core' ? 4 : 2.5, 'stroke-dasharray': kind === 'manual' ? '3 8' : 'none', 'stroke-linecap': 'round' }, eg); edges.push({ p: p, kind: kind }); }

    // ERP
    if (S.erp) box(ng, 400, 40, 200, 66, { name: 'ERP', sub: 'Runs the business', fill: 'rgba(255,184,107,0.12)', stroke: C.erp, rx: 18, size: 17, sw: 2 });
    // MOM / MES / none
    if (S.approach === 'none') {
      box(ng, 330, momTop, 340, momH, { name: 'Paper and spreadsheets', sub: 'No shopfloor system yet', fill: 'rgba(255,155,155,0.05)', stroke: C.alone, dash: '6 6', rx: 24, size: 17 });
    } else {
      el('ellipse', { cx: 500, cy: momTop + momH / 2, rx: 240, ry: momH / 2 + 50, fill: 'rgba(51,212,224,0.07)' }, ng);
      el('rect', { x: 330, y: momTop, width: 340, height: momH, rx: 26, fill: '#120f33', stroke: 'url(#lsMom)', 'stroke-width': 3.5 }, ng);
      txt(ng, 500, momTop + 30, S.approach === 'mom' ? 'MOM' : 'MES', 20, C.text, 700);
      txt(ng, 500, momTop + 48, S.approach === 'mom' ? 'Runs the operation, on one set of data' : 'Runs production', 11, C.sub);
      mods.forEach(function (m, i) {
        var x = i % 2 ? 504 : 346, y = momTop + 62 + Math.floor(i / 2) * 86;
        if (mods.length % 2 && i === mods.length - 1) x = 425;
        box(ng, x, y, 150, 76, { name: m.name, sub: m.sub, fill: 'rgba(139,108,255,0.14)', stroke: 'rgba(165,148,255,0.5)', size: 17 });
      });
      if (cwIn) box(ng, 346, momTop + 62 + rows * 86, 308, 42, { name: 'Connected worker', fill: 'rgba(139,108,255,0.08)', stroke: 'rgba(165,148,255,0.55)', dash: '5 4', rx: 12, size: 13.5 });
      if (S.erp) edge('M500,106 L500,' + momTop, 'core');
    }
    // floor
    box(ng, 270, floorY, 460, 52, { name: 'Machines, PLCs and people', sub: S.machines === 'auto' ? 'Connected automatically' : 'Data typed in by hand', fill: 'rgba(165,148,255,0.08)', stroke: 'rgba(165,148,255,0.4)', dash: '4 4' });
    edge('M500,' + momBot + ' L500,' + floorY, S.machines === 'auto' && S.approach !== 'none' ? 'floor' : 'manual');

    // side apps
    function place(list, side) {
      list.forEach(function (a, i) {
        var x = side === 'L' ? 36 : 812, y = sideTop + i * gap, cy = y + 28;
        var ex = side === 'L' ? 188 : 812, dir = side === 'L' ? 1 : -1;
        var t = (i + 0.5) / list.length;
        if ((a.link === 'erp' || a.link === 'both') && S.erp) {
          var ty = 52 + t * 46, tx = side === 'L' ? 400 : 600;
          edge('M' + ex + ',' + cy + ' C' + (ex + dir * 110) + ',' + cy + ' ' + (tx - dir * 80) + ',' + ty + ' ' + tx + ',' + ty, 'erp');
        }
        if ((a.link === 'mom' || a.link === 'both') && hasMom()) {
          var my = momTop + 20 + t * (momH - 40), mx = side === 'L' ? 330 : 670;
          edge('M' + ex + ',' + cy + ' C' + (ex + dir * 80) + ',' + cy + ' ' + (mx - dir * 70) + ',' + my + ' ' + mx + ',' + my, 'mom');
        }
        var alone = a.link === 'alone';
        box(ng, x, y, 152, 56, { name: a.name.length > 18 ? a.name.slice(0, 17) + '…' : a.name, sub: alone ? 'Not connected' : a.sub, fill: alone ? 'rgba(255,155,155,0.06)' : 'rgba(255,255,255,0.05)', stroke: alone ? C.alone : 'rgba(255,255,255,0.25)', dash: alone ? '5 4' : 'none', subFill: alone ? C.alone : C.sub });
      });
    }
    place(left, 'L'); place(right, 'R');

    // flowing dots
    if (!reduce) edges.forEach(function (e) {
      if (e.kind === 'manual') return;
      var col = e.kind === 'erp' ? C.erp : e.kind === 'mom' ? C.mom : C.core, len = e.p.getTotalLength(), k = e.kind === 'core' ? 4 : 2;
      for (var i = 0; i < k; i++) {
        var c = el('circle', { r: e.kind === 'core' ? 4.5 : 3.5, fill: col }, dg);
        dots.push({ el: c, p: e.p, len: len, t: i / k + Math.random() * 0.1, dir: i % 2 ? -1 : 1, v: 0.0026 * (0.8 + Math.random() * 0.4) });
      }
    });

    // stats
    var nSys = left.length + right.length + (S.erp ? 1 : 0) + (hasMom() ? 1 : 0);
    var nInt = edges.filter(function (e) { return e.kind === 'erp' || e.kind === 'mom'; }).length + (S.erp && hasMom() ? 1 : 0);
    var nAlone = left.concat(right).filter(function (a) { return a.link === 'alone'; }).length;
    document.getElementById('ls-stats').textContent = nSys + ' systems, ' + nInt + ' integrations' + (nAlone ? ', ' + nAlone + ' not connected' : '');
    return { nInt: nInt, nAlone: nAlone };
  }
  function tick() {
    if (!document.hidden) dots.forEach(function (d) {
      d.t += d.v; if (d.t > 1) d.t -= 1;
      var pt = d.p.getPointAtLength(d.len * (d.dir > 0 ? d.t : 1 - d.t));
      d.el.setAttribute('cx', pt.x); d.el.setAttribute('cy', pt.y);
      d.el.setAttribute('opacity', Math.min(1, Math.sin(d.t * Math.PI) * 1.6));
    });
    requestAnimationFrame(tick);
  }

  /* ---------- insights */
  var ins = document.getElementById('ls-insights');
  function insights(st) {
    var out = [], m = S.modules, a = function (id) { return linkOf(id); };
    function add(tone, title, text, slug, label) { out.push({ tone: tone, title: title, text: text, slug: slug, label: label }); }
    if (S.approach === 'mom' && m.mes && m.qms && m.ims && m.cmms) add('good', 'One set of data across the operation', 'Production, quality, inventory and maintenance share the same data, so everyone works from one version of the truth.', 'mes-vs-mom', 'MES vs MOM');
    if (S.approach === 'mom' && !(m.mes && m.qms && m.ims && m.cmms)) add('idea', 'Room to grow your MOM', 'Some of the four MOM areas aren\'t in your platform yet. Each one you add brings its data onto the same platform as the rest, with no new interface to build.', 'mes-functionality-guide', 'MES functionality guide');
    if (S.approach === 'mes') add('idea', 'An MES covers production', 'It can feed separate quality and maintenance systems, and that works. A full MOM puts production, quality, inventory and maintenance on the same data, which is the better overall solution.', 'mes-vs-mom', 'MES vs MOM');
    if (S.approach === 'none') add('watch', 'The shopfloor runs on paper', 'That\'s where most manufacturers start. A MOM platform gives you real-time data and traceability, and the foundation that AI learns from.', 'what-is-mes', 'What is MES/MOM?');
    if (a('xqms') !== 'off' && S.approach === 'mom' && m.qms) add('watch', 'Two places for quality', 'Your MOM already covers quality on the line. Running a separate QMS alongside it means paying twice for much of the same capability. Serious non-conformances and CAPA can escalate into ERP instead.', 'qms-and-mes-quality', 'QMS and MES');
    else if (a('xqms') !== 'off') add('idea', 'A separate QMS', 'Make sure non-conformances arrive with their full context. With a MOM that covers quality, and ERP for non-conformances and CAPA, a separate QMS adds little.', 'qms-vs-lims-vs-mes', 'QMS vs LIMS vs MES');
    if (a('xcmms') !== 'off' && S.approach === 'mom' && m.cmms) add('watch', 'Two versions of downtime', 'Your MOM covers maintenance. A separate CMMS alongside it means two records of every stop, and an interface to keep in step.', 'cmms-vs-eam-vs-mes', 'CMMS vs EAM vs MES');
    else if (a('xcmms') !== 'off' && hasMom() && a('xcmms') !== 'mom' && a('xcmms') !== 'both') add('idea', 'Feed maintenance from the shopfloor', 'Your CMMS should get run hours, counts and downtime from the shopfloor system, so maintenance works from the same downtime as production.', 'eam-cmms-and-mes', 'EAM, CMMS and MES');
    if (a('eam') !== 'off') add('idea', 'Check what ERP already covers', 'ERP often holds the asset register, depreciation and capital spend. A full EAM earns its place in asset-heavy businesses with advanced needs.', 'cmms-vs-eam-vs-mes', 'CMMS vs EAM vs MES');
    if (a('wms') !== 'off') add('idea', 'WMS and the line', 'A WMS is the right tool for complex warehousing and distribution. Drive line-side replenishment from what the shopfloor is about to consume.', 'wms-vs-mes-inventory', 'WMS vs MES vs ERP');
    if (a('lims') === 'erp' || a('lims') === 'alone') add('watch', 'Lab results reach the line late', 'Results that only go to ERP, or nowhere, can\'t hold or release a batch in real time. Connect the LIMS to MOM, or let MOM handle sampling if the lab is simple.', 'lims-and-mes', 'LIMS and MES');
    if (a('aps') === 'erp' && hasMom()) add('idea', 'Schedule from reality', 'Feed your APS with actual progress from the shopfloor, so each new schedule starts from what really happened.', 'aps-vs-mes-scheduling', 'APS vs ERP scheduling');
    if (a('xcw') !== 'off' && hasMom() && a('xcw') !== 'mom' && a('xcw') !== 'both') add('watch', 'Frontline apps without the line', 'A connected worker app that isn\'t linked to the shopfloor system knows the order, but not what the line is actually doing.', 'connected-worker-one-app-not-five', 'Connected worker');
    if (a('xcw') !== 'off' && S.approach === 'mom' && m.cw) add('watch', 'Two connected worker tools', 'Your MOM already includes connected worker. A second app means two places for instructions and checklists.', 'connected-worker-one-app-not-five', 'Connected worker');
    if (a('xls') !== 'off') add('watch', 'The spreadsheets are a system too', 'If people rely on them, they hold data nobody else can see. Find out what they\'re used for. It often shows exactly what\'s missing.', 'manufacturing-process-mapping', 'Process before technology');
    if (st.nAlone > (a('xls') !== 'off' ? 1 : 0)) add('watch', 'Islands of data', 'Systems that aren\'t connected mean re-keying, delays and different versions of the truth. Connecting them is often a quick win.', 'isa95-integration-patterns', 'Integration patterns');
    if (S.machines === 'manual' && S.approach !== 'none') add('watch', 'Machine data typed in by hand', 'Manual entry misses short stops and arrives late. Connecting machines gives you real-time data and accurate OEE.', 'opc-ua-mqtt-uns-explained', 'OPC UA, MQTT and UNS');
    if (!S.data) add('idea', 'Data and AI', 'AI and the data foundation are best built together. A data platform that brings contextualised data from all of these systems together is what AI learns from.', 'manufacturing-data-platforms', 'Where shopfloor data lives');
    else add('good', 'A data layer across everything', 'Make sure the shopfloor data arrives with its context: the order, material, machine and operator. That context is what makes AI useful.', 'contextualised-manufacturing-data', 'Context is what makes data useful');
    if (st.nInt >= 8) add('idea', st.nInt + ' integrations to look after', 'Point-to-point is often the safest choice, but every interface needs retesting at each upgrade. Be clear which system owns each piece of master data.', 'isa95-integration-patterns', 'Integration patterns');
    ins.innerHTML = out.map(function (o) {
      return '<div class="ls-in ' + o.tone + '"><b>' + esc(o.title) + '</b><p>' + esc(o.text) + '</p><a href="' + link(o.slug) + '">Read: ' + esc(o.label) + ' →</a></div>';
    }).join('');
  }

  function update(rebuildPanel) {
    if (rebuildPanel) renderPanel();
    else [].forEach.call(panel.querySelectorAll('.ls-row'), function (r) { var s = r.querySelector('select[data-k^="app:"],select[data-k^="cust:"]'); if (s) r.classList.toggle('used', s.value !== 'off'); });
    var st = draw(); insights(st); save();
  }

  /* ---------- actions */
  document.getElementById('ls-reset').addEventListener('click', function () { S = clone(DEFAULT); history.replaceState(null, '', location.pathname); update(true); });
  document.getElementById('ls-share').addEventListener('click', function (e) {
    var u = location.href.split('#')[0] + '#s=' + btoa(unescape(encodeURIComponent(JSON.stringify(S))));
    var b = e.currentTarget, t = b.textContent;
    if (navigator.clipboard) navigator.clipboard.writeText(u).then(function () { b.textContent = 'Link copied'; setTimeout(function () { b.textContent = t; }, 1800); });
    else prompt('Copy this link', u);
  });
  document.getElementById('ls-png').addEventListener('click', function () {
    if (!svg) return;
    var clone2 = svg.cloneNode(true);
    [].forEach.call(clone2.querySelectorAll('circle'), function (c) { c.remove(); });
    var vb = svg.viewBox.baseVal, scale = 2;
    var data = new XMLSerializer().serializeToString(clone2);
    var img = new Image();
    img.onload = function () {
      var cv = document.createElement('canvas'); cv.width = vb.width * scale; cv.height = (vb.height + 40) * scale;
      var cx = cv.getContext('2d'); cx.fillStyle = '#0b0a22'; cx.fillRect(0, 0, cv.width, cv.height);
      cx.drawImage(img, 0, 0, vb.width * scale, vb.height * scale);
      cx.fillStyle = '#a9a4d6'; cx.font = (13 * scale) + 'px Arial, sans-serif'; cx.textAlign = 'right';
      cx.fillText('Made with the systems landscape tool at shopfloormatters.com', (vb.width - 20) * scale, (vb.height + 24) * scale);
      var a = document.createElement('a'); a.download = 'my-systems-landscape.png'; a.href = cv.toDataURL('image/png'); document.body.appendChild(a); a.click(); a.remove();
    };
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(data);
  });

  update(true);
  if (!reduce) requestAnimationFrame(tick);
})();
