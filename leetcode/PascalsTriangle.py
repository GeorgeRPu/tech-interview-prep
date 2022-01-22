"""
Problem
-------
https://leetcode.com/problems/pascals-triangle/

Solution
--------
Right align the normal presentation of Pascal's Triangle.

    1        1
   1 1       1 1
  1 2 1  --> 1 2 1
 1 3 3 1     1 3 3 1
1 4 6 4 1    1 4 6 4 1

A middle entry is the sum of the entry directly above and to the north-west.
The first/last entry is always 1.
"""

from pprint import pprint
from typing import List


def generate_pascals_triangle(n_rows: int) -> List[List[int]]:
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


pprint(generate_pascals_triangle(3))
pprint(generate_pascals_triangle(6))
