"""
Problem
-------
https://leetcode.com/problems/integer-to-roman/

Solution
--------
Observe that the Roman numeral for a number is composed of the Roman numerals
for each digit. Suppose our digit is in the ones place. Then, the Roman
numberal is 'I' repeated ``digit`` times if ``digit`` is less than 4 and 'IV'
if ``digit`` is 4. For ``digit`` between 5 and 8, the Roman numeral is 'V'
followed by 'I' ``digit - 5`` times. Finally, if ``digit`` is 9, the Roman
numeral is 'IX'. For digits in the tens, hundreds, and thousands places, the
pattern holds, but with different symbols for ones, fives, and tens.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/IntegerToRoman.py

.. literalinclude:: ../solutions/IntegerToRoman.py
    :language: python
    :lines: 36-

Test
----
>>> from IntegerToRoman import intToRoman
>>> intToRoman(3)
'III'
>>> intToRoman(58)
'LVIII'
>>> intToRoman(1994)
'MCMXCIV'
"""


def intToRoman(num: int) -> str:
    """Convert an integer between 0 and 3999 to a Roman numeral.
    """
    thousands_digit = (num % 10000) // 1000
    hundreds_digit = (num % 1000) // 100
    tens_digit = (num % 100) // 10
    ones_digit = num % 10

    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '?', '!']

    thousands_roman = roman_subnumeral(thousands_digit, *symbols[6:9])
    hundreds_roman = roman_subnumeral(hundreds_digit, *symbols[4:7])
    tens_roman = roman_subnumeral(tens_digit, *symbols[2:5])
    ones_roman = roman_subnumeral(ones_digit, *symbols[:3])

    return thousands_roman + hundreds_roman + tens_roman + ones_roman


def roman_subnumeral(digit, symbol, five_symbol, ten_symbol):
    """Generate the Roman sub-numberal for a single digit.
    """
    if digit < 4:
        return digit * symbol
    elif digit == 4:
        return symbol + five_symbol
    elif 5 <= digit < 9:
        return five_symbol + (digit - 5) * symbol
    elif digit == 9:
        return symbol + ten_symbol
