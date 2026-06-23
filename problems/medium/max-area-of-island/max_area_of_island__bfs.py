r"""
>>> from max_area_of_island__bfs import maxAreaOfIsland
>>> maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
6
>>> maxAreaOfIsland([[0,0,0,0,0,0,0,0]])
0
"""

from collections import deque

VISITED = -1


def maxAreaOfIsland(grid: list[list[int]]) -> int:
    M = len(grid)
    N = len(grid[0])

    def bfs(start_i, start_j):
        area = 0

        queue = deque()
        queue.append((start_i, start_j))

        while queue:
            i, j = queue.popleft()

            if not (0 <= i < M and 0 <= j < N):
                continue

            if grid[i][j] == VISITED or grid[i][j] == 0:
                continue

            if grid[i][j] == 1:
                grid[i][j] = VISITED
                area += 1

                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))

        return area

    result = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                result = max(bfs(i, j), result)

    return result
