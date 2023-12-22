"""
Problem
-------
https://leetcode.com/problems/valid-sudoku/

Solution
--------
Check that each row, column, and 3x3 square contains no duplicates and contains
the digits 1-9. Return ``False`` if these conditions don't hold.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/ValidSudoku.py

.. literalinclude:: ../solutions/medium/ValidSudoku.py
    :language: python
    :lines: 50-

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
