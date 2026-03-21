"""
Problem
-------
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes ``n`` steps to reach the top.

Each time you can either climb ``1`` or ``2`` steps. In how many
distinct ways can you climb to the top?

 

**Example 1:**

::


   Input: n = 2
   Output: 2
   Explanation: There are two ways to climb to the top.
   1. 1 step + 1 step
   2. 2 steps

**Example 2:**

::


   Input: n = 3
   Output: 3
   Explanation: There are three ways to climb to the top.
   1. 1 step + 1 step + 1 step
   2. 1 step + 2 steps
   3. 2 steps + 1 step

 

**Constraints:**

- ``1 <= n <= 45``

Solution
--------
Let's start at the top and work backwards. If we are at the top, our last move
must be either a 1 or a 2 step jump. Thus ::

    climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)

Pattern
-------
Math, Dynamic Programming, Memoization

Code
----

.. literalinclude:: ../solutions/easy/ClimbingStairs.py
    :language: python
    :lines: 69-

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
