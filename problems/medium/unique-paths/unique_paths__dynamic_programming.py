r"""
>>> from unique_paths__dynamic_programming import uniquePaths
>>> uniquePaths(3, 7)
28
>>> uniquePaths(3, 2)
3
"""


def uniquePaths(m: int, n: int) -> int:
    paths = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                paths[0][0] = 1
            elif i == 0:
                paths[i][j] = paths[i][j - 1]
            elif j == 0:
                paths[i][j] = paths[i - 1][j]
            else:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

    return paths[-1][-1]
