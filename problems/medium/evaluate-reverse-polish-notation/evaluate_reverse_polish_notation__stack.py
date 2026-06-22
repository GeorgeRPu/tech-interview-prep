r"""
>>> from evaluate_reverse_polish_notation__stack import evalRPN
>>> evalRPN(["2", "1", "+", "3", "*"])
9
>>> evalRPN(["4", "13", "5", "/", "+"])
6
>>> evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
22
"""

from typing import List
from collections import deque

def exec_op(x, y, op_token):
    match op_token:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return int(float(x) / y)


def evalRPN(tokens: List[str]) -> int:
    num_stack = deque()
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            y = num_stack.pop()
            x = num_stack.pop()
            result = exec_op(x, y, token)
            num_stack.append(result)
        else:
            num_stack.append(int(token))

    return num_stack.pop()
