r"""
>>> from rotting_oranges__multi_source_bfs import orangesRotting
>>> orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
4
>>> orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
-1
>>> orangesRotting([[0,2]])
0
"""

from typing import List
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
    M = len(grid)
    N = len(grid[0])

    rotten_locs = []
    fresh_locs = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                fresh_locs.append((i, j))
            if grid[i][j] == 2:
                rotten_locs.append((i, j))

    queue = deque()
    for i, j in rotten_locs:
        queue.append((i - 1, j, 0))
        queue.append((i + 1, j, 0))
        queue.append((i, j - 1, 0))
        queue.append((i, j + 1, 0))

    visited = set()
    max_minutes = 0
    while queue:
        i, j, minutes = queue.popleft()

        if not (0 <= i < M and 0 <= j < N):
            continue

        if (i, j) in visited:
            continue

        if grid[i][j] == 0 or grid[i][j] == 2:
            continue

        grid[i][j] = 2
        max_minutes = max(max_minutes, minutes + 1)
        queue.append((i - 1, j, minutes + 1))
        queue.append((i + 1, j, minutes + 1))
        queue.append((i, j + 1, minutes + 1))
        queue.append((i, j - 1, minutes + 1))

    for i, j in fresh_locs:
        if grid[i][j] == 1:
            return -1

    return max_minutes
