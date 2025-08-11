"""
Problem
-------
https://leetcode.com/problems/climbing-stairs/

Solution
--------
Let's start at the top and work backwards. If we are at the top, our last move
must be either a 1 or a 2 step jump. Thus ::

    climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)

Code
----

.. literalinclude:: ../solutions/easy/ClimbingStairs.py
    :language: python
    :lines: 27-

Test
----
>>> from ClimbingStairs import climbStairs
>>> climbStairs(2)
2
>>> climbStairs(3)
3
"""

climb_stairs = {}


def climbStairs(n: int) -> int:
    """Return the number of ways to climb ``n`` steps of stairs taking only
    jumps of 1 and 2, using memoization to speed up the calculation.
    """
    if n > 2:
        if n - 1 not in climb_stairs:
            climb_stairs[n - 1] = climbStairs(n - 1)
        x = climb_stairs[n - 1]
        if n - 2 not in climb_stairs:
            climb_stairs[n - 2] = climbStairs(n - 2)
        y = climb_stairs[n - 2]
        return x + y
    elif n == 2:
        return 2
    else:
        return 1
