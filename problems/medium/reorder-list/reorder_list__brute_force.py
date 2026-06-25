r"""
>>> from reorder_list__brute_force import reorderList, ListNode
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


class ListNode:
    """Node in a linked list."""

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, vals: list[int]) -> ListNode | None:
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


def reorderList(head: ListNode | None) -> None:
    """Reorder ``head`` in-place by interleaving front and back."""
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next

    i = 0
    j = len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i >= j:
            break
        nodes[j].next = nodes[i]
        j -= 1

    nodes[i].next = None
