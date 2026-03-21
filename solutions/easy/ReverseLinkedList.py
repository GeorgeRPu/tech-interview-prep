r"""
Problem
-------
https://leetcode.com/problems/reverse-linked-list/

Given the ``head`` of a singly linked list, reverse the list, and return
*the reversed list*.

 

**Example 1:**

|image1|

::


   Input: head = [1,2,3,4,5]
   Output: [5,4,3,2,1]

**Example 2:**

|image2|

::


   Input: head = [1,2]
   Output: [2,1]

**Example 3:**

::


   Input: head = []
   Output: []

 

**Constraints:**

- The number of nodes in the list is the range ``[0, 5000]``.
- ``-5000 <= Node.val <= 5000``

 

**Follow up:** A linked list can be reversed either iteratively or
recursively. Could you implement both?

.. |image1| image:: https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg

Solution
--------
Track the current ``node`` and ``prev`` node. At each step, store ``node.next``
in a temporary variable. Set ``node.next`` to ``prev`` and then advance
``prev`` and ``node``.

Pattern
-------
Linked List, Recursion

Code
----

.. literalinclude:: ../solutions/easy/ReverseLinkedList.py
    :language: python
    :lines: 84-

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
from __future__ import annotations

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
