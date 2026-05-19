r"""
>>> from generate_parentheses__approach_1 import generateParenthesis
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
