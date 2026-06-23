r"""
>>> from number_of_islands__bfs import numIslands
>>> numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
1
>>> numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
3
"""

from collections import deque

VISITED = "*"


def numIslands(grid: list[list[str]]) -> int:
    M = len(grid)
    N = len(grid[0])

    def bfs(start_i, start_j):
        queue = deque()

        queue.append((start_i, start_j))
        while queue:
            i, j = queue.popleft()

            if not (0 <= i < M and 0 <= j < N):
                continue

            if grid[i][j] == VISITED or grid[i][j] == "0":
                continue

            if grid[i][j] == "1":
                grid[i][j] = VISITED
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))

    result = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "1":
                result += 1
                bfs(i, j)

    return result
