r"""
>>> from network_delay_time__dijkstra import networkDelayTime
>>> networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
2
>>> networkDelayTime([[1,2,1]], 2, 1)
1
>>> networkDelayTime([[1,2,1]], 2, 2)
-1
"""

import heapq
from collections import defaultdict


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for [u, v, time] in times:
        graph[u].append((v, time))

    dist = {u: float("inf") for u in range(1, n + 1)}
    dist[k] = 0

    heap = [(0, k)]

    while heap:
        time, v = heapq.heappop(heap)

        for neighbor, w in graph[v]:
            next_time = time + w
            if next_time < dist[neighbor]:
                dist[neighbor] = next_time
                heapq.heappush(heap, (next_time, neighbor))

    result = max(dist.values())
    return result if result < float("inf") else -1
