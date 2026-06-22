r"""
>>> from min_stack__two_stacks import MinStack
>>> s = MinStack()
>>> s.push(-2); s.push(0); s.push(-3)
>>> s.getMin()
-3
>>> s.pop()
>>> s.top()
0
>>> s.getMin()
-2
"""

from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
