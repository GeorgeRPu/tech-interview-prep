"""
Problem
-------
https://leetcode.com/problems/valid-parentheses/

Given a string ``s`` containing just the characters ``'('``, ``')'``,
``'{'``, ``'}'``, ``'['`` and ``']'``, determine if the input string is
valid.

An input string is valid if:

#. Open brackets must be closed by the same type of brackets.
#. Open brackets must be closed in the correct order.
#. Every close bracket has a corresponding open bracket of the same
   type.

 

**Example 1:**

.. container:: example-block

   **Input:** s = "()"

   **Output:** true

**Example 2:**

.. container:: example-block

   **Input:** s = "()[]{}"

   **Output:** true

**Example 3:**

.. container:: example-block

   **Input:** s = "(]"

   **Output:** false

**Example 4:**

.. container:: example-block

   **Input:** s = "([])"

   **Output:** true

**Example 5:**

.. container:: example-block

   **Input:** s = "([)]"

   **Output:** false

 

**Constraints:**

- ``1 <= s.length <= 10``\ :sup:```4```
- ``s`` consists of parentheses only ``'()[]{}'``.

Solution
--------
This is a classic use case for stacks. For each opening parenthesis, push it
onto the stack. For each closing parenthesis, pop the stack and check if the
popped parenthesis belongs with the closing parenthesis. If it doesn't, return
False. At the end, the stack should be empty for the string to be valid.

Code
----

.. literalinclude:: ../solutions/easy/ValidParentheses.py
    :language: python
    :lines: 92-

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
