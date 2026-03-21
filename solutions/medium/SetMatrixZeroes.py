"""
Problem
-------
https://leetcode.com/problems/set-matrix-zeroes/

Given an ``m x n`` integer matrix ``matrix``, if an element is ``0``,
set its entire row and column to ``0``'s.

You must do it `in
place <https://en.wikipedia.org/wiki/In-place_algorithm>`__.

 

**Example 1:**

|image1|

::


   Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
   Output: [[1,0,1],[0,0,0],[1,0,1]]

**Example 2:**

|image2|

::


   Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
   Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

 

**Constraints:**

- ``m == matrix.length``
- ``n == matrix[0].length``
- ``1 <= m, n <= 200``
- ``-2``\ :sup:```31```\ ``<= matrix[i][j] <= 2``\ :sup:```31```\ ``- 1``

 

**Follow up:**

- A straightforward solution using ``O(mn)`` space is probably a bad
  idea.
- A simple improvement uses ``O(m + n)`` space, but still not the best
  solution.
- Could you devise a constant space solution?

.. |image1| image:: https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg

Solution
--------
We make 2 passes over  ``matrix``. In the first pass, we find all the indices
where ``matrix[i][j] == 0`` and store them in a list. In the second pass, we
zero all the rows and columns in the list of indices. We can make a small
optimization to convert the indices to a seet to avoid setting a row or column
to zero twice.

Pattern
-------
Array, Hash Table, Matrix

Code
----

.. literalinclude:: ../solutions/medium/SetMatrixZeroes.py
    :language: python
    :lines: 88-

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
