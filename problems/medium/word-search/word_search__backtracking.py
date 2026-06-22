r"""
>>> from word_search__backtracking import exist
>>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
True
>>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
True
>>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
False
"""

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    M = len(board)
    N = len(board[0])

    def backtrack(w, path, i, j):

        if (i, j) in path or not (0 <= i < M and 0 <= j < N):
            return False

        path.add((i, j))

        if board[i][j] != word[w - 1]:
            return False

        if w == len(word):
            return True

        return any([
            backtrack(w + 1, path.copy(), i - 1, j),
            backtrack(w + 1, path.copy(), i + 1, j),
            backtrack(w + 1, path.copy(), i, j - 1),
            backtrack(w + 1, path.copy(), i, j + 1)
        ])

    for i in range(M):
        for j in range(N):
            if board[i][j] == word[0] and backtrack(1, set(), i, j):
                return True

    return False
