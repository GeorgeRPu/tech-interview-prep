"""
Problem
-------
https://leetcode.com/problems/generate-parentheses/

Given ``n`` pairs of parentheses, write a function to *generate all
combinations of well-formed parentheses*.

 

**Example 1:**

::

   Input: n = 3
   Output: ["((()))","(()())","(())()","()(())","()()()"]

**Example 2:**

::

   Input: n = 1
   Output: ["()"]

 

**Constraints:**

- ``1 <= n <= 8``

Solution
--------
Let's construct a well-formed parentheses string of size 3 from left to right. ::

    (, (), ()(, ()((, ()((), ()(())

Observe that

1. we can only add ')' when the number of '(' is :math:`>` to the number of ')'
2. we can keep adding '(' until we run out.

We can recursively add parenthesis according to these 2 rules until we exhaust
the limit of left and right parentheses.

Code
----

.. literalinclude:: ../solutions/medium/GenerateParentheses.py
    :language: python
    :lines: 62-

Test
----
>>> from GenerateParentheses import generateParenthesis
>>> paren = generateParenthesis(3)
>>> set(paren) == {'((()))', '(()())', '(())()', '()(())', '()()()'}
True
>>> generateParenthesis(1)
['()']
"""

from typing import List


def generateParenthesis(n: int) -> List[str]:
    """Generate all combinations of well-formed parentheses.
    """
    paren = []
    genParen(n, n, '', paren)
    return paren


def genParen(left: int, right: int, s: str, paren: List[str]):
    """Recursively add parenthesis to ``s``, finally appending ``s`` to
    ``paren``.
    """
    if left == 0 and right == 0:
        paren.append(s)
        return

    if right > left:
        genParen(left, right - 1, s + ')', paren)

    if left > 0:
        genParen(left - 1, right, s + '(', paren)
