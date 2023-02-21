"""
Problem
-------
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Solution
--------
First map each digit to a group of letters. We can generate letter combinations
by appending each letter in the group to each combination.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/LetterCombinationsOfAPhoneNumber.py

.. literalinclude:: ../solutions/LetterCombinationsOfAPhoneNumber.py
    :language: python
    :lines: 30-

Test
----
>>> from LetterCombinationsOfAPhoneNumber import letterCombinations
>>> letterCombinations('23')
['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
>>> letterCombinations('')
[]
>>> letterCombinations('2')
['a', 'b', 'c']
"""

from typing import List


def letterCombinations(digits: str) -> List[str]:
    """Generate letter combinations from a phone number.
    """
    if len(digits) == 0:
        return []

    digit2group = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    letter_groups = []
    for digit in digits:
        letter_groups.append(digit2group[digit])

    letter_combinations = ['']
    for group in letter_groups:
        letter_combinations = [combination + letter for letter in group for combination in letter_combinations]

    return letter_combinations
