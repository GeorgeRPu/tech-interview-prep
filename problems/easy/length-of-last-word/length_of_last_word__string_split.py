r"""
>>> from length_of_last_word__string_split import lengthOfLastWord
>>> lengthOfLastWord('Hello World')
5
>>> lengthOfLastWord('   fly me   to   the moon  ')
4
>>> lengthOfLastWord('luffy is still joyboy')
6
"""


def lengthOfLastWord(s: str) -> int:
    """Finds the length of the last word in a string."""
    return len(s.strip().split(" ")[-1])
