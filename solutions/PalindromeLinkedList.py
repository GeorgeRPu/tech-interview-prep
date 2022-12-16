"""
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

.. literalinclude:: ../solutions/PalindromeLinkedList.py
    :language: python
    :lines: 32-

Test
----
>>> from PalindromeLinkedList import ListNode, isPalindrome
>>> head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
>>> isPalindrome(head)
True
>>> head = ListNode(1, ListNode(2))
>>> isPalindrome(head)
False
"""


from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
