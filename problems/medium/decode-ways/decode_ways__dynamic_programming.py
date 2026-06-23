r"""
>>> from decode_ways__dynamic_programming import numDecodings
>>> numDecodings("12")
2
>>> numDecodings("226")
3
>>> numDecodings("06")
0
"""

CODES = {str(i) for i in range(1, 27)}


def numDecodings(s: str) -> int:
    N = len(s)
    num_ways = [0] * N

    for i in range(N):
        if i == 0:
            num_ways[i] = 1 if s[i] in CODES else 0
        elif i == 1:
            one_digit = num_ways[i - 1] if s[i] in CODES else 0
            two_digit = 1 if s[i - 1:i + 1] in CODES else 0
            num_ways[i] = one_digit + two_digit
        else:
            one_digit = num_ways[i - 1] if s[i] in CODES else 0
            two_digit = num_ways[i - 2] if s[i - 1:i + 1] in CODES else 0
            num_ways[i] = one_digit + two_digit

    return num_ways[-1]
