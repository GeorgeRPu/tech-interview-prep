"""
Problem
-------
https://leetcode.com/problems/set-matrix-zeroes/

Solution
--------
We make 2 passes over  ``matrix``. In the first pass, we find all the indices
where ``matrix[i][j] == 0`` and store them in a list. In the second pass, we
zero all the rows and columns in the list of indices. We can make a small
optimization to convert the indices to a seet to avoid setting a row or column
to zero twice.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/SetMatrixZeroes.py

.. literalinclude:: ../solutions/medium/SetMatrixZeroes.py
    :language: python
    :lines: 35-

Test
----
>>> from SetMatrixZeroes import setZeroes
>>> matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
>>> setZeroes(matrix)
>>> matrix
[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
>>> matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
>>> setZeroes(matrix)
>>> matrix
[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """Set rows and columns to zero if an element is zero.

    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])

    indices = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                indices.append((i, j))

    if len(indices) == 0:
        return

    rows_to_zero, columns_to_zero = zip(*indices)
    rows_to_zero = set(rows_to_zero)
    columns_to_zero = set(columns_to_zero)

    for i in rows_to_zero:
        for j in range(n):
            matrix[i][j] = 0

    for j in columns_to_zero:
        for i in range(m):
            matrix[i][j] = 0
