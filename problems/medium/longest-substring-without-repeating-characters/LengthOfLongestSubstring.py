r"""
>>> from LengthOfLongestSubstring import lengthOfLongestSubstring
>>> lengthOfLongestSubstring('abcabcbb')
3
>>> lengthOfLongestSubstring('bbbbb')
1
>>> lengthOfLongestSubstring('pwwkew')
3
"""


def lengthOfLongestSubstring(s: str) -> int:
    """Finds the length of the longest substring without repeating characters.
    """
    longest_len = 0
    for i in range(len(s)):
        j = i
        seen_chars = set()
        curr_len = 0
        while j < len(s):
            char = s[j]
            if char in seen_chars:
                break
            else:
                curr_len += 1
                seen_chars.add(char)
                j += 1

            longest_len = max(longest_len, curr_len)

    return longest_len
