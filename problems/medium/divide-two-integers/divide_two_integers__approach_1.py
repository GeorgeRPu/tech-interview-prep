r"""
>>> from divide_two_integers__approach_1 import divide
>>> divide(10, 3)
3
>>> divide(7, -3)
-2
"""


def divide(dividend: int, divisor: int) -> int:
    quotient = len(range(0, abs(dividend) - abs(divisor) + 1, abs(divisor)))

    if (dividend < 0) ^ (divisor < 0):
        quotient = -quotient

    return max(min(quotient, 2**31 - 1), -2**31)
