r"""
>>> from string_to_integer_atoi__linear_scan import myAtoi
>>> myAtoi('42')
42
>>> myAtoi('   -42')
-42
>>> myAtoi('4193 with words')
4193
"""


def myAtoi(s: str) -> int:
    """Convert string to integer."""
    sign = 1
    value = 0

    s = s.strip()

    if len(s) == 0:
        return 0

    sign_char = s[0]
    num_start = 0
    if sign_char in {"-", "+"}:
        num_start = 1
    if sign_char == "-":
        sign = -1

    num_string = ""
    for char in s[num_start:]:
        if not char.isnumeric():
            break

        num_string += char

    for i, char in enumerate(reversed(num_string)):
        value += int(char) * 10**i
        if sign == 1 and value >= 2**31 - 1:
            return 2**31 - 1
        elif sign == -1 and value >= 2**31:
            return -(2**31)

    return sign * value
