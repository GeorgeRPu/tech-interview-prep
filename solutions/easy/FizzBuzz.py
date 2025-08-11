"""
Problem
-------
https://leetcode.com/problems/fizz-buzz/

Solution
--------
https://www.youtube.com/watch?v=QPZ0pIK_wsc

There are 4 cases to consider: divisible by 3, divisible by 5, divisible by 3
and 5, and not divisible by 3 or 5. However, observe that the third case is a
combination of the first two cases. We can use a string to build up the output
for each index 1 to :math:`n`, appending 'Fizz', then appending 'Buzz'. This saves us on an
if statement. Finally we can check if the output string is empty to determine
whether we need to print the index.

Code
----

.. literalinclude:: ../solutions/easy/FizzBuzz.py
    :language: python
    :lines: 29-

Test
----
>>> from FizzBuzz import fizzBuzz
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
