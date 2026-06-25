r"""
>>> from find_the_duplicate_number__cycle_detection import findDuplicate
>>> findDuplicate([1, 3, 4, 2, 2])
2
>>> findDuplicate([3, 1, 3, 4, 2])
3
>>> findDuplicate([3, 3, 3, 3, 3])
3
"""


def findDuplicate(nums: list[int]) -> int:
    """Find the duplicate number using Floyd's cycle detection."""
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while slow2 != slow:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow2
