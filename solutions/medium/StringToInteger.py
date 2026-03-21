"""
Problem
-------
https://leetcode.com/problems/string-to-integer-atoi/

Implement the ``myAtoi(string s)`` function, which converts a string to
a 32-bit signed integer.

The algorithm for ``myAtoi(string s)`` is as follows:

#. **Whitespace**: Ignore any leading whitespace (``" "``).
#. **Signedness**: Determine the sign by checking if the next character
   is ``'-'`` or ``'+'``, assuming positivity if neither present.
#. **Conversion**: Read the integer by skipping leading zeros until a
   non-digit character is encountered or the end of the string is
   reached. If no digits were read, then the result is 0.
#. **Rounding**: If the integer is out of the 32-bit signed integer
   range ``[-2``\ :sup:```31```\ ``, 2``\ :sup:```31```\ ``- 1]``, then
   round the integer to remain in the range. Specifically, integers less
   than ``-2``\ :sup:```31``` should be rounded to
   ``-2``\ :sup:```31```, and integers greater than
   ``2``\ :sup:```31```\ ``- 1`` should be rounded to
   ``2``\ :sup:```31```\ ``- 1``.

Return the integer as the final result.

 

**Example 1:**

.. container:: example-block

   **Input:** s = "42"

   **Output:** 42

   **Explanation:**

   ::


      The underlined characters are what is read in and the caret is the current reader position.
      Step 1: "42" (no characters read because there is no leading whitespace)
               ^
      Step 2: "42" (no characters read because there is neither a '-' nor '+')
               ^
      Step 3: "42" ("42" is read in)
                 ^

**Example 2:**

.. container:: example-block

   **Input:** s = " -042"

   **Output:** -42

   **Explanation:**

   ::


      Step 1: "   -042" (leading whitespace is read and ignored)
                  ^
      Step 2: "   -042" ('-' is read, so the result should be negative)
                   ^
      Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
                     ^

**Example 3:**

.. container:: example-block

   **Input:** s = "1337c0d3"

   **Output:** 1337

   **Explanation:**

   ::


      Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
               ^
      Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
               ^
      Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
                   ^

**Example 4:**

.. container:: example-block

   **Input:** s = "0-1"

   **Output:** 0

   **Explanation:**

   ::


      Step 1: "0-1" (no characters read because there is no leading whitespace)
               ^
      Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
               ^
      Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
                ^

**Example 5:**

.. container:: example-block

   **Input:** s = "words and 987"

   **Output:** 0

   **Explanation:**

   Reading stops at the first non-digit character 'w'.

 

**Constraints:**

- ``0 <= s.length <= 200``
- ``s`` consists of English letters (lower-case and upper-case), digits
  (``0-9``), ``' '``, ``'+'``, ``'-'``, and ``'.'``.

Solution
--------
Track the value of the integer as in separate ``sign`` and ``value`` variables.

1. Use ``s.strip()`` to remove any whitespace.
2. Check if the string is empty. If so, return 0.
3. Check the first character of the string. If it is '+' or '-', the number portion of the string starts at 1. Set the ``sign`` based on the character or default to a positive sign.
4. Get all the numeric digits in the string.
5. From the end, increase ``value`` by :math:`\\textrm{digit}_i * 10^i`. If ``value`` exceeds the int32 limits of :math:`[-2^{32}, 2^{32} - 1]`, clamp ``value``.

Pattern
-------
String

Code
----

.. literalinclude:: ../solutions/medium/StringToInteger.py
    :language: python
    :lines: 163-

Test
----
>>> from StringToInteger import myAtoi
>>> myAtoi('42')
42
>>> myAtoi('   -42')
-42
>>> myAtoi('4193 with words')
4193
"""


def myAtoi(s: str) -> int:
    """Convert string to integer.
    """
    sign = 1
    value = 0

    s = s.strip()

    if len(s) == 0:
        return 0

    sign_char = s[0]
    num_start = 0
    if sign_char in {'-', '+'}:
        num_start = 1
    if sign_char == '-':
        sign = -1

    num_string = ''
    for char in s[num_start:]:
        if not char.isnumeric():
            break

        num_string += char

    for i, char in enumerate(reversed(num_string)):
        value += int(char) * 10**i
        if sign == 1 and value >= 2**31 - 1:
            return 2**31 - 1
        elif sign == -1 and value >= 2**31:
            return -2**31

    return sign * value
