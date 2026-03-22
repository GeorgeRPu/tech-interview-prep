/**
 * Interactive code runner for solution pages.
 *
 * Detects solution pages by looking for section#code with a Python highlight
 * block, extracts the code and doctests, and replaces the static block with
 * a CodeMirror editor (loaded from CDN).  The editor is always editable.
 * Pyodide is loaded lazily on first Run click.
 */
document.addEventListener('DOMContentLoaded', function () {
  var codeSection = document.getElementById('code');
  if (!codeSection) return;

  var highlightDiv = codeSection.querySelector('.highlight-python');
  var highlightPre = highlightDiv ? highlightDiv.querySelector('pre') : null;
  if (!highlightPre) return;

  var testSection = document.getElementById('test');
  var doctestBlock = testSection
    ? testSection.querySelector('.doctest pre')
    : null;

  var sourceCode = highlightPre.textContent;
  var testCalls = doctestBlock ? parseDoctests(sourceCode, doctestBlock.textContent) : '';

  var initialCode = testCalls
    ? sourceCode + '\n\n# --- Test Cases ---\n' + testCalls
    : sourceCode;

  buildWidget(codeSection, highlightDiv, initialCode);
});

/**
 * Parse doctest text into plain Python calls.
 */
function parseDoctests(sourceCode, text) {
  var lines = text.split('\n');
  var result = [];
  var i = 0;

  while (i < lines.length) {
    var line = lines[i];

    if (line.match(/^>>> /)) {
      var code = line.slice(4);

      while (i + 1 < lines.length && lines[i + 1].match(/^\.\.\. /)) {
        i++;
        code += '\n' + lines[i].slice(4);
      }

      if (code.match(/^from\s+\S+\s+import\s+/)) {
        i++;
        continue;
      }

      if (isExpression(code)) {
        code = 'print(' + code + ')';
      }

      result.push(code);
    }
    i++;
  }

  return result.join('\n');
}

/**
 * Heuristic: returns true if `code` looks like a bare expression that should
 * be wrapped in print() to show output.
 */
function isExpression(code) {
  if (code.indexOf('\n') !== -1) return false;
  var stmtPat = /^(import |from |class |def |if |elif |else:|for |while |with |try:|except |finally:|raise |return |assert |del |pass|break|continue)/;
  if (stmtPat.test(code)) return false;
  if (code.match(/^[^=]+=(?!=)/) && !code.match(/^print\s*\(/)) return false;
  if (code.match(/^print\s*\(/)) return false;
  return true;
}

/* --- CodeMirror lazy loader --- */

var cmReady = null;

function loadCodeMirrorOnce() {
  if (cmReady) return cmReady;

  var CM_VERSION = '5.65.18';
  var CDN = 'https://cdn.jsdelivr.net/npm/codemirror@' + CM_VERSION;

  cmReady = new Promise(function (resolve, reject) {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = CDN + '/lib/codemirror.min.css';
    document.head.appendChild(link);

    var script = document.createElement('script');
    script.src = CDN + '/lib/codemirror.min.js';
    script.onload = function () {
      var mode = document.createElement('script');
      mode.src = CDN + '/mode/python/python.min.js';
      mode.onload = function () { resolve(window.CodeMirror); };
      mode.onerror = reject;
      document.head.appendChild(mode);
    };
    script.onerror = reject;
    document.head.appendChild(script);
  });

  return cmReady;
}

/**
 * Build the interactive widget: replace the static Pygments block with a
 * CodeMirror editor, plus Run / Reset buttons and an output area.
 */
function buildWidget(codeSection, highlightDiv, initialCode) {
  var cmInstance = null;

  // Toolbar
  var toolbar = document.createElement('div');
  toolbar.className = 'pyodide-toolbar';

  var runBtn = document.createElement('button');
  runBtn.className = 'pyodide-run-btn';
  runBtn.textContent = '\u25b6 Run';
  runBtn.title = 'Run code (loads Python runtime on first use)';

  var resetBtn = document.createElement('button');
  resetBtn.className = 'pyodide-reset-btn';
  resetBtn.textContent = '\u21ba Reset';
  resetBtn.title = 'Reset to original code';

  var status = document.createElement('span');
  status.className = 'pyodide-status';

  toolbar.appendChild(runBtn);
  toolbar.appendChild(resetBtn);
  toolbar.appendChild(status);

  // Editor container
  var editorWrap = document.createElement('div');
  editorWrap.className = 'pyodide-editor-wrap';

  // Output
  var output = document.createElement('pre');
  output.className = 'pyodide-output';

  // Replace the static highlight block with our widget
  highlightDiv.parentNode.insertBefore(toolbar, highlightDiv);
  highlightDiv.parentNode.insertBefore(editorWrap, highlightDiv);
  highlightDiv.parentNode.insertBefore(output, highlightDiv);
  highlightDiv.style.display = 'none';

  // Load CodeMirror and initialize the editor
  loadCodeMirrorOnce().then(function (CodeMirror) {
    cmInstance = CodeMirror(editorWrap, {
      value: initialCode,
      mode: 'python',
      theme: 'pygments-match',
      lineNumbers: true,
      indentUnit: 4,
      tabSize: 4,
      indentWithTabs: false,
      extraKeys: { 'Tab': 'indentMore', 'Shift-Tab': 'indentLess' },
      viewportMargin: Infinity
    });
  });

  function getCode() {
    return cmInstance ? cmInstance.getValue() : initialCode;
  }

  runBtn.addEventListener('click', function () {
    runCode(getCode(), output, runBtn, status);
  });

  resetBtn.addEventListener('click', function () {
    if (cmInstance) cmInstance.setValue(initialCode);
    output.textContent = '';
    output.className = 'pyodide-output';
    status.textContent = '';
    status.className = 'pyodide-status';
  });
}

/* --- Pyodide runtime --- */

var pyodidePromise = null;

function loadPyodideOnce() {
  if (pyodidePromise) return pyodidePromise;

  pyodidePromise = new Promise(function (resolve, reject) {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/pyodide/v0.27.5/full/pyodide.js';
    script.onload = function () {
      /* global loadPyodide */
      loadPyodide().then(resolve).catch(reject);
    };
    script.onerror = function () {
      pyodidePromise = null;
      reject(new Error('Failed to load Pyodide from CDN'));
    };
    document.head.appendChild(script);
  });

  return pyodidePromise;
}

function runCode(code, outputEl, runBtn, statusEl) {
  outputEl.textContent = '';
  outputEl.className = 'pyodide-output';
  runBtn.disabled = true;
  statusEl.textContent = 'Loading Python runtime\u2026';
  statusEl.className = 'pyodide-status pyodide-status-loading';

  loadPyodideOnce()
    .then(function (pyodide) {
      statusEl.textContent = 'Running\u2026';

      var collected = '';
      pyodide.setStdout({
        batched: function (text) { collected += text + '\n'; }
      });
      pyodide.setStderr({
        batched: function (text) { collected += text + '\n'; }
      });

      return pyodide.runPythonAsync(code).then(function () {
        outputEl.textContent = collected;
        statusEl.textContent = 'Done';
        statusEl.className = 'pyodide-status';
      });
    })
    .catch(function (err) {
      var msg = err && err.message ? err.message : String(err);
      outputEl.textContent = (outputEl.textContent || '') + msg + '\n';
      outputEl.className = 'pyodide-output pyodide-output-error';
      statusEl.textContent = 'Error';
      statusEl.className = 'pyodide-status';
    })
    .finally(function () {
      runBtn.disabled = false;
    });
}
