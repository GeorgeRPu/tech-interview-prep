from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/reverse-linked-list/

Solution
--------
Track the current ``node`` and ``prev`` node. At each step, store ``node.next``
in a temporary variable. Set ``node.next`` to ``prev`` and then advance
``prev`` and ``node``.

Code
----

.. literalinclude:: ../solutions/easy/ReverseLinkedList.py
    :language: python
    :lines: 33-

Test
----
>>> from ReverseLinkedList import ListNode, reverseList
>>> head = ListNode.from_list([1, 2, 3, 4, 5])
>>> reverseList(head).to_list()
[5, 4, 3, 2, 1]
>>> head = ListNode.from_list([1, 2])
>>> reverseList(head).to_list()
[2, 1]
>>> head = ListNode.from_list([1])
>>> reverseList(head).to_list()
[1]
"""

from typing import List


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        list = []
        while self is not None:
            list.append(self.val)
            self = self.next
        return list

    @classmethod
    def from_list(cls, list: List[int]) -> ListNode | None:
        head: ListNode | None = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def reverseList(head: ListNode | None) -> ListNode | None:
    prev = None
    node = head
    while node is not None:
        original_next = node.next
        node.next = prev

        prev = node
        node = original_next
    return prev
