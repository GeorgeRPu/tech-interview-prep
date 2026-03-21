"""
Problem
-------
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from ``2-9`` inclusive, return all
possible letter combinations that the number could represent. Return the
answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is
given below. Note that 1 does not map to any letters.

|image1|

 

**Example 1:**

::


   Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Example 2:**

::


   Input: digits = "2"
   Output: ["a","b","c"]

 

**Constraints:**

- ``1 <= digits.length <= 4``
- ``digits[i]`` is a digit in the range ``['2', '9']``.

.. |image1| image:: https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png

Solution
--------
First map each digit to a group of letters. We can generate letter combinations
by appending each letter in the group to each combination.

Pattern
-------
Hash Table, String, Backtracking

Code
----

.. literalinclude:: ../solutions/medium/LetterCombinationsOfAPhoneNumber.py
    :language: python
    :lines: 69-

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
