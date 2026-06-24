r"""
>>> from ransom_note__character_count import canConstruct
>>> canConstruct("a", "b")
False
>>> canConstruct("aa", "ab")
False
>>> canConstruct("aa", "aab")
True
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """Checks if ``ransomNote`` can be constructed from ``magazine`` by cutting
    and gluing letters.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    counter = {letter: 0 for letter in letters}
    for char in magazine:
        counter[char] += 1

    for char in ransomNote:
        counter[char] -= 1

    for char, count in counter.items():
        if counter[char] < 0:
            return False

    return True
