r"""
>>> from edit_distance__dynamic_programming import minDistance
>>> minDistance("horse", "ros")
3
>>> minDistance("intention", "execution")
5
"""


def minDistance(word1: str, word2: str) -> int:
    M = len(word1)
    N = len(word2)

    edit_dist = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    for i in range(M + 1):
        edit_dist[i][0] = i

    for j in range(N + 1):
        edit_dist[0][j] = j

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if word1[i - 1] == word2[j - 1]:
                edit_dist[i][j] = edit_dist[i - 1][j - 1]
            else:
                edit_dist[i][j] = 1 + min(edit_dist[i][j - 1], edit_dist[i - 1][j], edit_dist[i - 1][j - 1])

    return edit_dist[-1][-1]
