r"""
>>> from delete_node_in_a_linked_list__node_swap import ListNode, deleteNode
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
