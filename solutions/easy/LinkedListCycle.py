from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/linked-list-cycle/

Solution
--------
Set two pointers, ``a`` and ``b``, to ``head``. Move ``a`` 1 node at a time but
move ``b`` 2 nodes at a time. If ``a`` and ``b`` ever point to the same node,
then ``b`` must have wrapped around the linked list and caught up to ``a``.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/LinkedListCycle.py

.. literalinclude:: ../solutions/easy/LinkedListCycle.py
    :language: python
    :lines: 38-

Test
----
>>> from LinkedListCycle import ListNode, hasCycle
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

from typing import List, Optional


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, list: List[int]) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        for el in list:
            if head is None:
                head = ListNode(el)
                node = head
            else:
                node.next = ListNode(el)
                node = node.next
        return head


def hasCycle(head: Optional[ListNode]) -> bool:
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
