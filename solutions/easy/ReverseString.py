"""
Problem
-------
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an
array of characters ``s``.

You must do this by modifying the input array
`in-place <https://en.wikipedia.org/wiki/In-place_algorithm>`__ with
``O(1)`` extra memory.

 

**Example 1:**

::

   Input: s = ["h","e","l","l","o"]
   Output: ["o","l","l","e","h"]

**Example 2:**

::

   Input: s = ["H","a","n","n","a","h"]
   Output: ["h","a","n","n","a","H"]

 

**Constraints:**

- ``1 <= s.length <= 10``\ :sup:```5```
- ``s[i]`` is a `printable ascii
  character <https://en.wikipedia.org/wiki/ASCII#Printable_characters>`__.

Solution
--------
Let :math:`n` be the length of the input list ``s``. Let ``end = n - 1``. We
can reverse the list by swapping the outermost elements, moving inwards. ::

    s[i], s[end - i] = s[end - i], s[i]

Code
----

.. literalinclude:: ../solutions/easy/ReverseString.py
    :language: python
    :lines: 65-

Test
----
>>> from ReverseString import reverseString
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> reverseString(s)
>>> s
['o', 'l', 'l', 'e', 'h']
>>> s = ['H', 'a', 'n', 'n', 'a', 'h']
>>> reverseString(s)
>>> s
['h', 'a', 'n', 'n', 'a', 'H']
"""


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    end = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[end - i] = s[end - i], s[i]
