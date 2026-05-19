r"""
>>> from palindrome_linked_list__approach_1 import ListNode, isPalindrome
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
