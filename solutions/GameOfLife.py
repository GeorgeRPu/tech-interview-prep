__doc__ = r"""
Problem
-------
https://leetcode.com/problems/game-of-life/

Solution
--------
Observe that we can calulate the number of live neighbors by summing the
surrounding :math:`\mathtt{board[i'][j']}` values. Use a list comprehension to
get the neighbor indices, only taking those where :math:`0 \leq i' < m` and
:math:`0 \leq j < n`. Make sure to calculate the number of live neighbors for
each cell before updating the board.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/AddTwoNumbers.py

.. literalinclude:: ../solutions/AddTwoNumbers.py
    :language: python
    :lines: 35-

Test
----
>>> from GameOfLife import gameOfLife
>>> board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
>>> gameOfLife(board)
>>> board
[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
>>> board = [[1, 1], [1, 0]]
>>> gameOfLife(board)
>>> board
[[1, 1], [1, 1]]
"""

from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    """Advance the board for Conway's Game of Life by one step.

    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])

    num_live_neighbors = []

    for i, row in enumerate(board):
        num_live_neighbors_row = []
        for j, cell in enumerate(row):
            neighbor_indices = [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1)
            ]
            neighbors = [
                board[i_][j_]
                for i_, j_ in neighbor_indices
                if 0 <= i_ < m and 0 <= j_ < n
            ]
            num_live_neighbors_row.append(sum(neighbors))
        num_live_neighbors.append(num_live_neighbors_row)

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                if num_live_neighbors[i][j] == 3:
                    board[i][j] = 1
            else:
                if num_live_neighbors[i][j] < 2:
                    board[i][j] = 0
                elif num_live_neighbors[i][j] < 4:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
