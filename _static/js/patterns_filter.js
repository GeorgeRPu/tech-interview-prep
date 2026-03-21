$(document).on('init.dt', 'table.sphinx-datatable', function (_e, settings) {
  var api = new $.fn.dataTable.Api(settings);
  var wrapper = api.table().container();

  var filtersDiv = $('<div style="margin-bottom:1em;display:flex;gap:1.5em;flex-wrap:wrap;align-items:center;"></div>');

  // Difficulty dropdown
  var diffSel = $('<select><option value="">All Difficulties</option></select>');
  ['\ud83d\udfe2 Easy', '\ud83d\udfe1 Medium', '\ud83d\udd34 Hard'].forEach(function (d) {
    diffSel.append($('<option>').val(d).text(d));
  });
  diffSel.on('change', function () {
    var val = $(this).val();
    api.column(1).search(val ? '^' + $.fn.dataTable.util.escapeRegex(val) + '$' : '', true, false).draw();
  });
  filtersDiv.append($('<label style="font-weight:bold;">Difficulty:\u00a0</label>').append(diffSel));

  // Pattern dropdown — strip HTML tags, then split comma-separated values
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
  filtersDiv.append($('<label style="font-weight:bold; margin-left:.5em;">Pattern:\u00a0</label>').append(patSel));

  $(wrapper).before(filtersDiv);
});
