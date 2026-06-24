r"""
>>> from contains_duplicate__hash_set import containsDuplicate
>>> containsDuplicate([1, 2, 3, 1])
True
>>> containsDuplicate([1, 2, 3, 4])
False
>>> containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
True
"""


def containsDuplicate(nums: list[int]) -> bool:
    """Return whether any value appears at least twice in ``nums``."""
    seen: set[int] = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
