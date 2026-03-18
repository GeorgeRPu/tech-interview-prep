"""
Problem
-------
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a `Least
Recently Used (LRU)
cache <https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU>`__.

Implement the ``LRUCache`` class:

- ``LRUCache(int capacity)`` Initialize the LRU cache with **positive**
  size ``capacity``.
- ``int get(int key)`` Return the value of the ``key`` if the key
  exists, otherwise return ``-1``.
- ``void put(int key, int value)`` Update the value of the ``key`` if
  the ``key`` exists. Otherwise, add the ``key-value`` pair to the
  cache. If the number of keys exceeds the ``capacity`` from this
  operation, **evict** the least recently used key.

The functions ``get`` and ``put`` must each run in ``O(1)`` average time
complexity.

 

**Example 1:**

::


   Input
   ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
   [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
   Output
   [null, null, null, 1, null, -1, null, -1, 3, 4]

   Explanation
   LRUCache lRUCache = new LRUCache(2);
   lRUCache.put(1, 1); // cache is {1=1}
   lRUCache.put(2, 2); // cache is {1=1, 2=2}
   lRUCache.get(1);    // return 1
   lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
   lRUCache.get(2);    // returns -1 (not found)
   lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
   lRUCache.get(1);    // return -1 (not found)
   lRUCache.get(3);    // return 3
   lRUCache.get(4);    // return 4

 

**Constraints:**

- ``1 <= capacity <= 3000``
- ``0 <= key <= 10``\ :sup:```4```
- ``0 <= value <= 10``\ :sup:```5```
- At most ``2 * 10``\ :sup:```5``` calls will be made to ``get`` and
  ``put``.

Solution
--------
We want all ``get(key)`` and ``put(key, value)`` operations to be :math:`O(1)`. This
nessecitaties the use of a hashmap. The hashmap key-value pairs must be orderd
by usage in a list. Because list insertion and removal need to be done with
every get and put, we use a linked list. Once we exceed our fixed capacity, we
discard the items from the linked list and hashmap. To simplify the linked list
implementation, we use a dummy head and tail node whose keys are negative
values.

Code
----

.. literalinclude:: ../solutions/medium/LRUCache.py
    :language: python
    :lines: 96-

Test
----
>>> from LRUCache import LRUCache
>>> cache = LRUCache(2)
>>> cache.put(1, 1)
>>> cache.put(2, 2)
>>> cache.get(1)
1
>>> cache.put(3, 3)
>>> cache.get(2)
-1
>>> cache.put(4, 4)
>>> cache.get(1)
-1
>>> cache.get(3)
3
>>> cache.get(4)
4
"""

from __future__ import annotations
from typing import Dict, List


class LRUCache:
    """Implemented using a hashmap and a linked list.
    """

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.length: int = 0
        self.dict: Dict[str, Node] = {}
        self.ll: LinkedList = LinkedList()

    def get(self, key: int) -> int:
        try:
            node = self.dict[key]
            self.ll.remove(node)
            self.ll.appendleft(node)
            return node.value
        except KeyError:
            return -1

    def put(self, key: int, value: int):
        try:
            node = self.dict[key]
            node.value = value
            self.ll.remove(node)
            self.ll.appendleft(node)
        except KeyError:
            node = Node(key, value)
            self.dict[key] = node
            self.ll.appendleft(node)
            self.length += 1
            if self.length > self.capacity:
                lru = self.ll.tail.prev
                self.ll.remove(lru)
                del self.dict[lru.key]
                self.length -= 1

    def __str__(self) -> str:
        node = self.ll.head
        strings: List[str] = []
        while node is not None:
            strings.append(str(node))
            node = node.next
        return '{' + ', '.join(strings) + '}'


class Node:
    """Entry in the LRU cache.
    """

    def __init__(self, key: int, value: int):
        self.key: int = key
        self.value: int = value
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self) -> str:
        return f'{self.key}: {self.value}'

    def __repr__(self) -> str:
        return f'Node({self.key}, {self.value})'

    def none_ref(self):
        self.next = None
        self.prev = None


class LinkedList:
    """Linked list of entries in the LRU cache.
    """

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def appendleft(self, node: Node):
        node.none_ref()
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self) -> str:
        node = self.head
        strings: List[str] = []
        while node is not None:
            strings.append(str(node))
            node = node.next
        return '[' + ', '.join(strings[1:-1]) + ']'
