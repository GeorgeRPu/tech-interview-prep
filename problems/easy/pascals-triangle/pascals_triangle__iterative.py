r"""
>>> from pascals_triangle__iterative import generate
>>> generate(3)
[[1], [1, 1], [1, 2, 1]]
>>> generate(6)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
"""


def generate(n_rows: int) -> list[list[int]]:
    """Generate Pascal's Triangle with ``n_rows``.
    """
    rows = [[1]]
    for i in range(1, n_rows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(rows[i - 1][j - 1] + rows[i - 1][j])
        rows.append(row)
    return rows
