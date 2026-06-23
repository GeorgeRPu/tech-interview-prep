r"""
>>> from maximum_product_subarray__dynamic_programming import maxProduct
>>> maxProduct([2, 3, -2, 4])
6
>>> maxProduct([-2, 0, -1])
0
"""


def maxProduct(nums: list[int]) -> int:
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for num in nums[1:]:
        candidates = [num, max_product * num, min_product * num]
        max_product = max(candidates)
        min_product = min(candidates)
        result = max(result, max_product)

    return result
