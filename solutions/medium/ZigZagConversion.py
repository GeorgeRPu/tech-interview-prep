"""
Problem
-------
https://leetcode.com/problems/zigzag-conversion/

Solution
--------
Create a 2d array ``rows`` that is ``numRows`` rows by ``len(s)`` columns. The
zigzag pattern has 2 parts. The zig is a vertical line and the zag is diagonal.
Track whether we should be zigging or zagging with a boolean. When we reach the
top or bottom of ``rows``, switch from zig to zag or zag to zig. Iterate
through the string, setting a cell in rows to the current character. Join
``rows`` together row-wise to get the converted string.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/ZigZagConversion.py

.. literalinclude:: ../solutions/medium/ZigZagConversion.py
    :language: python
    :lines: 35-

Test
----
>>> from ZigZagConversion import convert
>>> convert('PAYPALISHIRING', 3)
'PAHNAPLSIIGYIR'
>>> convert('PAYPALISHIRING', 4)
'PINALSIGYAHRPI'
>>> convert('A', 1)
'A'
"""


def convert(s: str, numRows: int) -> str:
    """Convert a string ``s`` to a zigzag pattern with ``numRows`` rows.
    """
    rows = [len(s) * [''] for i in range(numRows)]
    i = 0
    j = 0

    for char in s:
        rows[i][j] = char

        if i == 0:
            zig = True
        if i == numRows - 1:
            zig = False

        if zig:
            i += 1
        else:
            i -= 1
            j += 1

        i %= numRows

    joined_rows = [''.join(row) for row in rows]
    return ''.join(joined_rows)
