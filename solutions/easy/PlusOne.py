r"""
Problem
-------
https://leetcode.com/problems/plus-one

You are given a **large integer** represented as an integer array
``digits``, where each ``digits[i]`` is the ``i``\ :sup:```th``` digit
of the integer. The digits are ordered from most significant to least
significant in left-to-right order. The large integer does not contain
any leading ``0``'s.

Increment the large integer by one and return *the resulting array of
digits*.

 

**Example 1:**

::


   Input: digits = [1,2,3]
   Output: [1,2,4]
   Explanation: The array represents the integer 123.
   Incrementing by one gives 123 + 1 = 124.
   Thus, the result should be [1,2,4].

**Example 2:**

::


   Input: digits = [4,3,2,1]
   Output: [4,3,2,2]
   Explanation: The array represents the integer 4321.
   Incrementing by one gives 4321 + 1 = 4322.
   Thus, the result should be [4,3,2,2].

**Example 3:**

::


   Input: digits = [9]
   Output: [1,0]
   Explanation: The array represents the integer 9.
   Incrementing by one gives 9 + 1 = 10.
   Thus, the result should be [1,0].

 

**Constraints:**

- ``1 <= digits.length <= 100``
- ``0 <= digits[i] <= 9``
- ``digits`` does not contain any leading ``0``'s.

Solution
--------
Add 1 to the end of the array. Start from the least signfinicant digit and
carry any 1s to the next digit.

Pattern
-------
Array, Math

Code
----

.. literalinclude:: ../solutions/easy/PlusOne.py
    :language: python
    :lines: 83-

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
