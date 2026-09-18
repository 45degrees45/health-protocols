(function () {
  'use strict';

  var TRACKER = 'http://' + location.hostname + ':8768/track';

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
  });
})();
