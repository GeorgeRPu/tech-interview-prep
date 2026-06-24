r"""
>>> from min_cost_to_connect_all_points__prims_algorithm import minCostConnectPoints
>>> minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
20
>>> minCostConnectPoints([[3,12],[-2,5],[-4,1]])
18
"""

import heapq


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def minCostConnectPoints(points: list[list[int]]) -> int:
    points = [(x, y) for [x, y] in points]

    visited = set()
    p = points[0]
    visited.add(p)
    edges = [(dist(p, q), p, q) for q in points if p != q]
    heapq.heapify(edges)

    total_cost = 0
    while len(visited) < len(points):
        cost, p, q = heapq.heappop(edges)
        if q in visited:
            continue

        visited.add(q)

        total_cost += cost

        for r in points:
            if r not in visited:
                heapq.heappush(edges, (dist(q, r), q, r))

    return total_cost
