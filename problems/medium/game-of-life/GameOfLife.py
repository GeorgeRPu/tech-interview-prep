r"""
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
