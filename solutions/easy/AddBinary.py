r"""
Problem
-------
https://leetcode.com/problems/add-binary/

Solution
--------
To make the problem easier, reverse the bit strings into least significant bit
first order and pad the shorter bit string with 0s. Then, add the bits with the
carry. The next bit is the sum modulo 2 and the carry is the sum divided by 2.
At the end, if the carry is not 0, add it to the front of the string.

Code
----

.. literalinclude:: ../solutions/easy/AddBinary.py
    :language: python
    :lines: 30-

Test
----
>>> from AddBinary import addBinary
>>> addBinary('11', '1')
'100'
>>> addBinary('1010', '1011')
'10101'
"""


def addBinary(a: str, b: str) -> str:
    """Add two binary numbers ``a`` and ``b``.
    """
    s = ''
    carry = 0

    a = a[::-1]
    b = b[::-1]
    if len(a) < len(b):
        a += '0' * (len(b) - len(a))
    else:
        b += '0' * (len(a) - len(b))

    for i in range(len(a)):
        a_bit = int(a[i])
        b_bit = int(b[i])
        raw_sum = carry + a_bit + b_bit
        next_bit = raw_sum % 2
        carry = raw_sum // 2
        s = str(next_bit) + s

    return s if carry == 0 else '1' + s
