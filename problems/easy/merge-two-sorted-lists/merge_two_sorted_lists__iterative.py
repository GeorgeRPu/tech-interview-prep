r"""
>>> from merge_two_sorted_lists__iterative import ListNode, merge_2_lists
>>> head1 = ListNode.from_list([1, 2, 4])
>>> head2 = ListNode.from_list([1, 3, 4])
>>> head = merge_2_lists(head1, head2)
>>> print(head)
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

from __future__ import annotations


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        suffix = ' -> ' + str(self.next) if self.next else ''
        return str(self.val) + suffix

    @classmethod
    def from_list(cls, list: list[int]) -> ListNode | None:
        head = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def merge_2_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Merge two sorted linked lists.
    """
    dummy = node = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next

        node = node.next

    node.next = list1 or list2

    return dummy.next
