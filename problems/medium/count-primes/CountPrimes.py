r"""
>>> from CountPrimes import countPrimes
>>> countPrimes(10)
4
>>> countPrimes(0)
0
>>> countPrimes(1)
0
"""


def countPrimes(n: int) -> int:
    """Count of primes less than ``n``.
    """
    if n < 3:
        return 0

    is_prime = n * [True]

    for i in range(2, n):
        if is_prime[i]:
            for j in range(2 * i, n, i):
                is_prime[j] = False

    return len([p for p in is_prime if p]) - 2
