r"""
>>> from longest_consecutive_sequence__hash_set import longestConsecutive
>>> longestConsecutive([100, 4, 200, 1, 3, 2])
4
>>> longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
9
"""

from typing import List
from collections import defaultdict

    def longestConsecutive(nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
