r"""
>>> from daily_temperatures__monotonic_stack import dailyTemperatures
>>> dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
[1, 1, 4, 2, 1, 1, 0, 0]
>>> dailyTemperatures([30, 40, 50, 60])
[1, 1, 1, 0]
>>> dailyTemperatures([30, 60, 90])
[1, 1, 0]
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []

    output = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):

        while len(stack) > 0 and temperatures[stack[-1]] < temp:
            j = stack.pop()
            output[j] = i - j

        stack.append(i)

    return output
