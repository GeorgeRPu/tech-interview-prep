r"""
>>> from plus_one__right_to_left_carry import plusOne
>>> plusOne([4, 3, 2, 1])
[4, 3, 2, 2]
>>> plusOne([9])
[1, 0]
"""


def plusOne(digits: list[int]) -> list[int]:
    """Add 1 to the integer, represented in base 10, ``digits``.
    """
    n = len(digits)
    digits[-1] += 1
    for i in range(n - 1, -1, -1):
        if digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
    return digits
