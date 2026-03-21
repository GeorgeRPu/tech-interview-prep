r"""
Problem
-------
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of ``k`` linked-lists ``lists``, each linked-list
is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

 

**Example 1:**

::


   Input: lists = [[1,4,5],[1,3,4],[2,6]]
   Output: [1,1,2,3,4,4,5,6]
   Explanation: The linked-lists are:
   [
     1->4->5,
     1->3->4,
     2->6
   ]
   merging them into one sorted linked list:
   1->1->2->3->4->4->5->6

**Example 2:**

::


   Input: lists = []
   Output: []

**Example 3:**

::


   Input: lists = [[]]
   Output: []

 

**Constraints:**

- ``k == lists.length``
- ``0 <= k <= 10``\ :sup:```4```
- ``0 <= lists[i].length <= 500``
- ``-10``\ :sup:```4```\ ``<= lists[i][j] <= 10``\ :sup:```4```
- ``lists[i]`` is sorted in **ascending order**.
- The sum of ``lists[i].length`` will not exceed ``10``\ :sup:```4```.

Solution
--------
Same as merge 2 sorted linked lists: pick the smallest head and add it to the
end of the new list.

Pattern
-------
Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

Code
----

.. literalinclude:: ../solutions/hard/MergeKSortedLists.py
    :language: python
    :lines: 82-

Test
----
>>> from MergeKSortedLists import ListNode, merge_k_lists
>>> head1 = ListNode.from_list([1, 5, 6])
>>> head2 = ListNode.from_list([2, 3, 7])
>>> head3 = ListNode.from_list([2, 4, 8])
>>> head = merge_k_lists([head1, head2, head3])
>>> print(head)
1 -> 2 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
"""
from __future__ import annotations

import heapq
from typing import List


class ListNode:
    """Node in a linked list.
    """

    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __lt__(self, node: ListNode) -> bool:
        return self.val < node.val

    def __eq__(self, node: object) -> bool:
        return self.val == node.val

    def __str__(self) -> str:
        return str(self.val) + (' -> ' + str(self.next) if self.next is not None else '')

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


def merge_k_lists(heads: List[ListNode | None]) -> ListNode | None:
    """Merge k sorted linked lists.
    """
    not_none_heads: List[ListNode] = [head for head in heads if head is not None]
    heapq.heapify(not_none_heads)
    new_head: ListNode | None = None
    prev_node: ListNode | None = None
    while len(not_none_heads) > 0:
        node = heapq.heappop(not_none_heads)
        if new_head is None:
            new_head = node
        elif prev_node is not None:
            prev_node.next = node
        prev_node = node
        if node.next is not None:
            heapq.heappush(not_none_heads, node.next)
    return new_head
