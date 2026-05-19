r"""
>>> from remove_nth_node_from_end_of_list__approach_1 import ListNode, removeNthFromEnd
>>> head = ListNode.from_list([1, 2, 3, 4, 5])
>>> removeNthFromEnd(head, 2).to_list()
[1, 2, 3, 5]
>>> head = ListNode.from_list([1])
>>> print(removeNthFromEnd(head, 1))
None
>>> head = ListNode.from_list([1, 2])
>>> removeNthFromEnd(head, 1).to_list()
[1]
"""

from __future__ import annotations

from typing import List


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        list = []
        while self is not None:
            list.append(self.val)
            self = self.next
        return list

    @classmethod
    def from_list(cls, list: List[int]) -> ListNode | None:
        head: ListNode | None = None
        prev_node: ListNode | None = None
        for el in list:
            node = ListNode(el)
            if head is None:
                head = node
            elif prev_node is not None:
                prev_node.next = node
                prev_node = node
            prev_node = node
        return head


def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    """Remove the nth node from the end of the linked list starting at ``head``.
    """
    node = head
    length = 0
    while node is not None:
        length += 1
        node = node.next

    i = length - n

    # remove the first node
    if i == 0:
        head = head.next
        return head

    # remove a middle node
    prev = head
    for i in range(i - 1):
        prev = prev.next
    prev.next = prev.next.next

    return head
