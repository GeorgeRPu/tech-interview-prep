"""
Problem
-------
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number ``n`` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of
  the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or
  it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return ``true`` *if* ``n`` *is a happy number, and* ``false`` *if not*.

 

**Example 1:**

::


   Input: n = 19
   Output: true
   Explanation:
   12 + 92 = 82
   82 + 22 = 68
   62 + 82 = 100
   12 + 02 + 02 = 1

**Example 2:**

::


   Input: n = 2
   Output: false

 

**Constraints:**

- ``1 <= n <= 2``\ :sup:```31```\ ``- 1``

Solution
--------
For 1000 iterations, sum the squares of each digit. If the sum is 1, return
``True``. If the sum has been seen before, return ``False``. Otherwise,
continue.

Code
----

.. literalinclude:: ../solutions/easy/HappyNumber.py
    :language: python
    :lines: 71-


Test
----
>>> from HappyNumber import isHappy
>>> isHappy(19)
True
>>> isHappy(2)
False
"""


def isHappy(n: int) -> bool:
    """Checks if a number is happy.
    """
    old_n = set()
    for i in range(1000):
        if n == 1:
            return True
        elif n in old_n:
            return False
        else:
            old_n.add(n)
            n = sum_of_square_of_digits(n)
    return True


def sum_of_square_of_digits(n):
    s = 0
    for digit in str(n):
        s += int(digit) ** 2
    return s
