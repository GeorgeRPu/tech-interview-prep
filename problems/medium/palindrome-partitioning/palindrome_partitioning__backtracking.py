r"""
>>> from palindrome_partitioning__backtracking import partition
>>> sorted(partition("aab"))
[['a', 'a', 'b'], ['aa', 'b']]
>>> partition("a")
[['a']]
"""


def partition(s: str) -> list[list[str]]:
    partitions = []

    def backtrack(partition, i):

        if i == len(s):
            partitions.append(partition)

        for j in range(i + 1, len(s) + 1):
            t = s[i:j]
            if t == t[::-1]:
                backtrack(partition + [t], j)

    backtrack([], 0)
    return partitions
