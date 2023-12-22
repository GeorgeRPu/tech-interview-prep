"""
Problem
-------
https://leetcode.com/problems/string-to-integer-atoi/

Solution
--------
Track the value of the integer as in separate ``sign`` and ``value`` variables.

1. Use ``s.strip()`` to remove any whitespace.
2. Check if the string is empty. If so, return 0.
3. Check the first character of the string. If it is '+' or '-', the number portion of the string starts at 1. Set the ``sign`` based on the character or default to a positive sign.
4. Get all the numeric digits in the string.
5. From the end, increase ``value`` by :math:`\\textrm{digit}_i * 10^i`. If ``value`` exceeds the int32 limits of :math:`[-2^{32}, 2^{32} - 1]`, clamp ``value``.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/StringToInteger.py

.. literalinclude:: ../solutions/medium/StringToInteger.py
    :language: python
    :lines: 39-

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
