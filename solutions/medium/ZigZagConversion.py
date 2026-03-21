"""
Problem
-------
https://leetcode.com/problems/zigzag-conversion/

The string ``"PAYPALISHIRING"`` is written in a zigzag pattern on a
given number of rows like this: (you may want to display this pattern in
a fixed font for better legibility)

::


   P   A   H   N
   A P L S I I G
   Y   I   R

And then read line by line: ``"PAHNAPLSIIGYIR"``

Write the code that will take a string and make this conversion given a
number of rows:

::


   string convert(string s, int numRows);

 

**Example 1:**

::


   Input: s = "PAYPALISHIRING", numRows = 3
   Output: "PAHNAPLSIIGYIR"

**Example 2:**

::


   Input: s = "PAYPALISHIRING", numRows = 4
   Output: "PINALSIGYAHRPI"
   Explanation:
   P     I    N
   A   L S  I G
   Y A   H R
   P     I

**Example 3:**

::


   Input: s = "A", numRows = 1
   Output: "A"

 

**Constraints:**

- ``1 <= s.length <= 1000``
- ``s`` consists of English letters (lower-case and upper-case), ``','``
  and ``'.'``.
- ``1 <= numRows <= 1000``

Solution
--------
Create a 2d array ``rows`` that is ``numRows`` rows by ``len(s)`` columns. The
zigzag pattern has 2 parts. The zig is a vertical line and the zag is diagonal.
Track whether we should be zigging or zagging with a boolean. When we reach the
top or bottom of ``rows``, switch from zig to zag or zag to zig. Iterate
through the string, setting a cell in rows to the current character. Join
``rows`` together row-wise to get the converted string.

Pattern
-------
String

Code
----

.. literalinclude:: ../solutions/medium/ZigZagConversion.py
    :language: python
    :lines: 99-

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
