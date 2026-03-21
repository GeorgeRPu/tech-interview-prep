"""
Problem
-------
https://leetcode.com/problems/delete-node-in-a-linked-list/

There is a singly-linked list ``head`` and we want to delete a node
``node`` in it.

You are given the node to be deleted ``node``. You will **not be given
access** to the first node of ``head``.

All the values of the linked list are **unique**, and it is guaranteed
that the given node ``node`` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean
removing it from memory. We mean:

- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before ``node`` should be in the same order.
- All the values after ``node`` should be in the same order.

**Custom testing:**

- For the input, you should provide the entire linked list ``head`` and
  the node to be given ``node``. ``node`` should not be the last node of
  the list and should be an actual node in the list.
- We will build the linked list and pass the node to your function.
- The output will be the entire list after calling your function.

 

**Example 1:**

|image1|

::


   Input: head = [4,5,1,9], node = 5
   Output: [4,1,9]
   Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

**Example 2:**

|image2|

::


   Input: head = [4,5,1,9], node = 1
   Output: [4,5,9]
   Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

 

**Constraints:**

- The number of the nodes in the given list is in the range
  ``[2, 1000]``.
- ``-1000 <= Node.val <= 1000``
- The value of each node in the list is **unique**.
- The ``node`` to be deleted is **in the list** and is **not a tail**
  node.

.. |image1| image:: https://assets.leetcode.com/uploads/2020/09/01/node1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2020/09/01/node2.jpg

Solution
--------
Because we do not have access to the previous node, we cannot delete ``node``
in the usual fashion by setting the previous node's ``next`` pointer to
``node.next``. Instead we can shift the values in the linked list to the left,
dropping the tail node.

Pattern
-------
Linked List

Code
----

.. literalinclude:: ../solutions/medium/DeleteNodeInALinkedList.py
    :language: python
    :lines: 99-

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
from __future__ import annotations

from typing import List


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')

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


def deleteNode(node: ListNode) -> None:
    """Delete ``node`` from a linked list.
    """
    while node is not None and node.next is not None:
        node.val = node.next.val
        if node.next.next is None:
            node.next = None

        node = node.next
