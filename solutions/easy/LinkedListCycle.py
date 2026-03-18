"""
Problem
-------
https://leetcode.com/problems/linked-list-cycle/

Given ``head``, the head of a linked list, determine if the linked list
has a cycle in it.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the ``next`` pointer.
Internally, ``pos`` is used to denote the index of the node
that tail's ``next`` pointer is connected to. **Note that ``pos`` is not
passed as a parameter**.

Return ``true`` *if there is a cycle in the linked list*. Otherwise,
return ``false``.

 

**Example 1:**

|image1|

::


   Input: head = [3,2,0,-4], pos = 1
   Output: true
   Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

|image2|

::


   Input: head = [1,2], pos = 0
   Output: true
   Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:**

|image3|

::


   Input: head = [1], pos = -1
   Output: false
   Explanation: There is no cycle in the linked list.

 

**Constraints:**

- The number of the nodes in the list is in the range
  ``[0, 10``\ :sup:```4```\ ``]``.
- ``-10``\ :sup:```5```\ ``<= Node.val <= 10``\ :sup:```5```
- ``pos`` is ``-1`` or a **valid index** in the linked-list.

 

**Follow up:** Can you solve it using ``O(1)`` (i.e. constant) memory?

.. |image1| image:: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png
.. |image2| image:: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png
.. |image3| image:: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png

Solution
--------
Set two pointers, ``a`` and ``b``, to ``head``. Move ``a`` 1 node at a time but
move ``b`` 2 nodes at a time. If ``a`` and ``b`` ever point to the same node,
then ``b`` must have wrapped around the linked list and caught up to ``a``.

Code
----

.. literalinclude:: ../solutions/easy/LinkedListCycle.py
    :language: python
    :lines: 34-

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
from __future__ import annotations

from typing import List


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

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


def hasCycle(head: ListNode | None) -> bool:
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
