r"""
Problem
-------
https://leetcode.com/problems/missing-number/

Solution
--------

Let :math:`m \in \{1, ..., n\}` be the missing number. Since ``nums``
:math:`= \{1, ..., n\} - \{m\}`,

.. math::

    \begin{align}
    \DeclareMathOperator{\sumof}{sumof}
    \sumof(nums) &= \left( \sum_{i=1}^{n} i \right) - m \\
    m &= \sum_{i=1}^{n} i - \sumof(nums)
    \end{align}

Use the formula

.. math::

    \sum_{i=1}^{n} i = \frac{n(n+1)}{2}

to calculate the the sum
from 1 to :math:`n` quickly. Note that :math:`n` is one more than the number of
elements in ``nums``.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/MissingNumber.py

.. literalinclude:: ../solutions/MissingNumber.py
    :language: python
    :lines: 51-

Test
----
>>> from MissingNumber import missing_number
>>> list1 = list(range(4))
>>> list1.remove(2)
>>> missing_number(list1)
2
>>> list2 = list(range(100))
>>> list2.remove(47)
>>> missing_number(list2)
47
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    """Find the single missing number in a list of integers.
    """
    n = len(nums)
    s = sum(nums)
    return n * (n + 1) // 2 - s
