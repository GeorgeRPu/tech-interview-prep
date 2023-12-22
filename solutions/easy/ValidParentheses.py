"""
Problem
-------
https://leetcode.com/problems/valid-parentheses/

Solution
--------
This is a classic use case for stacks. For each opening parenthesis, push it
onto the stack. For each closing parenthesis, pop the stack and check if the
popped parenthesis belongs with the closing parenthesis. If it doesn't, return
False. At the end, the stack should be empty for the string to be valid.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/ValidParentheses.py

.. literalinclude:: ../solutions/easy/ValidParentheses.py
    :language: python
    :lines: 33-

Test
----
>>> from ValidParentheses import isValid
>>> isValid('()')
True
>>> isValid('()[]{}')
True
>>> isValid('(]')
False
"""


def isValid(s: str) -> bool:
    """Checks if a string of parentheses is valid.
    """
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if len(stack) == 0 or not parentheses_match(stack[-1], char):
                return False
            else:
                stack.pop()

    return len(stack) == 0


def parentheses_match(opening, closing):
    """Checks if a pair of opening and closing parentheses match.
    """
    return (opening == '(' and closing == ')') or \
        (opening == '{' and closing == '}') or \
        (opening == '[' and closing == ']')
