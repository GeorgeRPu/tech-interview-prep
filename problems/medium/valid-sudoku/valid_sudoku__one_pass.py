r"""
>>> from valid_sudoku__one_pass import isValidSudoku
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

from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    """Check that ``board`` is a valid sudoku board in a single pass."""
    rows = defaultdict(set)
    columns = defaultdict(set)
    squares = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board[0])):
            cell = board[i][j]

            if cell == ".":
                continue

            if (
                cell in rows[i]
                or cell in columns[j]
                or cell in squares[(i // 3, j // 3)]
            ):
                return False

            rows[i].add(cell)
            columns[j].add(cell)
            squares[(i // 3, j // 3)].add(cell)

    return True
