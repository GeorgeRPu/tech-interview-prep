r"""
>>> from add_two_numbers__iterative import addTwoNumbers, ListNode
>>> l1 = ListNode.from_list([2, 4, 3])
>>> l2 = ListNode.from_list([5, 6, 4])
>>> addTwoNumbers(l1, l2).to_list()
[7, 0, 8]
>>> l1 = ListNode.from_list([0])
>>> l2 = ListNode.from_list([0])
>>> addTwoNumbers(l1, l2).to_list()
[0]
>>> l1 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
>>> l2 = ListNode.from_list([9, 9, 9, 9])
>>> addTwoNumbers(l1, l2).to_list()
[8, 9, 9, 9, 0, 0, 0, 1]
"""

from __future__ import annotations


class ListNode:
    """Node in a linked list."""

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def to_list(self):
        list = []
        while self is not None:
            list.append(self.val)
            self = self.next
        return list

    @classmethod
    def from_list(cls, vals: list[int]) -> ListNode | None:
        dummy = cls(0)
        node = dummy
        for val in vals:
            node.next = cls(val)
            node = node.next
        return dummy.next


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None):
    """Add two numbers whose digits are stored in little endian linked lists."""
    head = None

    carry = 0
    while not (l1 is None and l2 is None and carry == 0):
        if l1 is not None:
            val1 = l1.val
            l1 = l1.next
        else:
            val1 = 0

        if l2 is not None:
            val2 = l2.val
            l2 = l2.next
        else:
            val2 = 0

        s = carry + val1 + val2
        digit = s % 10
        carry = s // 10

        if head is None:
            head = ListNode(digit, None)
            node = head
        else:
            node.next = ListNode(digit, None)
            node = node.next

    return head
