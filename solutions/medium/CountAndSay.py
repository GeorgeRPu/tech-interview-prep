"""
Problem
-------
https://leetcode.com/problems/count-and-say/

The **count-and-say** sequence is a sequence of digit strings defined by
the recursive formula:

- ``countAndSay(1) = "1"``
- ``countAndSay(n)`` is the run-length encoding of
  ``countAndSay(n - 1)``.

`Run-length
encoding <http://en.wikipedia.org/wiki/Run-length_encoding>`__ (RLE) is
a string compression method that works by replacing consecutive
identical characters (repeated 2 or more times) with the concatenation
of the character and the number marking the count of the characters
(length of the run). For example, to compress the string ``"3322251"``
we replace ``"33"`` with ``"23"``, replace ``"222"`` with ``"32"``,
replace ``"5"`` with ``"15"`` and replace ``"1"`` with ``"11"``. Thus
the compressed string becomes ``"23321511"``.

Given a positive integer ``n``, return *the* ``n``\ :sup:```th```
*element of the* **count-and-say** *sequence*.

 

**Example 1:**

.. container:: example-block

   **Input:** n = 4

   **Output:** "1211"

   **Explanation:**

   ::


      countAndSay(1) = "1"
      countAndSay(2) = RLE of "1" = "11"
      countAndSay(3) = RLE of "11" = "21"
      countAndSay(4) = RLE of "21" = "1211"

**Example 2:**

.. container:: example-block

   **Input:** n = 1

   **Output:** "1"

   **Explanation:**

   This is the base case.

 

**Constraints:**

- ``1 <= n <= 30``

 

**Follow up:** Could you solve it iteratively?

Solution
--------
If ``n == 1``, return ``'1'``. Otherwise, get the previous count-and-say
string. Iterate through the digits of the previous string. If the current digit
is the same as the previous digit, increment ``count`` by 1. Otherwise, append
``f'{count}{previous_digit}'`` to the count-and-say string and reset ``count``
to 1.

Pattern
-------
String

Code
----

.. literalinclude:: ../solutions/medium/CountAndSay.py
    :language: python
    :lines: 97-

Test
----
>>> from CountAndSay import countAndSay
>>> countAndSay(1)
'1'
>>> countAndSay(4)
'1211'
"""


def countAndSay(n: int) -> str:
    """Return the ``n``-th count-and-say string.
    """
    if n == 1:
        return '1'

    count_and_say = ''
    digits = countAndSay(n - 1)
    previous_digit = digits[0]
    count = 0
    for digit in digits:
        if digit == previous_digit:
            count += 1
        else:
            count_and_say += f'{count}{previous_digit}'

            previous_digit = digit
            count = 1

    count_and_say += f'{count}{previous_digit}'

    return count_and_say
