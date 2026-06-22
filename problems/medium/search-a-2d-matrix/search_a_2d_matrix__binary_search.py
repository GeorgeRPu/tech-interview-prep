r"""
>>> from search_a_2d_matrix__binary_search import searchMatrix
>>> searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
True
>>> searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
False
"""

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2

        rows = mid // n
        cols = mid % n

        if matrix[rows][cols] == target:
            return True
        elif matrix[rows][cols] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
