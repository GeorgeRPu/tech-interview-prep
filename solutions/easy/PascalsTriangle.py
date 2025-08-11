"""
Problem
-------
https://leetcode.com/problems/pascals-triangle/

Solution
--------
Right align the normal presentation of Pascal's Triangle. ::

        1        1
       1 1       1 1
      1 2 1  --> 1 2 1
     1 3 3 1     1 3 3 1
    1 4 6 4 1    1 4 6 4 1

Observe that a middle entry is the sum of the entry directly above and to the
north-west. The first/last entry is always 1.

Code
----

.. literalinclude:: ../solutions/easy/PascalsTriangle.py
    :language: python
    :lines: 33-

Test
----
>>> from PascalsTriangle import generate
>>> generate(3)
[[1], [1, 1], [1, 2, 1]]
>>> generate(6)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
"""

from typing import List


def generate(n_rows: int) -> List[List[int]]:
    """Generate Pascal's Triangle with ``n_rows``.
    """
    rows = [[1]]
    for i in range(1, n_rows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(rows[i - 1][j - 1] + rows[i - 1][j])
        rows.append(row)
    return rows
