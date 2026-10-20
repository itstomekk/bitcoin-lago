/*
  v/app.js: behaviour shared by the five design variants (/v/a/ to /v/e/, English and Spanish).
  It is script.js (the baseline page) plus three additions, marked "VARIANTS":
    * the map markers take their colours from CSS variables of each design (--marker-fill, ...),
    * the floating Design switcher remembers the last design (localStorage "lbc-design"),
    * big numbers count up once when they scroll into view (only when motion is allowed).
  The merchant finder, map, filters and the QA hook window.LBC_STATE are unchanged.

  WHAT IT DOES
    1. Remembers the language choice when the visitor uses the EN / ES switcher.
    2. Wires placeholder links from config.js (WhatsApp, Facebook, email ...).
    3. Mobile menu, scroll reveal, active nav link.
    4. The merchant finder: loads data/merchants.json, draws one marker per place on a
       Leaflet map (OpenStreetMap tiles, no API key) and one card per place in the list,
       with search, type chips and a village filter that act on map and list together.

  DATA ORIGIN   data/merchants.json (OpenStreetMap contributors, ODbL; built by tools/build_data.py)
  WORDS         the finder reads its labels from the <script id="i18n"> block that tools/build_pages.py
                writes into each page from tools/content.py, so there is no text to translate here.
*/
(function () {
  'use strict';

  var doc = document;
  var BASE = doc.body.getAttribute('data-base') || '';
  var I18N = JSON.parse(doc.getElementById('i18n').textContent);
  var GROUPS = ['eat', 'stay', 'tours', 'shops', 'services', 'other'];
  var BBOX = [[14.598, -91.326], [14.762, -91.097]]; // Lago Bitcoin community area on BTC Map

  /* Load the privacy-enhanced YouTube player only after an explicit, keyboard-accessible click. */
  doc.addEventListener('click', function (event) {
    var button = event.target.closest && event.target.closest('[data-youtube-play]');
    if (!button) return;
    var id = button.getAttribute('data-youtube-play');
    var title = button.getAttribute('data-youtube-title') || '';
    var frame = doc.createElement('iframe');
    frame.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1';
    frame.title = title;
    frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    button.parentNode.replaceChild(frame, button);
  });

  /* ---------- helpers ---------- */
  function $(sel, root) { return (root || doc).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); }
  function el(tag, cls, text) {
    var n = doc.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function norm(s) { return String(s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(); }
  function safeUrl(u) { return /^https?:\/\//i.test(u) ? u : null; }
  function host(u) { try { return new URL(u).hostname.replace(/^www\./, ''); } catch (e) { return u; } }

  var toastTimer;
  function toast() {
    var t = $('#toast');
    if (!t) return;
    t.textContent = t.getAttribute('data-msg');
    t.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove('show'); }, 2600);
  }

  /* ---------- 1. language memory ---------- */
  $all('.lang a[data-lang]').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('lbc-lang', a.getAttribute('data-lang')); } catch (e) {}
    });
  });

  /* ---------- VARIANTS: remember the chosen design ---------- */
  try { localStorage.setItem('lbc-design', doc.body.getAttribute('data-design') || 'a'); } catch (e) {}
  $all('.vsw a[data-design]').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('lbc-design', a.getAttribute('data-design')); } catch (e) {}
    });
  });

  /* ---------- 2. config.js links ---------- */
  var cfg = window.LBC_CONFIG || {};
  $all('[data-config-link]').forEach(function (a) {
    var key = a.getAttribute('data-config-link');
    var v = String(cfg[key] || '').trim();
    if (v) {
      if (key === 'email' && !/^mailto:/i.test(v)) v = 'mailto:' + v;
      if (key === 'expatContact' && /@/.test(v) && !/^(mailto:|https?:)/i.test(v)) v = 'mailto:' + v;
      a.href = v;
      a.removeAttribute('data-placeholder');
      if (/^https?:/i.test(v)) { a.target = '_blank'; a.rel = 'noopener'; }
    } else {
      a.addEventListener('click', function (e) { e.preventDefault(); toast(); });
    }
  });
  $all('[data-hide-if]').forEach(function (n) {
    if (String(cfg[n.getAttribute('data-hide-if')] || '').trim()) n.hidden = true;
  });

  /* ---------- 3. menu, reveal, active nav ---------- */
  var menuBtn = $('.menu-btn'), nav = $('#nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
      $('.sr-only', menuBtn).textContent = menuBtn.getAttribute(open ? 'data-close' : 'data-open');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('a')) { nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); $('.sr-only', menuBtn).textContent = menuBtn.getAttribute('data-open'); }
    });
  }

  var reveals = $all('.reveal');
  if ('IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); ro.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    reveals.forEach(function (n) { ro.observe(n); });

    var links = {};
    $all('.nav a').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
    var no = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var a = links[en.target.id];
        if (a && en.isIntersecting) {
          Object.keys(links).forEach(function (k) { links[k].classList.remove('active'); });
          a.classList.add('active');
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    Object.keys(links).forEach(function (id) { var s = doc.getElementById(id); if (s) no.observe(s); });
  } else {
    reveals.forEach(function (n) { n.classList.add('in'); });
  }

  /* ---------- VARIANTS: count-up for big numbers ---------- */
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !still) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        co.unobserve(en.target);
        var end = parseInt(en.target.getAttribute('data-count'), 10), t0 = null;
        function tick(t) {
          if (t0 === null) t0 = t;
          var k = Math.min(1, (t - t0) / 900);
          en.target.textContent = String(Math.round(end * (1 - Math.pow(1 - k, 3))));
          if (k < 1) requestAnimationFrame(tick); else en.target.textContent = String(end);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    $all('[data-count]').forEach(function (n) { co.observe(n); });
  }

  /* ---------- 4. merchant finder ---------- */
  var mapEl = $('#map'), cardsEl = $('#cards');
  if (!mapEl || !cardsEl) return;

  var state = { q: '', group: '', town: '' };
  var places = [], markers = {}, cards = {}, map = null, layer = null;

  function groupLabel(g) { return I18N['group_' + g] || g; }
  function catLabel(p) { return (I18N.categories && I18N.categories[p.category]) || p.category; }

  function buildCard(p) {
    var li = el('li', 'card');
    li.setAttribute('data-id', p.id);
    li.appendChild(el('h3', null, p.name || I18N.unnamed));
    li.appendChild(el('p', 'sub', catLabel(p) + ', ' + p.town));

    var tags = el('ul', 'tags');
    if (p.lightning === 'yes') tags.appendChild(el('li', null, I18N.ln));
    if (p.onchain === 'yes') tags.appendChild(el('li', null, I18N.chain));
    if (tags.children.length) li.appendChild(tags);

    var facts = el('ul', 'facts');
    function fact(label, node) {
      var f = el('li');
      if (label) f.appendChild(el('span', 'k', label + ': '));
      f.appendChild(node);
      facts.appendChild(f);
    }
    function link(href, text) {
      var a = el('a', null, text);
      a.href = href; a.target = '_blank'; a.rel = 'noopener';
      return a;
    }
    if (p.phone) fact(I18N.phone, link('tel:' + p.phone.replace(/[^\d+]/g, ''), p.phone));
    var web = safeUrl(p.website);
    if (web) fact(null, link(web, host(web)));
    if (p.facebook) { var fb = safeUrl(p.facebook); if (fb) fact(null, link(fb, 'Facebook')); }
    if (p.instagram) fact(null, link('https://www.instagram.com/' + encodeURIComponent(p.instagram.replace(/^@/, '')) + '/', 'Instagram'));
    if (p.hours) fact(I18N.hours, doc.createTextNode(p.hours));
    fact(null, doc.createTextNode(p.survey ? I18N.survey.replace('{d}', p.survey) : I18N.survey_none));
    li.appendChild(facts);

    var b = el('button', 'btn btn-quiet', I18N.show_on_map);
    b.type = 'button';
    b.addEventListener('click', function () { focusPlace(p.id, false); });
    li.appendChild(b);
    return li;
  }

  function popupNode(p) {
    var d = el('div');
    d.appendChild(el('strong', null, p.name || I18N.unnamed));
    d.appendChild(doc.createTextNode(catLabel(p) + ', ' + p.town));
    var web = safeUrl(p.website);
    if (web) { d.appendChild(doc.createElement('br')); var a = el('a', null, host(web)); a.href = web; a.target = '_blank'; a.rel = 'noopener'; d.appendChild(a); }
    return d;
  }

  function matches(p) {
    if (state.group && p.group !== state.group) return false;
    if (state.town && p.town !== state.town) return false;
    if (state.q) {
      var hay = norm([p.name, catLabel(p), p.category, p.town, groupLabel(p.group)].join(' '));
      if (hay.indexOf(norm(state.q)) === -1) return false;
    }
    return true;
  }

  function apply(fit) {
    var shown = [];
    places.forEach(function (p) {
      var ok = matches(p);
      cards[p.id].hidden = !ok;
      if (map) {
        var m = markers[p.id];
        if (ok && !layer.hasLayer(m)) layer.addLayer(m);
        if (!ok && layer.hasLayer(m)) layer.removeLayer(m);
      }
      if (ok) shown.push(p);
    });
    $('#count').textContent = I18N.showing.replace('{n}', shown.length).replace('{total}', places.length);
    mapEl.setAttribute('data-markers', String(shown.length));
    var emptyEl = $('#empty');
    if (!shown.length && !emptyEl) { emptyEl = el('li', 'empty', I18N.empty); emptyEl.id = 'empty'; cardsEl.appendChild(emptyEl); }
    if (shown.length && emptyEl) emptyEl.remove();
    if (map && fit) {
      if (!state.q && !state.group && !state.town) map.fitBounds(BBOX);
      else if (shown.length) map.fitBounds(shown.map(function (p) { return [p.lat, p.lon]; }), { maxZoom: 16, padding: [30, 30] });
    }
    $all('.chip').forEach(function (c) { c.setAttribute('aria-pressed', String(c.getAttribute('data-group') === state.group)); });
  }

  function focusPlace(id, resetFilters) {
    var p = places.filter(function (x) { return x.id === id; })[0];
    if (!p || !map) return;
    if (resetFilters) {
      state.q = ''; state.group = ''; state.town = '';
      $('#q').value = ''; $('#town').value = '';
      apply(false);
    }
    map.setView([p.lat, p.lon], 17);
    markers[id].openPopup();
    $all('.card.is-focus').forEach(function (c) { c.classList.remove('is-focus'); });
    var c = cards[id];
    c.classList.add('is-focus');
    c.scrollIntoView({ block: 'nearest' });
    mapEl.scrollIntoView({ block: 'center', behavior: 'smooth' });
  }

  function init(data) {
    places = data.places;

    // chips and village select
    var chips = $('#chips');
    function chip(g, label, n) {
      var b = el('button', 'chip', label);
      b.type = 'button';
      b.setAttribute('data-group', g);
      b.setAttribute('aria-pressed', String(g === ''));
      b.appendChild(el('small', null, String(n)));
      b.addEventListener('click', function () { state.group = g; apply(true); });
      chips.appendChild(b);
    }
    chip('', I18N.group_all, places.length);
    GROUPS.forEach(function (g) {
      var n = places.filter(function (p) { return p.group === g; }).length;
      if (n) chip(g, groupLabel(g), n);
    });
    var counts = {};
    places.forEach(function (p) { counts[p.town] = (counts[p.town] || 0) + 1; });
    Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a] || a.localeCompare(b); }).forEach(function (t) {
      var o = el('option', null, t + ' (' + counts[t] + ')');
      o.value = t;
      $('#town').appendChild(o);
    });

    // cards
    var frag = doc.createDocumentFragment();
    places.forEach(function (p) { var c = buildCard(p); cards[p.id] = c; frag.appendChild(c); });
    cardsEl.appendChild(frag);

    // map
    if (window.L) {
      var cs = getComputedStyle(mapEl);
      var tok = function (n, d) { return (cs.getPropertyValue(n) || '').trim() || d; };
      map = L.map(mapEl, { scrollWheelZoom: false, zoomSnap: 0.5 });
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);
      map.fitBounds(BBOX);
      layer = L.layerGroup().addTo(map);
      places.forEach(function (p) {
        var m = L.circleMarker([p.lat, p.lon], { radius: parseInt(tok('--marker-r', '8'), 10), weight: 2.5, color: tok('--marker-stroke', '#0A3047'), fillColor: tok('--marker-fill', '#F7931A'), fillOpacity: 0.95 });
        m.bindPopup(function () { return popupNode(p); });
        m.on('click', function () {
          $all('.card.is-focus').forEach(function (c) { c.classList.remove('is-focus'); });
          cards[p.id].classList.add('is-focus');
          cards[p.id].scrollIntoView({ block: 'nearest' });
        });
        markers[p.id] = m;
        layer.addLayer(m);
      });
      map.on('click', function () { map.scrollWheelZoom.enable(); });
      mapEl.addEventListener('mouseleave', function () { map.scrollWheelZoom.disable(); });
    } else {
      mapEl.setAttribute('data-state', 'error');
    }

    // controls
    var qTimer;
    $('#q').addEventListener('input', function (e) {
      clearTimeout(qTimer);
      var v = e.target.value.trim();
      qTimer = setTimeout(function () { state.q = v; apply(true); }, 160);
    });
    $('#town').addEventListener('change', function (e) { state.town = e.target.value; apply(true); });
    $('#reset').addEventListener('click', function () {
      state = { q: '', group: '', town: '' };
      $('#q').value = ''; $('#town').value = '';
      apply(true);
    });
    $all('.show-btn').forEach(function (b) {
      b.addEventListener('click', function () { focusPlace(b.getAttribute('data-place-id'), true); });
    });

    apply(false);
    mapEl.setAttribute('data-state', map ? 'ready' : 'error');
    // Small hook for automated QA: counts of what is on screen.
    window.LBC_STATE = {
      places: function () { return places.length; },
      cards: function () { return cardsEl.querySelectorAll('.card').length; },
      visibleCards: function () { return cardsEl.querySelectorAll('.card:not([hidden])').length; },
      markers: function () { return layer ? layer.getLayers().length : 0; }
    };
  }

  mapEl.setAttribute('data-state', 'loading');
  fetch(BASE + 'data/merchants.json')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(init)
    .catch(function () { mapEl.setAttribute('data-state', 'error'); });
})();
