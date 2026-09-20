(function () {
  'use strict';

  var TRACKER = 'http://' + location.hostname + ':8768/track';
  var TAG = '45degrees45-21';

  function profileName() {
    var h1 = document.querySelector('.page-header h1') || document.querySelector('h1');
    return h1 ? h1.textContent.trim() : document.title;
  }

  function productName(row) {
    var s = row.querySelector('.product-name') || row.querySelector('td strong');
    return s ? s.textContent.trim() : 'Unknown';
  }

  function track(row, buy) {
    buy.addEventListener('click', function () {
      try {
        fetch(
          TRACKER + '?p=' + encodeURIComponent(profileName()) + '&n=' + encodeURIComponent(productName(row)),
          { mode: 'no-cors', keepalive: true }
        );
      } catch (e) {}
    });
  }

  function buildCartUrl(hrefs) {
    var base = 'https://www.amazon.in/gp/aws/cart/add.html?tag=' + TAG;
    var count = 0;
    hrefs.forEach(function (href) {
      var m = href.match(/\/dp\/([A-Z0-9]{10})/);
      if (m) {
        count++;
        base += '&ASIN.' + count + '=' + m[1] + '&Quantity.' + count + '=1';
      }
    });
    return count > 0 ? { url: base, count: count } : null;
  }

  function injectCartBar(cart, beforeEl) {
    var bar = document.createElement('div');
    bar.className = 'cart-all-bar';

    var msg = document.createElement('span');
    msg.textContent = cart.count + ' product' + (cart.count > 1 ? 's' : '') + ' in this section';
    bar.appendChild(msg);

    var btn = document.createElement('a');
    btn.href = cart.url;
    btn.target = '_blank';
    btn.rel = 'noopener';
    btn.className = 'btn-cart-all';
    btn.textContent = 'Add all to Amazon cart →';
    bar.appendChild(btn);

    beforeEl.parentNode.insertBefore(bar, beforeEl);
  }

  document.addEventListener('DOMContentLoaded', function () {
    // New div-based product rows (Design A)
    document.querySelectorAll('.product-row').forEach(function (row) {
      var buy = row.querySelector('a.btn-buy');
      if (buy) track(row, buy);
    });

    // Legacy table rows (research pages) — inject photo column and track
    document.querySelectorAll('.product-table thead tr').forEach(function (headerRow) {
      var th = document.createElement('th');
      th.textContent = 'Photo';
      th.className = 'th-photo';
      headerRow.insertBefore(th, headerRow.firstChild);
    });

    document.querySelectorAll('.product-table tbody tr').forEach(function (row) {
      var buy = row.querySelector('a.btn-amazon');
      var imgCell = document.createElement('td');
      imgCell.className = 'product-img';

      if (buy) {
        var m = buy.href.match(/\/dp\/([A-Z0-9]+)/);
        if (m) {
          var img = document.createElement('img');
          img.src = 'assets/images/products/' + m[1] + '.jpg';
          img.alt = '';
          img.loading = 'lazy';
          img.onerror = function () { this.style.display = 'none'; };
          imgCell.appendChild(img);
        }
        track(row, buy);
      }

      row.insertBefore(imgCell, row.firstChild);
    });

    // Add-all-to-cart bar — one per product-grid section
    document.querySelectorAll('.product-grid').forEach(function (grid) {
      var hrefs = Array.from(grid.querySelectorAll('a.btn-buy, a.btn-amazon'))
        .map(function (a) { return a.href; });
      var cart = buildCartUrl(hrefs);
      if (cart) {
        injectCartBar(cart, grid.nextSibling || grid.parentNode.lastChild);
      }
    });
  });
})();
