r"""
Problem
-------
https://leetcode.com/problems/game-of-life/

According to `Wikipedia's
article <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>`__: "The
**Game of Life**, also known simply as **Life**, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970."

The board is made up of an ``m x n`` grid of cells, where each cell has
an initial state: **live** (represented by a ``1``) or **dead**
(represented by a ``0``). Each cell interacts with its `eight
neighbors <https://en.wikipedia.org/wiki/Moore_neighborhood>`__
(horizontal, vertical, diagonal) using the following four rules (taken
from the above Wikipedia article):

#. Any live cell with fewer than two live neighbors dies as if caused by
   under-population.
#. Any live cell with two or three live neighbors lives on to the next
   generation.
#. Any live cell with more than three live neighbors dies, as if by
   over-population.
#. Any dead cell with exactly three live neighbors becomes a live cell,
   as if by reproduction.

The next state of the board is determined by applying the above rules
simultaneously to every cell in the current state of the ``m x n`` grid
``board``. In this process, births and deaths occur **simultaneously**.

Given the current state of the ``board``, **update** the ``board`` to
reflect its next state.

**Note** that you do not need to return anything.

 

**Example 1:**

|image1|

::


   Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
   Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

**Example 2:**

|image2|

::


   Input: board = [[1,1],[1,0]]
   Output: [[1,1],[1,1]]

 

**Constraints:**

- ``m == board.length``
- ``n == board[i].length``
- ``1 <= m, n <= 25``
- ``board[i][j]`` is ``0`` or ``1``.

 

**Follow up:**

- Could you solve it in-place? Remember that the board needs to be
  updated simultaneously: You cannot update some cells first and then
  use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In
  principle, the board is infinite, which would cause problems when the
  active area encroaches upon the border of the array (i.e., live cells
  reach the border). How would you address these problems?

.. |image1| image:: https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg

Solution
--------
Observe that we can calulate the number of live neighbors by summing the
surrounding :math:`\mathtt{board[i'][j']}` values. Use a list comprehension to
get the neighbor indices, only taking those where :math:`0 \leq i' < m` and
:math:`0 \leq j < n`. Make sure to calculate the number of live neighbors for
each cell before updating the board.

Pattern
-------
Array, Matrix, Simulation

Code
----

.. literalinclude:: ../solutions/medium/GameOfLife.py
    :language: python
    :lines: 114-

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
