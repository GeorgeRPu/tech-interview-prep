r"""
>>> from trapping_rain_water__two_pointers import trap
>>> trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
6
>>> trap([4, 2, 0, 3, 2, 5])
9
"""


def trap(height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    left_max = height[left]
    right_max = height[right]

    trapped = 0
    while left < right:
        if height[left] <= height[right]:
            left += 1
            left_max = max(left_max, height[left])
            trapped += left_max - height[left]

        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped += right_max - height[right]

    return trapped
