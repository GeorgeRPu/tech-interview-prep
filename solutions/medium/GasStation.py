"""
Problem
-------
https://leetcode.com/problems/gas-station/

Solution
--------
Create a ``surplus`` array, which stores the difference between gas and cost.
If the sum of ``surplus`` is negative, then there is not enough gas to complete
the circuit no matter the starting point. Otherwise, we can complete the
circuit. Observe that if we cannot complete the circuit by ``i``, then we
cannot complete the circuit starting at any station in ``[start, i]``. This is
because the car had a non-empty tank until ``i``. Thus, if there is a solution,
it must be in ``[i + 1, n]``.

Code
----

.. literalinclude:: ../solutions/medium/GasStation.py
    :language: python
    :lines: 34-

Test
----
>>> from GasStation import canCompleteCircuit
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
