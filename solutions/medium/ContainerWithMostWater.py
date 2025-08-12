"""
Problem
-------
https://leetcode.com/problems/container-with-most-water/

Solution
--------
Since the area of a container is the product of its width and height, set the
``left`` and ``right`` pointer to ends. Compute the area and store it as the
``max_area``. Then, move the pointer with the smaller height inwards. If the
heights are equal, move the pointer whose inward height is larger.

Code
----

.. literalinclude:: ../solutions/medium/ContainerWithMostWater.py
    :language: python
    :lines: 29-

Test
----
>>> from ContainerWithMostWater import maxArea
>>> maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
49
>>> maxArea([1, 1])
1
"""

from typing import List


def maxArea(height: List[int]) -> int:
    """Finds the maximum area of a container that can hold water when given a
    list of heights ``height`` at positions 0 to ``len(height) - 1``.
    """

    left = 0
    right = len(height) - 1

    max_area = 0

    while left < right:
        w = right - left
        h = min(height[left], height[right])

        area = w * h
        if area > max_area:
            max_area = area

        if height[left] < height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1
        elif height[left + 1] < height[right - 1]:
            right -= 1
        else:
            left += 1

    return max_area
