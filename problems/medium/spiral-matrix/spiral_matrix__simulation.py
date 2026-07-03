r"""
>>> from spiral_matrix__simulation import spiralOrder
>>> spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[1, 2, 3, 6, 9, 8, 7, 4, 5]
>>> spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """Return all elements of *matrix* in spiral order."""
    m = len(matrix)
    n = len(matrix[0])

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    i = 0
    j = 0
    d = 0

    output: list[int] = []

    left = 0
    right = n - 1
    top = 1
    bottom = m - 1

    while len(output) < m * n:
        output.append(matrix[i][j])

        hit_right = d == 0 and j == right
        hit_bottom = d == 1 and i == bottom
        hit_left = d == 2 and j == left
        hit_top = d == 3 and i == top

        if hit_right:
            d += 1
            right -= 1
        if hit_bottom:
            d += 1
            bottom -= 1
        if hit_left:
            d += 1
            left += 1
        if hit_top:
            d = (d + 1) % 4
            top += 1

        i += directions[d][0]
        j += directions[d][1]

    return output
