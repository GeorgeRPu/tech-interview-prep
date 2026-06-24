r"""
>>> from roman_to_integer__lookup_table import roman_to_int
>>> roman_to_int('III')
3
>>> roman_to_int('LVIII')
58
>>> roman_to_int('MCMXCIV')
1994
"""


def roman_to_int(s: str):
    """Convert Roman numeral ``s`` to integer."""
    additions = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    subtractions = {"IV", "IX", "XL", "XC", "CD", "CM"}

    value = 0
    for i, numeral in enumerate(s):
        if s[i : i + 2] in subtractions:
            value -= additions[numeral]
        else:
            value += additions[numeral]

    return value
