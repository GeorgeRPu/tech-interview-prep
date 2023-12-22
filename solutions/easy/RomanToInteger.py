"""
Problem
-------
https://leetcode.com/problems/roman-to-integer/

Solution
--------
Observe that the value of a Roman numeral is the sum of the value of the
letters, but the letters may be negative or positive depending on their
position. Since there are only 6 instances of subtractive notation, we can
store these in a set. If these are present, we subtract the value of the
numeral. Otherwise add up the numeral values.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/RomanToInteger.py

.. literalinclude:: ../solutions/easy/RomanToInteger.py
    :language: python
    :lines: 34-

Test
----
>>> from RomanToInteger import roman_to_int
>>> roman_to_int('III')
3
>>> roman_to_int('LVIII')
58
>>> roman_to_int('MCMXCIV')
1994
"""


def roman_to_int(s: str):
    """Convert Roman numeral ``s`` to integer.
    """
    additions = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    subtractions = {
        'IV',
        'IX',
        'XL',
        'XC',
        'CD',
        'CM'
    }

    value = 0
    for i, numeral in enumerate(s):
        if s[i:i + 2] in subtractions:
            value -= additions[numeral]
        else:
            value += additions[numeral]

    return value
