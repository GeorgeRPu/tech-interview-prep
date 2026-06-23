r"""
>>> from reverse_linked_list__iterative import ListNode, reverseList
>>> head = ListNode.from_list([1, 2, 3, 4, 5])
>>> reverseList(head).to_list()
[5, 4, 3, 2, 1]
>>> head = ListNode.from_list([1, 2])
>>> reverseList(head).to_list()
[2, 1]
>>> head = ListNode.from_list([1])
>>> reverseList(head).to_list()
[1]
"""

from __future__ import annotations


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def to_list(self) -> list[int]:
        list = []
        while self is not None:
            list.append(self.val)
            self = self.next
        return list

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


def reverseList(head: ListNode | None) -> ListNode | None:
    prev = None
    node = head
    while node is not None:
        original_next = node.next
        node.next = prev

        prev = node
        node = original_next
    return prev
