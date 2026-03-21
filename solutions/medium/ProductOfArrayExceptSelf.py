"""
Problem
-------
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array ``nums``, return *an array* ``answer`` *such
that* ``answer[i]`` *is equal to the product of all the elements of*
``nums`` *except* ``nums[i]``.

The product of any prefix or suffix of ``nums`` is **guaranteed** to fit
in a **32-bit** integer.

You must write an algorithm that runs in ``O(n)`` time and without using
the division operation.

 

**Example 1:**

::

   Input: nums = [1,2,3,4]
   Output: [24,12,8,6]

**Example 2:**

::

   Input: nums = [-1,1,0,-3,3]
   Output: [0,0,9,0,0]

 

**Constraints:**

- ``2 <= nums.length <= 10``\ :sup:```5```
- ``-30 <= nums[i] <= 30``
- The input is generated such that ``answer[i]`` is **guaranteed** to
  fit in a **32-bit** integer.

 

**Follow up:** Can you solve the problem in ``O(1)`` extra space
complexity? (The output array **does not** count as extra space for
space complexity analysis.)

Solution
--------
Observe that the product of all elements except the element at index i is the
product of all elements ``nums[:i - 1]`` multiplied by the product of all
elements ``nums[i + 1:]``. Iterate through ``nums`` once to compute the product
of all elements ``nums[:i - 1]`` and store the result in a list ``products``.
Start with ``left_product = 1`` and append it to ``products`` before
multiplying with the next element in ``nums``. Iterate through ``nums`` in
reverse to compute the product of all elements ``nums[i + 1:]`` and multiply
the result by the corresponding element in ``products`` to obtains the product
of all elements except the element at index :math:`i`.

Pattern
-------
Array, Prefix Sum

Code
----

.. literalinclude:: ../solutions/medium/ProductOfArrayExceptSelf.py
    :language: python
    :lines: 79-

Test
----
>>> from ProductOfArrayExceptSelf import productExceptSelf
>>> productExceptSelf([1, 2, 3, 4])
[24, 12, 8, 6]
>>> productExceptSelf([-1, 1, 0, -3, 3])
[0, 0, 9, 0, 0]
"""

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """Product of all elements except the element at index ``i`` for each index
    ``i`` in ``nums``.
    """
    products = []

    left_product = 1
    for num in nums:
        products.append(left_product)
        left_product *= num

    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= right_product
        right_product *= nums[i]

    return products
