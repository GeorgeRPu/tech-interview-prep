"""
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
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/LinkedListCycle.py

.. literalinclude:: ../solutions/LinkedListCycle.py
    :language: python
    :lines: 36-

Test
----
>>> from LinkedListCycle import ListNode, hasCycle
>>> head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
>>> head.next.next.next.next = head.next
>>> hasCycle(head)
True
>>> head = ListNode(1, ListNode(2))
>>> head.next.next = head
>>> hasCycle(head)
True
>>> head = ListNode(1)
>>> hasCycle(head)
False
"""

from typing import Optional


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


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
