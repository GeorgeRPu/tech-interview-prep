from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/merge-two-sorted-lists/

Solution
--------
Create the new list by selecting the minimum node of ``list1`` and ``list2``,
checking if either is ``None``. Set the ``next`` field of the previous node to
the minimum node. Advance the ``list1``/``list2`` and previous node pointers.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/Merge2SortedLists.py

Test
----
>>> from Merge2SortedLists import from_list, merge_2_lists
>>> head1 = from_list([1, 2, 4])
>>> head2 = from_list([1, 3, 4])
>>> head = merge_2_lists(head1, head2)
>>> print(head)
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

from typing import List, Optional, Tuple


class Node:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next = next

    def __lt__(self, node: Node) -> bool:
        return self.val < node.val

    def __eq__(self, node: object) -> bool:
        return self.val == node.val

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')


def from_list(lst: List[int]) -> Optional[Node]:
    """Create a linked list from a list of integers.
    """
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


def merge_2_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    """Merge two sorted linked lists.
    """
    new_head: Optional[Node] = None
    prev_node: Optional[Node] = None

    while list1 is not None or list2 is not None:
        node, list1, list2 = minimum(list1, list2)
        if new_head is None:
            new_head = node
        elif prev_node is not None:
            prev_node.next = node
        prev_node = node
        node = node.next

    return new_head


def minimum(list1: Optional[Node], list2: Optional[Node]) -> Tuple[Optional[Node]]:
    """Return the minimum node of ``list1`` and ``list2`` and advances the that
    pointer.
    """
    if list1 is None and list2 is None:
        return None, None, None
    elif list1 is None:
        return list2, None, None
    elif list2 is None:
        return list1, None, None
    elif list1 < list2:
        return list1, list1.next, list2
    else:
        return list2, list1, list2.next
