from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/palindrome-linked-list/

Solution
--------
Save the contents of the linked list in a regular list ``list``. Then, use two
pointers``i`` and ``j`` to check if ``list`` is a palindrome, moving them
inwards if ``list[i] == list[j]``.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/PalindromeLinkedList.py

.. literalinclude:: ../solutions/easy/PalindromeLinkedList.py
    :language: python
    :lines: 34-

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


from typing import List, Optional


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

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


def isPalindrome(head: Optional[ListNode]) -> bool:
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
