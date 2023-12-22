from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/delete-node-in-a-linked-list/

Solution
--------
Because we do not have access to the previous node, we cannot delete ``node``
in the usual fashion by setting the previous node's ``next`` pointer to
``node.next``. Instead we can shift the values in the linked list to the left,
dropping the tail node.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/DeleteNodeInALinkedList.py

.. literalinclude:: ../solutions/medium/DeleteNodeInALinkedList.py
    :language: python
    :lines: 36-

Test
----
>>> from DeleteNodeInALinkedList import ListNode, deleteNode
>>> head = ListNode.from_list([4, 5, 1, 9])
>>> deleteNode(head.next)
>>> print(head)
4 -> 1 -> 9
>>> head = ListNode.from_list([4, 5, 1, 9])
>>> deleteNode(head.next.next)
>>> print(head)
4 -> 5 -> 9
"""

from typing import List, Optional


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')

    @classmethod
    def from_list(cls, list: List[int]) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def deleteNode(node: ListNode) -> None:
    """Delete ``node`` from a linked list.
    """
    while node is not None and node.next is not None:
        node.val = node.next.val
        if node.next.next is None:
            node.next = None

        node = node.next
