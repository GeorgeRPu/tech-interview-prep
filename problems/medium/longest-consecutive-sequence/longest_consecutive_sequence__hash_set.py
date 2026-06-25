r"""
>>> from longest_consecutive_sequence__hash_set import longestConsecutive
>>> longestConsecutive([100, 4, 200, 1, 3, 2])
4
>>> longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
9
"""


def longestConsecutive(nums: list[int]) -> int:
    """Return the length of the longest consecutive elements sequence."""
    if not nums:
        return 0

    num_set = set(nums)

    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest
