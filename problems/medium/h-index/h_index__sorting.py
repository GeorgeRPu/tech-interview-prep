r"""
>>> from h_index__sorting import hIndex
>>> hIndex([3, 0, 6, 1, 5])
3
>>> hIndex([1, 3, 1])
1
"""


def hIndex(citations: list[int]) -> int:
    citations = reversed(sorted(citations))
    for h, citation_count in enumerate(citations):
        if h >= citation_count:
            return h

    return len(citations)
