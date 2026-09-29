/* ==========================================================================
   GRAFICO "I NUMERI" — crescita del team per area di competenza
   Legge window.NUMERI_DATA (js/numeri-data.js) e disegna un grafico a
   barre impilate in #numeri-chart, con legenda in #numeri-legend.
   Nessuna libreria esterna.
   ========================================================================== */
(function () {
  var DATA = window.NUMERI_DATA;
  var mount = document.getElementById('numeri-chart');
  var legendMount = document.getElementById('numeri-legend');
  if (!DATA || !mount || !DATA.serie || !DATA.clusters || DATA.serie.length < 2) return;

  var clusters = DATA.clusters;
  var serie = DATA.serie;
  var n = serie.length;

  function totalOf(valori) {
    return clusters.reduce(function (sum, c) { return sum + (valori[c.id] || 0); }, 0);
  }

  var totals = serie.map(function (d) { return totalOf(d.valori); });
  var maxTotal = Math.max.apply(null, totals);
  var niceMax = Math.max(5, Math.ceil(maxTotal / 5) * 5);
  var gridSteps = 4;

  var W = 800, H = 340;
  var padL = 36, padR = 16, padT = 34, padB = 36;
  var chartW = W - padL - padR;
  var chartH = H - padT - padB;
  var xStep = chartW / n;
  var barW = Math.min(46, xStep * 0.56);

  function xAt(i) { return padL + xStep * i + (xStep - barW) / 2; }
  function yAt(v) { return padT + chartH * (1 - v / niceMax); }

  var svgNS = 'http://www.w3.org/2000/svg';
  var svg = document.createElementNS(svgNS, 'svg');
  svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
  svg.setAttribute('class', 'numeri-chart__svg');
  svg.setAttribute('aria-hidden', 'true');

  /* Griglia orizzontale + etichette numeriche */
  for (var g = 0; g <= gridSteps; g++) {
    var gv = (niceMax / gridSteps) * g;
    var gy = yAt(gv);

    var line = document.createElementNS(svgNS, 'line');
    line.setAttribute('x1', padL);
    line.setAttribute('x2', W - padR);
    line.setAttribute('y1', gy);
    line.setAttribute('y2', gy);
    line.setAttribute('class', 'numeri-chart__grid');
    svg.appendChild(line);

    var label = document.createElementNS(svgNS, 'text');
    label.setAttribute('x', padL - 8);
    label.setAttribute('y', gy + 4);
    label.setAttribute('text-anchor', 'end');
    label.setAttribute('class', 'numeri-chart__axis-label');
    label.textContent = Math.round(gv);
    svg.appendChild(label);
  }

  /* Barre impilate, una per anno */
  serie.forEach(function (d, i) {
    var x = xAt(i);
    var yCursor = padT + chartH;
    var group = document.createElementNS(svgNS, 'g');
    group.setAttribute('class', 'numeri-bar-group');

    clusters.forEach(function (c, ci) {
      var v = d.valori[c.id] || 0;
      if (!v) return;
      var segH = chartH * (v / niceMax);
      var rect = document.createElementNS(svgNS, 'rect');
      rect.setAttribute('x', x);
      rect.setAttribute('width', barW);
      rect.setAttribute('y', yCursor - segH);
      rect.setAttribute('height', segH);
      rect.setAttribute('class', 'numeri-bar-seg');
      rect.style.fill = c.color;
      rect.style.transitionDelay = (i * 0.08 + ci * 0.03).toFixed(2) + 's';

      var title = document.createElementNS(svgNS, 'title');
      title.textContent = c.label + ' — ' + d.anno + ': ' + v;
      rect.appendChild(title);

      group.appendChild(rect);
      yCursor -= segH;
    });

    var totalLabel = document.createElementNS(svgNS, 'text');
    totalLabel.setAttribute('x', x + barW / 2);
    totalLabel.setAttribute('y', Math.max(padT - 10, yCursor - 10));
    totalLabel.setAttribute('text-anchor', 'middle');
    totalLabel.setAttribute('class', 'numeri-chart__total');
    totalLabel.style.transitionDelay = (i * 0.08 + 0.25).toFixed(2) + 's';
    totalLabel.textContent = totals[i];
    group.appendChild(totalLabel);

    var yearLabel = document.createElementNS(svgNS, 'text');
    yearLabel.setAttribute('x', x + barW / 2);
    yearLabel.setAttribute('y', H - 10);
    yearLabel.setAttribute('text-anchor', 'middle');
    yearLabel.setAttribute('class', 'numeri-chart__year');
    yearLabel.textContent = d.anno;
    group.appendChild(yearLabel);

    svg.appendChild(group);
  });

  mount.innerHTML = '';
  mount.appendChild(svg);

  /* Badge riassuntivo sopra il grafico */
  var summary = document.getElementById('numeri-summary');
  if (summary) {
    var firstTotal = totals[0];
    var lastTotal = totals[n - 1];
    var growthPct = firstTotal ? Math.round(((lastTotal - firstTotal) / firstTotal) * 100) : 0;
    summary.innerHTML =
      '<span class="numeri-chart__summary-value">' + lastTotal + '</span>' +
      '<span class="numeri-chart__summary-label">professionisti attivi nel ' + serie[n - 1].anno +
      ' — team cresciuto del ' + (growthPct >= 0 ? '+' : '') + growthPct + '% dal ' + serie[0].anno +
      ', in tutte le aree di competenza</span>';
  }

  /* Legenda con le aree e i ruoli che le compongono */
  if (legendMount) {
    legendMount.innerHTML = clusters.map(function (c) {
      var last = serie[n - 1].valori[c.id] || 0;
      return '<div class="numeri-chart__legend-item">' +
        '<span class="numeri-chart__legend-swatch" style="background:' + c.color + '"></span>' +
        '<span><strong>' + c.label + '</strong> — ' + last + ' persone<br>' +
        '<span class="numeri-chart__legend-roles">' + c.ruoli + '</span></span>' +
        '</div>';
    }).join('');
  }

  /* Animazione all'ingresso in viewport (rispetta prefers-reduced-motion) */
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduceMotion) {
    mount.classList.add('is-visible');
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      mount.classList.add('is-visible');
      io.unobserve(entry.target);
    });
  }, { threshold: 0.3 });
  io.observe(mount);
})();
