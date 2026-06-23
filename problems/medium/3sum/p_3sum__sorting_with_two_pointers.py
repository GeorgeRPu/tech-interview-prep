r"""
>>> from p_3sum__sorting_with_two_pointers import threeSum
>>> threeSum([-1, 0, 1, 2, -1, -4])
[[-1, 0, 1], [-1, -1, 2]]
>>> threeSum([0, 1, 1])
[]
>>> threeSum([0, 0, 0])
[[0, 0, 0]]
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    """Returns a list of triplets in ``nums`` with distinct indices that sum to
    0.
    """
    solutions = set()
    nums = sorted(nums)
    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                solutions.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
    return [list(solution) for solution in solutions]
