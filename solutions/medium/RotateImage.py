"""
Problem
-------
https://leetcode.com/problems/rotate-image/

Solution
--------
Because we need to rotate the square ``matrix`` in-place, we must rotate
related entries in a spiral. Let :math:`m` be the length of ``matrix`` minus 1.
Starting from any position :math:`(i, j)`, we need to rotate ::

    matrix[i][j] <- matrix[m - j][i] <- matrix[m - i][m - j] <- matrix[j][m - i] <- matrix[i][j]

where ``matrix[i][j]`` is saved in a temporary variable for ``matrix[j][m - i]``
to use later.

Since we are rotating 4 elements at a time, we cannot perform the
rotation for each entry in the matrix. Note that, except for the first entry in
the first row, no entry in the first row is rotated more than once. So we
iterate :math:`j = 0, 1, \dots, m - 1`. Afterwards the outermost shell of
``matrix`` is rotated. For each :math:`i = 0, 1, \dots, m - 1`, we only perform
a rotation for :math:`j = i, 2, \dots, m - i`.

Code
----

.. literalinclude:: ../solutions/medium/RotateImage.py
    :language: python
    :lines: 42-

Test
----
>>> from RotateImage import rotate
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> rotate(matrix)
>>> matrix
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
>>> matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
>>> rotate(matrix)
>>> matrix
[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
"""

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    m = n - 1

    for i in range(n):
        for j in range(i, m - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[m - j][i]
            matrix[m - j][i] = matrix[m - i][m - j]
            matrix[m - i][m - j] = matrix[j][m - i]
            matrix[j][m - i] = temp
