r"""
>>> from reverse_words_in_a_string__string_split import reverseWords
>>> reverseWords('the sky is blue')
'blue is sky the'
>>> reverseWords('  hello world  ')
'world hello'
>>> reverseWords('a good   example')
'example good a'
"""


def reverseWords(s: str) -> str:
    """Reverse the words in a string, separated by 1 space."""
    words = s.strip().split()
    return " ".join(reversed(words))
