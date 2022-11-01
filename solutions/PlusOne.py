"""
Problem
-------
https://leetcode.com/problems/plus-one

Solution
--------
Add 1 to the end of the array. Start from the least signfinicant digit and
carry any 1s to the next digit.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/PlusOne.py

Test
----
>>> from PlusOne import plusOne
>>> plusOne([4, 3, 2, 1])
[4, 3, 2, 2]
>>> plusOne([9])
[1, 0]
"""

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """Add 1 to the integer, represented in base 10, ``digits``.
    """
    n = len(digits)
    digits[-1] += 1
    for i in range(n - 1, -1, -1):
        if digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
    return digits
