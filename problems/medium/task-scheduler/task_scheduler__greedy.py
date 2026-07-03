r"""
>>> from task_scheduler__greedy import leastInterval
>>> leastInterval(["A","A","A","B","B","B"], 2)
8
>>> leastInterval(["A","C","A","B","D","B"], 1)
6
>>> leastInterval(["A","A","A","B","B","B"], 3)
10
"""

from collections import Counter


def leastInterval(tasks: list[str], n: int) -> int:
    """Return the minimum intervals to finish all *tasks*."""
    counter = Counter(tasks)
    result = 0

    while counter:
        most_common = counter.most_common()
        m = min(n + 1, len(most_common))
        for i in range(m):
            result += 1
            task, _ = most_common[i]
            counter[task] -= 1
            if counter[task] == 0:
                del counter[task]

        if counter and n + 1 > m:
            result += n + 1 - m

    return result
