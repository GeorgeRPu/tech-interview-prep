r"""
>>> from fizz_buzz__approach_1 import fizzBuzz
>>> fizzBuzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
"""

from typing import List


def fizzBuzz(n: int) -> List[str]:
    """Returns a list of numbers 1 to ``n``, with some numbers replaced by
    'Fizz', 'Buzz', or 'FizzBuzz' depending on their divisibility.
    """
    strings = []
    for i in range(1, n + 1):
        string = ''
        if i % 3 == 0:
            string += 'Fizz'
        if i % 5 == 0:
            string += 'Buzz'
        if len(string) == 0:
            string += str(i)
        strings.append(string)
    return strings
