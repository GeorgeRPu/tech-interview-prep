r"""
>>> from linked_list_cycle__floyds_cycle_detection import ListNode, hasCycle
>>> head = ListNode.from_list([3, 2, 0, -4])
>>> head.next.next.next.next = head.next
>>> hasCycle(head)
True
>>> head = ListNode.from_list([1, 2])
>>> head.next.next = head
>>> hasCycle(head)
True
>>> head = ListNode.from_list([1])
>>> hasCycle(head)
False
"""

from __future__ import annotations


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, list: list[int]) -> ListNode | None:
        head: ListNode | None = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def hasCycle(head: ListNode | None) -> bool:
    """Whether the linked list has a cycle.
    """
    if head is None:
        return False

    a = head
    b = head.next

    while b is not None:
        if a is b:
            return True

        a = a.next
        b = b.next
        if b is not None:
            b = b.next

    return False
