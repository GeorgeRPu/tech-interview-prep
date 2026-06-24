r"""
>>> from palindromic_substrings__expand_from_center import countSubstrings
>>> countSubstrings("abc")
3
>>> countSubstrings("aaa")
6
"""


def countSubstrings(s: str) -> int:
    substrs = 0

    for i in range(len(s)):
        for j in [1, 2]:
            left = i
            right = i + j

            while (
                0 <= left < right <= len(s)
                and s[left:right] == s[left:right][::-1]
            ):
                substrs += 1
                left -= 1
                right += 1

    return substrs
