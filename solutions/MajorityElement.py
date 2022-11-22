"""
Problem
-------
https://leetcode.com/problems/majority-element/

Solution
--------
Use a dictionary to count the occurrences of each element in ``nums``. We can
break early once the count of an element exceeds :math:`\\lfloor n/2 \\rfloor`.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/MajorityElement.py

Test
----
>>> from MajorityElement import majorityElement
>>> majorityElement([3, 2, 3])
3
>>> majorityElement([2, 2, 1, 1, 1, 2, 2])
2
>>> majorityElement([1])
1
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    """Returns the element that appears more than :math:`\\lfloor n/2 \\rfloor`
    times in the list.
    """
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

        if counts[n] > len(nums) // 2:
            return n
