r"""
>>> from powx_n__approach_1 import myPow
>>> myPow(2.0, 10)
1024.0
>>> myPow(2.1, 3)
9.261000000000001
>>> myPow(2.0, -2)
0.25
"""


def myPow(x: float, n: int):
    """Raise :math:`x` to the power :math:`n`."""
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 0:
        return myPow(x * x, n // 2)
    elif n > 0:
        return myPow(x * x, n // 2) * x
    else:
        return 1 / myPow(x, -n)
