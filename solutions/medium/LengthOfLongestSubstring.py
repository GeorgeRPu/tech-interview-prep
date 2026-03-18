"""
Problem
-------
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string ``s``, find the length of the **longest** substring
without duplicate characters.

 

**Example 1:**

::


   Input: s = "abcabcbb"
   Output: 3
   Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

**Example 2:**

::


   Input: s = "bbbbb"
   Output: 1
   Explanation: The answer is "b", with the length of 1.

**Example 3:**

::


   Input: s = "pwwkew"
   Output: 3
   Explanation: The answer is "wke", with the length of 3.
   Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

**Constraints:**

- ``0 <= s.length <= 5 * 10``\ :sup:```4```
- ``s`` consists of English letters, digits, symbols and spaces.

Solution
--------
The longest substring can start from any position in the string. So, we must
iterate through each position in the entire string. For each position, we look
right until we find a duplicate character. At each iteration, if the current
substring is longer than the longest, we update the length of the longest
substring. Once we find a duplicate character, reset the seen characters.

Code
----

.. literalinclude:: ../solutions/medium/LengthOfLongestSubstring.py
    :language: python
    :lines: 73-

Test
----
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
