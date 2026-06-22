r"""
>>> from top_k_frequent_elements__sorting import topKFrequent
>>> sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2))
[1, 2]
>>> topKFrequent([1], 1)
[1]
"""

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    for n in nums:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1

    counter_list = [(n, count) for n, count in counter.items()]
    counter_list = sorted(counter_list, key=lambda tup: tup[1], reverse=True)
    topk = counter_list[:k]
    return [n for n, count in topk]


