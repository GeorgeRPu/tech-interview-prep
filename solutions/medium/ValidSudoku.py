"""
Problem
-------
https://leetcode.com/problems/valid-sudoku/

Determine if a ``9 x 9`` Sudoku board is valid. Only the filled cells
need to be validated **according to the following rules**:

#. Each row must contain the digits ``1-9`` without repetition.
#. Each column must contain the digits ``1-9`` without repetition.
#. Each of the nine ``3 x 3`` sub-boxes of the grid must contain the
   digits ``1-9`` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not
  necessarily solvable.
- Only the filled cells need to be validated according to the
  mentioned rules.

 

**Example 1:**

|image1|

::


   Input: board = 
   [["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]
   Output: true

**Example 2:**

::


   Input: board = 
   [["8","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]
   Output: false
   Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

**Constraints:**

- ``board.length == 9``
- ``board[i].length == 9``
- ``board[i][j]`` is a digit ``1-9`` or ``'.'``.

.. |image1| image:: https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png

Solution
--------
Check that each row, column, and 3x3 square contains no duplicates and contains
the digits 1-9. Return ``False`` if these conditions don't hold.

Pattern
-------
Array, Hash Table, Matrix

Code
----

.. literalinclude:: ../solutions/medium/ValidSudoku.py
    :language: python
    :lines: 117-

Test
----
>>> from ValidSudoku import isValidSudoku
>>> board = [
...     ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
...     ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
...     ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
...     ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
...     ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
...     ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
...     ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
...     ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
...     ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
... ]
>>> isValidSudoku(board)
True
>>> board = [
...     ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
...     ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
...     ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
...     ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
...     ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
...     ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
...     ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
...     ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
...     ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
... ]
>>> isValidSudoku(board)
False
"""

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    """Check that ``board`` is a valid sudoku board.
    """
    for i in range(9):
        row = board[i]
        if not is_valid(row):
            return False

    for j in range(9):
        col = [board[i][j] for i in range(9)]
        if not is_valid(col):
            return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            square = [board[x + i][y + j] for i in range(3) for j in range(3)]
            if not is_valid(square):
                return False

    return True


one_through_nine = [str(i) for i in range(1, 10)]


def is_valid(cells: List[str]) -> bool:
    """Check that ``cells`` has no duplicates and contains the digits 1-9.
    """
    nums = [cell for cell in cells if cell != '.']

    if len(set(nums)) < len(nums):
        return False

    for num in nums:
        if num not in one_through_nine:
            return False

    return True
