r"""
>>> from surrounded_regions__dfs import solve
>>> board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
>>> solve(board)
>>> board
[['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
>>> board = [["X"]]
>>> solve(board)
>>> board
[['X']]
"""


def solve(board: list[list[str]]) -> None:
    """Capture surrounded regions in-place."""
    m = len(board)
    n = len(board[0])

    def dfs(i: int, j: int) -> None:
        if not (0 <= i < m and 0 <= j < n):
            return
        if board[i][j] != "O":
            return
        board[i][j] = "S"
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)

    for j in range(n):
        dfs(0, j)
        dfs(m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            if board[i][j] == "S":
                board[i][j] = "O"
