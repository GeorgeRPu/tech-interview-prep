from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/sort-list/

Solution
--------
Use merge sort.

Code
----

.. literalinclude:: ../solutions/medium/SortList.py
    :language: python
    :lines: 30-

Test
----
>>> from SortList import ListNode, sortList
>>> head = ListNode.from_list([4, 2, 1, 3])
>>> head = sortList(head)
>>> print(head)
1 -> 2 -> 3 -> 4
>>> head = ListNode.from_list([-1, 5, 3, 4, 0])
>>> head = sortList(head)
>>> print(head)
-1 -> 0 -> 3 -> 4 -> 5
"""

from typing import List, Tuple


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')

    @classmethod
    def from_list(cls, list: List[int]) -> ListNode | None:
        head = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def sortList(head: ListNode | None) -> ListNode | None:
    """Sort linked list.
    """
    node = head
    length = 0
    while node is not None:
        node = node.next
        length += 1

    return sort_list(head, length)


def sort_list(head: ListNode | None, length: int):
    """Sort a linked list of length ``length`` with merge sort.
    """
    if length <= 1:
        return head

    node = head
    midpoint = length // 2
    for i in range(midpoint - 1):
        node = node.next
    next_node = node.next
    node.next = None

    left_head = sort_list(head, midpoint)
    right_head = sort_list(next_node, length - midpoint)

    new_head = None
    prev_node = None

    while left_head is not None or right_head is not None:
        node, left_head, right_head = minimum(left_head, right_head)
        if new_head is None:
            new_head = node
        elif prev_node is not None:
            prev_node.next = node
        prev_node = node
        node = node.next

    return new_head


def minimum(list1: ListNode | None, list2: ListNode | None) -> Tuple[ListNode | None]:
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
