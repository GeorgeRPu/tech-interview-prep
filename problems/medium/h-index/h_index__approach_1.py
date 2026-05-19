r"""
>>> from h_index__approach_1 import hIndex
>>> hIndex([3, 0, 6, 1, 5])
3
>>> hIndex([1, 3, 1])
1
"""

from typing import List


def hIndex(citations: List[int]) -> int:
    citations = reversed(sorted(citations))
    for h, citation_count in enumerate(citations):
        if h >= citation_count:
            return h

    return len(citations)
