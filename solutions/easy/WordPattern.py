"""
Problem
-------
https://leetcode.com/problems/word-pattern/

Given a ``pattern`` and a string ``s``, find if ``s`` follows the same
pattern.

Here **follow** means a full match, such that there is a bijection
between a letter in ``pattern`` and a **non-empty** word in ``s``.
Specifically:

- Each letter in ``pattern`` maps to **exactly** one unique word in
  ``s``.
- Each unique word in ``s`` maps to **exactly** one letter in
  ``pattern``.
- No two letters map to the same word, and no two words map to the same
  letter.

 

**Example 1:**

.. container:: example-block

   **Input:** pattern = "abba", s = "dog cat cat dog"

   **Output:** true

   **Explanation:**

   The bijection can be established as:

   - ``'a'`` maps to ``"dog"``.
   - ``'b'`` maps to ``"cat"``.

**Example 2:**

.. container:: example-block

   **Input:** pattern = "abba", s = "dog cat cat fish"

   **Output:** false

**Example 3:**

.. container:: example-block

   **Input:** pattern = "aaaa", s = "dog cat cat dog"

   **Output:** false

 

**Constraints:**

- ``1 <= pattern.length <= 300``
- ``pattern`` contains only lower-case English letters.
- ``1 <= s.length <= 3000``
- ``s`` contains only lowercase English letters and spaces ``' '``.
- ``s`` **does not contain** any leading or trailing spaces.
- All the words in ``s`` are separated by a **single space**.

Solution
--------
Split ``s`` into a list of words. The problem reduces to IsomorphicStrings but
with characters in ``pattern`` and elements in ``s``. Since ``pattern`` and
``s`` can have different lenghts, we first check that they have the same
length.

Code
----

.. literalinclude:: ../solutions/easy/WordPattern.py
    :language: python
    :lines: 90-

Test
----
>>> from WordPattern import wordPattern
>>> wordPattern('abba', 'dog cat cat dog')
True
>>> wordPattern('abba', 'dog cat cat fish')
False
>>> wordPattern('aaaa', 'dog cat cat dog')
False
"""


def wordPattern(pattern: str, s: str) -> bool:
    """Given a pattern and a string s, finds if ``s`` follows the same pattern.
    """
    words = s.split()

    if len(pattern) != len(words):
        return False

    d = {}
    d_range = set()
    for char, word in zip(pattern, words):
        if char in d:
            if d[char] != word:
                return False
        else:
            if word in d_range:
                return False
            else:
                d[char] = word
                d_range.add(word)

    return True
