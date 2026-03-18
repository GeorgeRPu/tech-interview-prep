r"""
Problem
-------
https://leetcode.com/problems/missing-number/

Given an array ``nums`` containing ``n`` distinct numbers in the range
``[0, n]``, return *the only number in the range that is missing from
the array.*

 

**Example 1:**

.. container:: example-block

   **Input:** nums = [3,0,1]

   **Output:** 2

   **Explanation:**

   ``n = 3`` since there are 3 numbers, so all numbers are in the range
   ``[0,3]``. 2 is the missing number in the range since it does not
   appear in ``nums``.

**Example 2:**

.. container:: example-block

   **Input:** nums = [0,1]

   **Output:** 2

   **Explanation:**

   ``n = 2`` since there are 2 numbers, so all numbers are in the range
   ``[0,2]``. 2 is the missing number in the range since it does not
   appear in ``nums``.

**Example 3:**

.. container:: example-block

   **Input:** nums = [9,6,4,2,3,5,7,0,1]

   **Output:** 8

   **Explanation:**

   ``n = 9`` since there are 9 numbers, so all numbers are in the range
   ``[0,9]``. 8 is the missing number in the range since it does not
   appear in ``nums``.

.. container:: simple-translate-system-theme
   :name: simple-translate

   .. container::

      .. container:: simple-translate-button isShow

          

      .. container:: simple-translate-panel

         .. container:: simple-translate-result-wrapper

            .. container:: simple-translate-move

                

            .. container:: simple-translate-result-contents

                

                

 

**Constraints:**

- ``n == nums.length``
- ``1 <= n <= 10``\ :sup:```4```
- ``0 <= nums[i] <= n``
- All the numbers of ``nums`` are **unique**.

 

**Follow up:** Could you implement a solution using only ``O(1)`` extra
space complexity and ``O(n)`` runtime complexity?

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

.. literalinclude:: ../solutions/easy/MissingNumber.py
    :language: python
    :lines: 135-

Test
----
>>> from MissingNumber import missingNumber
>>> list1 = list(range(4))
>>> list1.remove(2)
>>> missingNumber(list1)
2
>>> list2 = list(range(100))
>>> list2.remove(47)
>>> missingNumber(list2)
47
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    """Find the single missing number in a list of integers.
    """
    n = len(nums)
    s = sum(nums)
    return n * (n + 1) // 2 - s
