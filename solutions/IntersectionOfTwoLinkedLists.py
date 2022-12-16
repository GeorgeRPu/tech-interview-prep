"""
Problem
-------
https://leetcode.com/problems/intersection-of-two-linked-lists/

Solution
--------
Use a set to store the nodes in the first linked list with ``headA``. Then,
check if any node in the second linked list with ``headB`` is in the set.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/IntersectionOfTwoLinkedLists.py

.. literalinclude:: ../solutions/IntersectionOfTwoLinkedLists.py
    :language: python
    :lines: 36-

Test
----
>>> from IntersectionOfTwoLinkedLists import ListNode, getIntersectionNode
>>> a = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
>>> b = ListNode(5, ListNode(0, ListNode(1, a.next.next)))
>>> getIntersectionNode(a, b).val
8
>>> a = ListNode(0, ListNode(9, ListNode(1, ListNode(2, ListNode(4)))))
>>> b = ListNode(3, a.next.next.next)
>>> getIntersectionNode(a, b).val
2
>>> a = ListNode(2, ListNode(6, ListNode(4)))
>>> b = ListNode(1, ListNode(5))
>>> getIntersectionNode(a, b) is None
True
"""

from typing import Optional


class ListNode:

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """Gets the first node where two linked lists intersect. Returns ``None``
    if there is no intersection.
    """
    setA = set()
    while headA is not None:
        setA.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in setA:
            return headB
        headB = headB.next
    return None
