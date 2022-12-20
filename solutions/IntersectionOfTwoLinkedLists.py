from __future__ import annotations

__doc__ = """
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
    :lines: 38-

Test
----
>>> from IntersectionOfTwoLinkedLists import ListNode, getIntersectionNode
>>> a = ListNode.from_list([4, 1, 8, 4, 5])
>>> b = ListNode(5, ListNode(0, ListNode(1, a.next.next)))
>>> getIntersectionNode(a, b).val
8
>>> a = ListNode.from_list([0, 9, 1, 2, 4])
>>> b = ListNode(3, a.next.next.next)
>>> getIntersectionNode(a, b).val
2
>>> a = ListNode.from_list([2, 6, 4])
>>> b = ListNode.from_list([1, 5])
>>> getIntersectionNode(a, b) is None
True
"""

from typing import List, Optional


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: Optional[ListNode] = None) -> None:
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
