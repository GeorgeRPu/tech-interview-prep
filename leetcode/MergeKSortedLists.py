from __future__ import annotations

"""
Problem
-------
https://leetcode.com/problems/merge-k-sorted-lists/
This is the problem that got me my first internship at Amazon.

Solution
--------
Same as merge 2 sorted linked lists: pick smallest head and add to end of new
list.
"""

import heapq
from typing import List, Optional


class Node:

    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next = next

    def __lt__(self, node: Node) -> bool:
        return self.val < node.val

    def __eq__(self, node: object) -> bool:
        if not isinstance(node, Node):
            return NotImplemented
        return self.val == node.val

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')


def from_list(lst: List[int]) -> Optional[Node]:
    head: Optional[Node] = None
    prev_node: Optional[Node] = None
    for el in lst:
        node = Node(el)
        if head is None:
            head = node
        elif prev_node is not None:
            prev_node.next = node
            prev_node = node
        prev_node = node
    return head


def merge_k_lists(heads: List[Optional[Node]]) -> Optional[Node]:
    not_none_heads: List[Node] = [head for head in heads if head is not None]
    heapq.heapify(not_none_heads)
    new_head: Optional[Node] = None
    prev_node: Optional[Node] = None
    while len(not_none_heads) > 0:
        node = heapq.heappop(not_none_heads)
        if new_head is None:
            new_head = node
        elif prev_node is not None:
            prev_node.next = node
        prev_node = node
        if node.next is not None:
            heapq.heappush(not_none_heads, node.next)
    return new_head


head1 = from_list([1, 5, 6])
print(head1)
head2 = from_list([2, 3, 7])
print(head2)
head3 = from_list([2, 4, 8])
print(head3)
head = merge_k_lists([head1, head2, head3])
print(head)
