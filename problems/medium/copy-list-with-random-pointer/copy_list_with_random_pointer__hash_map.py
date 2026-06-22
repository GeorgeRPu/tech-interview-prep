r"""
>>> from copy_list_with_random_pointer__hash_map import copyRandomList, Node
>>> n1, n2, n3 = Node(7), Node(13), Node(11)
>>> n1.next, n2.next = n2, n3
>>> n2.random, n3.random = n1, n1
>>> c = copyRandomList(n1)
>>> [c.val, c.next.val, c.next.next.val]
[7, 13, 11]
>>> c is not n1
True
"""

from __future__ import annotations

from collections import defaultdict
from typing import Optional


class Node:
    """Node in a linked list with a random pointer.
    """

    def __init__(self, x: int = 0, next: Node | None = None, random: Node | None = None):
        self.val = x
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    old2copy: dict[Node | None, Node | None] = defaultdict(lambda: Node(0))
    old2copy[None] = None

    node = head
    copy_head = None
    while node:
        copy = old2copy[node]
        copy.val = node.val
        copy.next = old2copy[node.next]
        copy.random = old2copy[node.random]

        if copy_head is None:
            copy_head = copy

        node = node.next

    return copy_head
