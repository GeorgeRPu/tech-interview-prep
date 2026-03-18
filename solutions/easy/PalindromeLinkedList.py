"""
Problem
-------
https://leetcode.com/problems/palindrome-linked-list/

Given the ``head`` of a singly linked list, return ``true`` *if it is a*
palindrome *or* ``false`` *otherwise*.

 

**Example 1:**

|image1|

::


   Input: head = [1,2,2,1]
   Output: true

**Example 2:**

|image2|

::


   Input: head = [1,2]
   Output: false

 

**Constraints:**

- The number of nodes in the list is in the range
  ``[1, 10``\ :sup:```5```\ ``]``.
- ``0 <= Node.val <= 9``

 

**Follow up:** Could you do it in ``O(n)`` time and ``O(1)`` space?

.. |image1| image:: https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg

Solution
--------
Save the contents of the linked list in a regular list ``list``. Then, use two
pointers``i`` and ``j`` to check if ``list`` is a palindrome, moving them
inwards if ``list[i] == list[j]``.

Code
----

.. literalinclude:: ../solutions/easy/PalindromeLinkedList.py
    :language: python
    :lines: 29-

Test
----
>>> from PalindromeLinkedList import ListNode, isPalindrome
>>> head = ListNode.from_list([1, 2, 2, 1])
>>> isPalindrome(head)
True
>>> head = ListNode.from_list([1, 2])
>>> isPalindrome(head)
False
"""
from __future__ import annotations

from typing import List


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

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


def isPalindrome(head: ListNode | None) -> bool:
    """Checks if the linked list is a palindrome.
    """
    list = []
    while head is not None:
        list.append(head.val)
        head = head.next

    i = 0
    j = len(list) - 1
    while i < j:
        if list[i] != list[j]:
            return False
        i += 1
        j -= 1
    return True
