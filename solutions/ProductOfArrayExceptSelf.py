"""
Problem
-------
https://leetcode.com/problems/product-of-array-except-self/

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

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/ProductOfArrayExceptSelf.py

.. literalinclude:: ../solutions/ProductOfArrayExceptSelf.py
    :language: python
    :lines: 35-

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
