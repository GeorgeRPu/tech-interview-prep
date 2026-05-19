r"""
>>> from sqrtx__approach_1 import mySqrt
>>> mySqrt(4)
2
>>> mySqrt(8)
2
"""


def mySqrt(x: int) -> int:
    """Finds the largest integer :math:`y` such that :math:`y^2 \\leq x`.
    """
    start = 0
    end = 65536
    while start + 1 < end:
        mid = (start + end) // 2
        if mid**2 > x:
            end = mid
        else:
            start = mid

    return start
