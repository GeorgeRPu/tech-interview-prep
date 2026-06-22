r"""
>>> from zigzag_conversion__row_simulation import convert
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
