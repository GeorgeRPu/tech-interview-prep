r"""
>>> from walls_and_gates__multi_source_bfs import wallsAndGates
>>> rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
>>> wallsAndGates(rooms)
>>> rooms
[[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
"""

from typing import List
from collections import deque

INF = 2147483647

def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    M = len(rooms)
    N = len(rooms[0])

    gate_locs = []
    for i in range(M):
        for j in range(N):
            if rooms[i][j] == 0:
                gate_locs.append((i, j))

    queue = deque()
    for i, j in gate_locs:
        queue.append((i - 1, j, 0))
        queue.append((i + 1, j, 0))
        queue.append((i, j - 1, 0))
        queue.append((i, j + 1, 0))

    visited = set()
    while queue:
        i, j, dist = queue.popleft()

        if not (0 <= i < M and 0 <= j < N):
            continue

        if rooms[i][j] <= 0:
            continue

        if (i, j) in visited:
            continue

        rooms[i][j] = min(dist + 1, rooms[i][j])
        visited.add((i, j))

        queue.append((i - 1, j, dist + 1))
        queue.append((i + 1, j, dist + 1))
        queue.append((i, j - 1, dist + 1))
        queue.append((i, j + 1, dist + 1))
