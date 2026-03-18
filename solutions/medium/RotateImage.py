"""
Problem
-------
https://leetcode.com/problems/rotate-image/

You are given an ``n x n`` 2D ``matrix`` representing an image, rotate
the image by **90** degrees (clockwise).

You have to rotate the image
`in-place <https://en.wikipedia.org/wiki/In-place_algorithm>`__, which
means you have to modify the input 2D matrix directly. **DO NOT**
allocate another 2D matrix and do the rotation.

 

**Example 1:**

|image1|

::


   Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
   Output: [[7,4,1],[8,5,2],[9,6,3]]

**Example 2:**

|image2|

::


   Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
   Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

 

**Constraints:**

- ``n == matrix.length == matrix[i].length``
- ``1 <= n <= 20``
- ``-1000 <= matrix[i][j] <= 1000``

.. |image1| image:: https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg

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
    :lines: 85-

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
