"""
Problem
-------
https://leetcode.com/problems/container-with-most-water/

You are given an integer array ``height`` of length ``n``. There are
``n`` vertical lines drawn such that the two endpoints of the
``i``\ :sup:```th``` line are ``(i, 0)`` and ``(i, height[i])``.

Find two lines that together with the x-axis form a container, such that
the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

 

**Example 1:**

|image1|

::


   Input: height = [1,8,6,2,5,4,8,3,7]
   Output: 49
   Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

::


   Input: height = [1,1]
   Output: 1

 

**Constraints:**

- ``n == height.length``
- ``2 <= n <= 10``\ :sup:```5```
- ``0 <= height[i] <= 10``\ :sup:```4```

.. |image1| image:: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

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
    :lines: 71-

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
