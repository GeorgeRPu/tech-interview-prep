r"""
>>> from cheapest_flights_within_k_stops__modified_dijkstra import findCheapestPrice
>>> findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
700
>>> findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
200
>>> findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
500
"""

import heapq
from collections import defaultdict


def findCheapestPrice(
    n: int,
    flights: list[list[int]],
    src: int,
    dst: int,
    k: int,
) -> int:
    graph = defaultdict(list)
    for [u, v, price] in flights:
        graph[u].append((v, price))

    dist = [[float("inf")] * (k + 2) for _ in range(n)]

    min_heap = [(0, src, 0)]
    while min_heap:
        price, u, stops = heapq.heappop(min_heap)

        if dst == u:
            return price

        if stops > k or dist[u][stops] < price:
            continue

        if price > dist[u][stops]:
            continue

        for v, w in graph[u]:
            next_price = w + price
            if dist[v][stops + 1] > next_price:
                dist[v][stops + 1] = next_price
                heapq.heappush(min_heap, (next_price, v, stops + 1))

    return -1
