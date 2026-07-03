r"""
>>> from detect_squares__hash_map import DetectSquares
>>> ds = DetectSquares()
>>> ds.add([3, 10])
>>> ds.add([11, 2])
>>> ds.add([3, 2])
>>> ds.count([11, 10])
1
>>> ds.count([14, 8])
0
>>> ds.add([11, 2])
>>> ds.count([11, 10])
2
"""

from collections import defaultdict


class DetectSquares:
    """Detect axis-aligned squares from a stream of points."""

    def __init__(self) -> None:
        self.points: dict[tuple[int, int], int] = defaultdict(int)
        self.points_list: list[tuple[int, int]] = []

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.points_list.append((x, y))

    def count(self, point: list[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.points_list:
            if abs(qx - x) == abs(qy - y) and qx != x and qy != y:
                res += self.points[(qx, y)] * self.points[(x, qy)]
        return res
