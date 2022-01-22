# LeetCode Solutions

Each solution file should have the following structure. Some imports must be at the very top of the file.

```python
"""docstring
"""

# imports

# helper classes/functions

def solution():
    pass
# ======== OR ===========
class Solution:
    pass

# examples
```

Examples should be comprehensive. The state of relevant variables should be logged between changes, as well as before and after the solution code executes. Use pprint (pretty print) instead of print when nessecary.

All code should pass mypy type checks without any issues.

```bash
mypy [filename.py]
```

## Docstring Format

```
Problem
-------
[problem statement or link]

Solution
--------
[description of solution]
```

Non-obvious solutions must include reasonsing explaining how a reader could develop that solution on their own. Any math should be in LaTeX.
