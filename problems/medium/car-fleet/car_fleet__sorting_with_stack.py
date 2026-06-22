r"""
>>> from car_fleet__sorting_with_stack import carFleet
>>> carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
3
>>> carFleet(10, [3], [3])
1
>>> carFleet(100, [0, 2, 4], [4, 2, 1])
1
"""

from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = list(zip(position, speed))
    cars = sorted(cars, key=lambda tup: tup[0], reverse=True)

    stack = []
    for p, v in cars:
        time = (target - p) / v

        if len(stack) == 0:
            stack.append(time)
        elif stack[-1] >= time:
            pass
        else:
            stack.append(time)

    return len(stack)
