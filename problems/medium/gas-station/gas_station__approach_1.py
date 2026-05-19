r"""
>>> from gas_station__approach_1 import canCompleteCircuit
>>> gas = [1, 2, 3, 4, 5]
>>> cost = [3, 4, 5, 1, 2]
>>> canCompleteCircuit(gas, cost)
3
>>> gas = [2, 3, 4]
>>> cost = [3, 4, 3]
>>> canCompleteCircuit(gas, cost)
-1
"""

from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    """Return the starting gas station index if we can complete the circuit, -1
    otherwise.
    """
    surplus = [g - c for g, c in zip(gas, cost)]

    if sum(surplus) < 0:
        return -1

    start = 0
    tank = 0
    for i, s in enumerate(surplus):
        tank += s
        if tank < 0:
            start = i + 1
            tank = 0

    return start
