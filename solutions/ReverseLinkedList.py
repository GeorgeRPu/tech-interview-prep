"""
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
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/ReverseLinkedList.py

Test
----
>>> from ReverseLinkedList import ListNode, reverseList
>>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
>>> reverseList(head).to_list()
[5, 4, 3, 2, 1]
>>> head = ListNode(1, ListNode(2))
>>> reverseList(head).to_list()
[2, 1]
>>> head = ListNode(1)
>>> reverseList(head).to_list()
[1]
"""

from typing import Optional


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        list = []
        while self is not None:
            list.append(self.val)
            self = self.next
        return list


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    node = head
    while node is not None:
        original_next = node.next
        node.next = prev

        prev = node
        node = original_next
    return prev
