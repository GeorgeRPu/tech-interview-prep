r"""
Problem
-------
https://leetcode.com/problems/single-number-ii/

Given an integer array ``nums`` where every element appears **three
times** except for one, which appears **exactly once**. *Find the single
element and return it*.

You must implement a solution with a linear runtime complexity and
use only constant extra space.

 

**Example 1:**

::

   Input: nums = [2,2,3,2]
   Output: 3

**Example 2:**

::

   Input: nums = [0,1,0,1,0,1,99]
   Output: 99

 

**Constraints:**

- ``1 <= nums.length <= 3 * 10``\ :sup:```4```
- ``-2``\ :sup:```31```\ ``<= nums[i] <= 2``\ :sup:```31```\ ``- 1``
- Each element in ``nums`` appears exactly **three times** except for
  one element which appears **once**.

Solution
--------
For each bit position, we sum the bits in that position across ``nums``. For
the integers in ``nums`` that appear 3 times, the number of 1s in each position
will be a multiple of 3. For each position, we can extract the bit value of
the integer :math:`x` that appears once by modding the sum by 3. If :math:`x`
is negative, then the bit values will be in 2's complement form. We can convert
unsigned integers to 2's complement by subtracting :math:`2^{32}`.

Pattern
-------
Array, Bit Manipulation

Code
----

.. literalinclude:: ../solutions/medium/SingleNumberII.py
    :language: python
    :lines: 67-

Test
----
>>> from SingleNumberII import singleNumber
>>> singleNumber([2, 2, 3, 2])
3
>>> singleNumber([0, 1, 0, 1, 0, 1, 99])
99
"""

from typing import List


def singleNumber(nums: List[int]) -> int:
    """Finds the integer that appears once in ``nums`` where all other integers
    appear 3 times.
    """
    bits = 32 * [0]
    for num in nums:
        for i in range(32):
            bits[i] += getBit(num, i)

    bits = [bit % 3 for bit in bits]

    ans = 0
    for i in range(32):
        ans += bits[i] << i

    return ans if ans < 2**31 else ans - 2**32


def getBit(num, i):
    """Gets the ``i``-th bit of ``num``.
    """
    return (num >> i) & 1
