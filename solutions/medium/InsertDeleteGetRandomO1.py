"""
Problem
-------
https://leetcode.com/problems/insert-delete-getrandom-o1/

Solution
--------
By default, we can insert and getRandom elements from an array in :math:`O(1)`
time. To remove an element from an array in :math:`O(1)` time, it needs to be
at the end of the array. We can move ``val`` to the end. To do this in
:math:`O(1)` time, we need to find the index of ``val`` in the array in
:math:`O(1)` time. We can use a dictionary to store the indices of each element
in the array.

Code
----

.. literalinclude:: ../solutions/medium/InsertDeleteGetRandomO1.py
    :language: python
    :lines: 43-

Test
----
>>> from InsertDeleteGetRandomO1 import RandomizedSet
>>> random_set = RandomizedSet()
>>> random_set.insert(1)
True
>>> random_set.remove(2)
False
>>> random_set.getRandom()
1
>>> random_set.insert(2)
True
>>> random_set.remove(1)
True
>>> random_set.insert(2)
False
>>> random_set.getRandom()
2
"""


import random


class RandomizedSet:
    """A data structure that supports ``insert``, ``remove``, and ``getRandom``
    in O(1) time.
    """

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """Inserts ``val`` into the set. Returns ``True`` if ``val`` was not
        present and ``False`` otherwise.
        """
        if val in self.indices:
            return False
        else:
            self.arr.append(val)
            self.indices[val] = len(self.arr) - 1
            return True

    def remove(self, val: int) -> bool:
        """Removes ``val`` from the set. Returns ``True`` if ``val`` was
        present and ``False`` otherwise.
        """
        if val not in self.indices:
            return False
        else:
            i = self.indices[val]
            self.indices[self.arr[-1]] = i

            self.arr[i] = self.arr[-1]

            del self.indices[val]
            self.arr.pop()
            return True

    def getRandom(self) -> int:
        """Returns a random element from the set.
        """
        return random.choice(self.arr)
