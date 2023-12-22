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
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/Merge2SortedLists.py

.. literalinclude:: ../solutions/easy/MergeTwoSortedLists.py
    :language: python
    :lines: 32-

Test
----
>>> from MergeTwoSortedLists import ListNode, merge_2_lists
>>> head1 = ListNode.from_list([1, 2, 4])
>>> head2 = ListNode.from_list([1, 3, 4])
>>> head = merge_2_lists(head1, head2)
>>> print(head)
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

from typing import List, Optional, Tuple


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')

    @classmethod
    def from_list(cls, list: List[int]) -> Optional[ListNode]:
        head = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def merge_2_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists.
    """
    new_head = None
    prev_node = None

    while list1 is not None or list2 is not None:
        node, list1, list2 = minimum(list1, list2)
        if new_head is None:
            new_head = node
        elif prev_node is not None:
            prev_node.next = node
        prev_node = node
        node = node.next

    return new_head


def minimum(list1: Optional[ListNode], list2: Optional[ListNode]) -> Tuple[Optional[ListNode]]:
    """Return the minimum node of ``list1`` and ``list2`` and advances the that
    pointer.
    """
    if list1 is None and list2 is None:
        return None, None, None
    elif list1 is None:
        return list2, None, None
    elif list2 is None:
        return list1, None, None
    elif list1.val < list2.val:
        return list1, list1.next, list2
    else:
        return list2, list1, list2.next
