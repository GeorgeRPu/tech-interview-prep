r"""
Problem
-------
https://leetcode.com/problems/count-primes/

Given an integer ``n``, return *the number of prime numbers that are
strictly less than* ``n``.

 

**Example 1:**

::


   Input: n = 10
   Output: 4
   Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

**Example 2:**

::


   Input: n = 0
   Output: 0

**Example 3:**

::


   Input: n = 1
   Output: 0

 

**Constraints:**

- ``0 <= n <= 5 * 10``\ :sup:```6```

Solution
--------
Use the Sieve of Eratosthenes. Ordinarily, we would start with a list of
integers ``primes = list(range(2, n))`` and remove multiples of ``primes[0]``
(2), then the multiples of ``primes[1]`` (3), and so on. However, this was too
slow for leetcode. Instead, we track whether each number ``i`` is prime in a
list of ``bool``s ``is_prime``. We mark the multiples of ``i`` as not prime by
setting ``is_prime[c * i] = False`` for :math:`c > 2`. The number of primes is
the number of ``True``.

Pattern
-------
Array, Math, Enumeration, Number Theory

Code
----

.. literalinclude:: ../solutions/medium/CountPrimes.py
    :language: python
    :lines: 75-

Test
----
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
