"""
Problem
-------
https://leetcode.com/problems/length-of-last-word/

Given a string ``s`` consisting of words and spaces, return *the length
of the* **last** *word in the string.*

A **word** is a maximal substring consisting of non-space characters
only.

 

**Example 1:**

::


   Input: s = "Hello World"
   Output: 5
   Explanation: The last word is "World" with length 5.

**Example 2:**

::


   Input: s = "   fly me   to   the moon  "
   Output: 4
   Explanation: The last word is "moon" with length 4.

**Example 3:**

::


   Input: s = "luffy is still joyboy"
   Output: 6
   Explanation: The last word is "joyboy" with length 6.

 

**Constraints:**

- ``1 <= s.length <= 10``\ :sup:```4```
- ``s`` consists of only English letters and spaces ``' '``.
- There will be at least one word in ``s``.

Solution
--------
Strip all the whitespace from the end of the string, then split the string by
spaces. The last element in the list is the last word in the string.

Code
----

.. literalinclude:: ../solutions/easy/LengthOfLastWord.py
    :language: python
    :lines: 73-

Test
----
>>> from LengthOfLastWord import lengthOfLastWord
>>> lengthOfLastWord('Hello World')
5
>>> lengthOfLastWord('   fly me   to   the moon  ')
4
>>> lengthOfLastWord('luffy is still joyboy')
6
"""


def lengthOfLastWord(s: str) -> int:
    """Finds the length of the last word in a string.
    """
    return len(s.strip().split(' ')[-1])
