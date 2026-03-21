r"""
Problem
-------
https://leetcode.com/problems/insert-delete-getrandom-o1/

Implement the ``RandomizedSet`` class:

- ``RandomizedSet()`` Initializes the ``RandomizedSet`` object.
- ``bool insert(int val)`` Inserts an item ``val`` into the set if not
  present. Returns ``true`` if the item was not present, ``false``
  otherwise.
- ``bool remove(int val)`` Removes an item ``val`` from the set if
  present. Returns ``true`` if the item was present, ``false``
  otherwise.
- ``int getRandom()`` Returns a random element from the current set of
  elements (it's guaranteed that at least one element exists when this
  method is called). Each element must have the **same probability** of
  being returned.

You must implement the functions of the class such that each function
works in **average** ``O(1)`` time complexity.

 

**Example 1:**

::


   Input
   ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
   [[], [1], [2], [2], [], [1], [2], []]
   Output
   [null, true, false, true, 2, true, false, 2]

   Explanation
   RandomizedSet randomizedSet = new RandomizedSet();
   randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
   randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
   randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
   randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
   randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
   randomizedSet.insert(2); // 2 was already in the set, so return false.
   randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

 

**Constraints:**

- ``-2``\ :sup:```31```\ ``<= val <= 2``\ :sup:```31```\ ``- 1``
- At most ``2 * ``\ ``10``\ :sup:```5``` calls will be made to
  ``insert``, ``remove``, and ``getRandom``.
- There will be **at least one** element in the data structure when
  ``getRandom`` is called.

Solution
--------
By default, we can insert and getRandom elements from an array in :math:`O(1)`
time. To remove an element from an array in :math:`O(1)` time, it needs to be
at the end of the array. We can move ``val`` to the end. To do this in
:math:`O(1)` time, we need to find the index of ``val`` in the array in
:math:`O(1)` time. We can use a dictionary to store the indices of each element
in the array.

Pattern
-------
Array, Hash Table, Math, Design, Randomized

Code
----

.. literalinclude:: ../solutions/medium/InsertDeleteGetRandomO1.py
    :language: python
    :lines: 97-

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
