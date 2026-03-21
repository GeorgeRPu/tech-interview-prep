"""
Problem
-------
https://leetcode.com/problems/integer-to-roman/

Seven different symbols represent Roman numerals with the following
values:

====== =====
Symbol Value
====== =====
I      1
V      5
X      10
L      50
C      100
D      500
M      1000
====== =====

Roman numerals are formed by appending the conversions of decimal place
values from highest to lowest. Converting a decimal place value into a
Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the
  maximal value that can be subtracted from the input, append that
  symbol to the result, subtract its value, and convert the remainder to
  a Roman numeral.
- If the value starts with 4 or 9 use the **subtractive
  form** representing one symbol subtracted from the following symbol,
  for example, 4 is 1 (``I``) less than 5 (``V``): ``IV`` and 9 is 1
  (``I``) less than 10 (``X``): ``IX``. Only the following subtractive
  forms are used: 4 (``IV``), 9 (``IX``), 40 (``XL``), 90 (``XC``), 400
  (``CD``) and 900 (``CM``).
- Only powers of 10 (``I``, ``X``, ``C``, ``M``) can be appended
  consecutively at most 3 times to represent multiples of 10. You cannot
  append 5 (``V``), 50 (``L``), or 500 (``D``) multiple times. If you
  need to append a symbol 4 times use the **subtractive form**.

Given an integer, convert it to a Roman numeral.

 

**Example 1:**

.. container:: example-block

   **Input:** num = 3749

   **Output:** "MMMDCCXLIX"

   **Explanation:**

   ::


      3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
       700 = DCC as 500 (D) + 100 (C) + 100 (C)
        40 = XL as 10 (X) less of 50 (L)
         9 = IX as 1 (I) less of 10 (X)
      Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

**Example 2:**

.. container:: example-block

   **Input:** num = 58

   **Output:** "LVIII"

   **Explanation:**

   ::


      50 = L
       8 = VIII

**Example 3:**

.. container:: example-block

   **Input:** num = 1994

   **Output:** "MCMXCIV"

   **Explanation:**

   ::


      1000 = M
       900 = CM
        90 = XC
         4 = IV

 

**Constraints:**

- ``1 <= num <= 3999``

Solution
--------
Observe that the Roman numeral for a number is composed of the Roman numerals
for each digit. Suppose our digit is in the ones place. Then, the Roman
numberal is 'I' repeated ``digit`` times if ``digit`` is less than 4 and 'IV'
if ``digit`` is 4. For ``digit`` between 5 and 8, the Roman numeral is 'V'
followed by 'I' ``digit - 5`` times. Finally, if ``digit`` is 9, the Roman
numeral is 'IX'. For digits in the tens, hundreds, and thousands places, the
pattern holds, but with different symbols for ones, fives, and tens.

Pattern
-------
Hash Table, Math, String

Code
----

.. literalinclude:: ../solutions/medium/IntegerToRoman.py
    :language: python
    :lines: 136-

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
