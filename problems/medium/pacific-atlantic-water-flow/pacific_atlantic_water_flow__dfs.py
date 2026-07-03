r"""
>>> from pacific_atlantic_water_flow__dfs import pacificAtlantic
>>> pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
>>> pacificAtlantic([[1]])
[[0, 0]]
"""


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    """Return cells that can reach both the Pacific and Atlantic oceans."""
    m = len(heights)
    n = len(heights[0])

    pacific: set[tuple[int, int]] = set()
    atlantic: set[tuple[int, int]] = set()

    def dfs(
        i: int, j: int, ocean: set[tuple[int, int]], prev_height: int
    ) -> None:
        if not (0 <= i < m and 0 <= j < n):
            return
        if (i, j) in ocean:
            return
        if heights[i][j] < prev_height:
            return
        ocean.add((i, j))
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dfs(i + di, j + dj, ocean, heights[i][j])

    for i in range(m):
        dfs(i, 0, pacific, 0)
        dfs(i, n - 1, atlantic, 0)

    for j in range(n):
        dfs(0, j, pacific, 0)
        dfs(m - 1, j, atlantic, 0)

    result = []
    for i in range(m):
        for j in range(n):
            if (i, j) in pacific and (i, j) in atlantic:
                result.append([i, j])

    return result
