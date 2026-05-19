r"""
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
