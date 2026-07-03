r"""
>>> from palindrome_linked_list__reverse_second_half import ListNode, isPalindrome
>>> head = ListNode.from_list([1, 2, 2, 1])
>>> isPalindrome(head)
True
>>> head = ListNode.from_list([1, 2])
>>> isPalindrome(head)
False
"""

from __future__ import annotations


class ListNode:
    """Node in a linked list."""

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, vals: list[int]) -> ListNode | None:
        dummy = cls(0)
        node = dummy
        for val in vals:
            node.next = cls(val)
            node = node.next
        return dummy.next


def isPalindrome(head: ListNode | None) -> bool:
    """Checks if the linked list is a palindrome."""
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
