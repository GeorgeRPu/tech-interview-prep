r"""
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
