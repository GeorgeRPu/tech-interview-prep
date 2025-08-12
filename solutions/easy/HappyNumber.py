"""
Problem
-------
https://leetcode.com/problems/happy-number/

Solution
--------
For 1000 iterations, sum the squares of each digit. If the sum is 1, return
``True``. If the sum has been seen before, return ``False``. Otherwise,
continue.

Code
----

.. literalinclude:: ../solutions/easy/HappyNumber.py
    :language: python
    :lines: 30-


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
