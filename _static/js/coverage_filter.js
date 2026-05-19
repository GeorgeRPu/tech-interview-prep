$(document).on('init.dt', 'table.sphinx-datatable', function (_e, settings) {
  if (!$(this).hasClass('coverage-datatable')) return;

  var api = new $.fn.dataTable.Api(settings);
  var wrapper = api.table().container();

  var filtersDiv = $('<div style="margin-bottom:1em;display:flex;gap:1.5em;flex-wrap:wrap;align-items:center;"></div>');

  // Difficulty dropdown (column 1)
  var diffSel = $('<select><option value="">All Difficulties</option></select>');
  ['🟢 Easy', '🟡 Medium', '🔴 Hard'].forEach(function (d) {
    diffSel.append($('<option>').val(d).text(d));
  });
  diffSel.on('change', function () {
    var val = $(this).val();
    api.column(1).search(val ? '^' + $.fn.dataTable.util.escapeRegex(val) + '$' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">Difficulty: </label>').append(diffSel));

  // Pattern dropdown (column 2) — discover unique comma-separated values
  var patterns = [];
  api.column(2).data().each(function (d) {
    var text = $('<div>').html(d).text();
    text.split(',').forEach(function (p) {
      p = p.trim();
      if (p && patterns.indexOf(p) === -1) patterns.push(p);
    });
  });
  patterns.sort();
  var patSel = $('<select><option value="">All Patterns</option></select>');
  patterns.forEach(function (p) { patSel.append($('<option>').val(p).text(p)); });
  patSel.on('change', function () {
    var val = $(this).val();
    var esc = val ? $.fn.dataTable.util.escapeRegex(val) : '';
    api.column(2).search(val ? '(^|, )' + esc + '(,|$)' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">Pattern: </label>').append(patSel));

  // Lists dropdown (column 3) — discover unique comma-separated values
  var lists = [];
  api.column(3).data().each(function (d) {
    var text = $('<div>').html(d).text().trim();
    if (!text) return;
    text.split(', ').forEach(function (l) {
      l = l.trim();
      if (l && lists.indexOf(l) === -1) lists.push(l);
    });
  });
  lists.sort();
  var listSel = $('<select><option value="">All Lists</option></select>');
  lists.forEach(function (l) {
    listSel.append($('<option>').val(l).text(l));
  });
  listSel.on('change', function () {
    var val = $(this).val();
    var esc = val ? $.fn.dataTable.util.escapeRegex(val) : '';
    api.column(3).search(val ? '(^|, )' + esc + '(,|$)' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">List: </label>').append(listSel));

  // Status dropdown (column 4)
  var statusSel = $('<select><option value="">All Statuses</option></select>');
  ['✅ Covered', '⬜ Missing', '🔒 Premium'].forEach(function (s) {
    statusSel.append($('<option>').val(s).text(s));
  });
  statusSel.on('change', function () {
    var val = $(this).val();
    var esc = val ? $.fn.dataTable.util.escapeRegex(val) : '';
    api.column(4).search(val ? '^' + esc + '$' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">Status: </label>').append(statusSel));

  $(wrapper).before(filtersDiv);
});
