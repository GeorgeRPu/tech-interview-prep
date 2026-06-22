r"""
>>> from longest_common_subsequence__dynamic_programming import longestCommonSubsequence
>>> longestCommonSubsequence("abcde", "ace")
3
>>> longestCommonSubsequence("abc", "abc")
3
>>> longestCommonSubsequence("abc", "def")
0
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    M = len(text1)
    N = len(text2)
    lcs = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if text1[i - 1] == text2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[-1][-1]
