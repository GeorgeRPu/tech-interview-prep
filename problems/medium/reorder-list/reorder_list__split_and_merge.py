r"""
>>> from reorder_list__split_and_merge import reorderList, ListNode
>>> head = ListNode.from_list([1, 2, 3, 4])
>>> reorderList(head)
>>> head.to_list()
[1, 4, 2, 3]
>>> head = ListNode.from_list([1, 2, 3, 4, 5])
>>> reorderList(head)
>>> head.to_list()
[1, 5, 2, 4, 3]
"""

from __future__ import annotations

from typing import List, Optional
from typing import Optional

class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, vals: List[int]) -> ListNode | None:
        head: ListNode | None = None
        for v in vals:
            if head is None:
                head = ListNode(v)
                node = head
            else:
                node.next = ListNode(v)
                node = node.next
        return head

    def to_list(self) -> list:
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        original_next = slow.next
        slow.next = prev
        prev = slow
        slow = original_next

    while head and prev:
        original_head_next = head.next
        original_prev_next = prev.next

        head.next = prev
        prev.next = original_head_next

        head = original_head_next
        prev = original_prev_next
