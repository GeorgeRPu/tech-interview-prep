$(document).on('init.dt', 'table.sphinx-datatable', function (_e, settings) {
  if (!$(this).hasClass('coverage-datatable')) return;

  var api = new $.fn.dataTable.Api(settings);
  var wrapper = api.table().container();

  var filtersDiv = $('<div style="margin-bottom:1em;display:flex;gap:1.5em;flex-wrap:wrap;align-items:center;"></div>');

  // Pattern dropdown — discover unique values from column 1
  var patterns = [];
  api.column(1).data().each(function (d) {
    var text = $('<div>').html(d).text().trim();
    if (text && patterns.indexOf(text) === -1) patterns.push(text);
  });
  patterns.sort();
  var patSel = $('<select><option value="">All Patterns</option></select>');
  patterns.forEach(function (p) { patSel.append($('<option>').val(p).text(p)); });
  patSel.on('change', function () {
    var val = $(this).val();
    var esc = val ? $.fn.dataTable.util.escapeRegex(val) : '';
    api.column(1).search(val ? '^' + esc + '$' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">Pattern:\u00a0</label>').append(patSel));

  // Lists dropdown — column 2 may contain "Blind 75", "NeetCode 150", or both
  var listSel = $('<select><option value="">All Lists</option></select>');
  ['Blind 75', 'Grind 75', 'Grind 169', 'NeetCode 150'].forEach(function (l) {
    listSel.append($('<option>').val(l).text(l));
  });
  listSel.on('change', function () {
    var val = $(this).val();
    var esc = val ? $.fn.dataTable.util.escapeRegex(val) : '';
    api.column(2).search(val ? '(^|, )' + esc + '(,|$)' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">List:\u00a0</label>').append(listSel));

  // Status dropdown (column 3)
  var statusSel = $('<select><option value="">All Statuses</option></select>');
  ['\u2705 Covered', '\u2b1c Missing', '\ud83d\udd12 Premium'].forEach(function (s) {
    statusSel.append($('<option>').val(s).text(s));
  });
  statusSel.on('change', function () {
    var val = $(this).val();
    var esc = val ? $.fn.dataTable.util.escapeRegex(val) : '';
    api.column(3).search(val ? '^' + esc + '$' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">Status:\u00a0</label>').append(statusSel));

  $(wrapper).before(filtersDiv);
});
