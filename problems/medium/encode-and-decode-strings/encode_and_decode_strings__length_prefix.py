r"""
>>> from encode_and_decode_strings__length_prefix import Codec
>>> c = Codec()
>>> c.decode(c.encode(["hello", "world"]))
['hello', 'world']
>>> c.decode(c.encode([""]))
['']
>>> c.decode(c.encode([]))
[]
"""

from typing import List


class Codec:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        s = ""
        for t in strs:
            s += str(len(t)) + "#" + t
        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            strs.append(s[i:i + length])
            i = i + length

        return strs
