"""
Problem
-------
https://leetcode.com/problems/climbing-stairs/

Solution
--------
Let's start at the top and work backwards. If we are at the top, our last move
must be either a 1 or a 2 step jump. Thus ::

    climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)

Test
----
>>> from ClimbingStairs import climbStairs
>>> climbStairs(2)
2
>>> climbStairs(3)
3
"""


def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)
