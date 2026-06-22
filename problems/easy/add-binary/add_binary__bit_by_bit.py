r"""
>>> from add_binary__bit_by_bit import addBinary
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
