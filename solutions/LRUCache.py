"""
Problem
-------
https://leetcode.com/problems/lru-cache/

Solution
--------
We want all ``get(key)`` and ``put(key, value)`` operations to be :math:`O(1)`. This
nessecitaties the use of a hashmap. The hashmap key-value pairs must be orderd
by usage in a list. Because list insertion and removal need to be done with
every get and put, we use a linked list. Once we exceed our fixed capacity, we
discard the items from the linked list and hashmap.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/LRUCache.py

Test
----
>>> from LRUCache import LRUCache
>>> cache = LRUCache(2)
>>> cache.put('1', 'a')
>>> cache.put('2', 'b')
>>> cache.get('1')
'a'
>>> cache.put('3', 'c')
>>> cache.get('2')
'Key 2 was not found'
>>> cache.put('4', 'd')
>>> cache.get('1')
'Key 1 was not found'
>>> cache.get('3')
'c'
>>> cache.get('4')
'd'
"""

from __future__ import annotations
from typing import Dict, List, Optional


class Node:
    """Entry in the LRU cache.
    """

    def __init__(self, key: str, value: str):
        self.key: str = key
        self.value: str = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __str__(self) -> str:
        return f'{self.key}: {self.value}'

    def none_ref(self):
        self.next = None
        self.prev = None


class LinkedList:
    """Linked list of entries in the LRU cache.
    """

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def appendleft(self, node: Node):
        node.none_ref()
        if self.tail is None:
            self.tail = node
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove(self, node: Node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.next

    def __str__(self) -> str:
        node = self.head
        strings: List[str] = []
        while node is not None:
            strings.append(str(node))
            node = node.next
        return ' -> '.join(strings)


class LRUCache:
    """Implemented using a hashmap and a linked list.
    """

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.length: int = 0
        self.dict: Dict[str, Node] = {}
        self.ll: LinkedList = LinkedList()

    def get(self, key: str) -> str:
        try:
            node = self.dict[key]
            self.ll.remove(node)
            self.ll.appendleft(node)
            return node.value
        except KeyError:
            return f'Key {key} was not found'

    def put(self, key: str, value: str):
        node = Node(key, value)
        self.dict[key] = node
        self.ll.appendleft(node)
        self.length += 1
        tail = self.ll.tail
        if self.length > self.capacity and tail is not None:
            self.ll.remove(tail)
            del self.dict[tail.key]
            self.length -= 1

    def __str__(self) -> str:
        node = self.ll.head
        strings: List[str] = []
        while node is not None:
            strings.append(str(node))
            node = node.next
        return '{' + ', '.join(strings) + '}'
