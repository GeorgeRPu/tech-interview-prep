"""
Problem
-------
https://leetcode.com/problems/count-and-say/

Solution
--------
If ``n == 1``, return ``'1'``. Otherwise, get the previous count-and-say
string. Iterate through the digits of the previous string. If the current digit
is the same as the previous digit, increment ``count`` by 1. Otherwise, append
``f'{count}{previous_digit}'`` to the count-and-say string and reset ``count``
to 1.

Code
----

.. literalinclude:: ../solutions/medium/CountAndSay.py
    :language: python
    :lines: 31-

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
