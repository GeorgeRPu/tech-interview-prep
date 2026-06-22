r"""
>>> from time_based_key_value_store__binary_search import TimeMap
>>> t = TimeMap()
>>> t.set("foo", "bar", 1)
>>> t.get("foo", 1)
'bar'
>>> t.get("foo", 3)
'bar'
>>> t.set("foo", "bar2", 4)
>>> t.get("foo", 4)
'bar2'
>>> t.get("foo", 5)
'bar2'
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]

        left = 0
        right = len(vals) - 1
        closest = ""

        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] == timestamp:
                return vals[mid][0]
            elif vals[mid][1] > timestamp:
                right = mid - 1
            else:
                closest = vals[mid][0]
                left = mid + 1

        return closest
