r"""
Problem
-------
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists ``list1`` and
``list2``.

Merge the two lists into one **sorted** list. The list should be made by
splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

 

**Example 1:**

|image1|

::


   Input: list1 = [1,2,4], list2 = [1,3,4]
   Output: [1,1,2,3,4,4]

**Example 2:**

::


   Input: list1 = [], list2 = []
   Output: []

**Example 3:**

::


   Input: list1 = [], list2 = [0]
   Output: [0]

 

**Constraints:**

- The number of nodes in both lists is in the range ``[0, 50]``.
- ``-100 <= Node.val <= 100``
- Both ``list1`` and ``list2`` are sorted in **non-decreasing** order.

.. |image1| image:: https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg

Solution
--------
Create the new list by selecting the minimum node of ``list1`` and ``list2``,
checking if either is ``None``. Set the ``next`` field of the previous node to
the minimum node. Advance the ``list1``/``list2`` and previous node pointers.

Pattern
-------
Linked List, Recursion

Code
----

.. literalinclude:: ../solutions/easy/MergeTwoSortedLists.py
    :language: python
    :lines: 78-

Test
----
>>> from MergeTwoSortedLists import ListNode, merge_2_lists
>>> head1 = ListNode.from_list([1, 2, 4])
>>> head2 = ListNode.from_list([1, 3, 4])
>>> head = merge_2_lists(head1, head2)
>>> print(head)
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""
from __future__ import annotations

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


def merge_2_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
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
