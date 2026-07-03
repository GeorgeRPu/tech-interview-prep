r"""
>>> from task_scheduler__max_heap import leastInterval
>>> leastInterval(["A","A","A","B","B","B"], 2)
8
>>> leastInterval(["A","C","A","B","D","B"], 1)
6
>>> leastInterval(["A","A","A","B","B","B"], 3)
10
"""

import heapq
from collections import Counter, deque


def leastInterval(tasks: list[str], n: int) -> int:
    """Return the minimum intervals to finish all *tasks*."""
    counter = Counter(tasks)
    heap = [-count for count in counter.values()]
    heapq.heapify(heap)

    time = 0
    cooldown: deque[tuple[int, int]] = deque()

    while heap or cooldown:
        time += 1

        if not heap:
            time = cooldown[0][1]
        else:
            count = heapq.heappop(heap) + 1
            if count < 0:
                cooldown.append((count, time + n))

        if cooldown and cooldown[0][1] == time:
            heapq.heappush(heap, cooldown.popleft()[0])

    return time
