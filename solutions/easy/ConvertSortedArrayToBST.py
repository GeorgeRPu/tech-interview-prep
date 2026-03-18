"""
Problem
-------
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array ``nums`` where the elements are sorted in
**ascending order**, convert *it to a* height-balanced *binary search
tree*.

 

**Example 1:**

|image1|

::


   Input: nums = [-10,-3,0,5,9]
   Output: [0,-3,9,-10,null,5]
   Explanation: [0,-10,5,null,-3,null,9] is also accepted:

**Example 2:**

|image2|

::


   Input: nums = [1,3]
   Output: [3,1]
   Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

 

**Constraints:**

- ``1 <= nums.length <= 10``\ :sup:```4```
- ``-10``\ :sup:```4```\ ``<= nums[i] <= 10``\ :sup:```4```
- ``nums`` is sorted in a **strictly increasing** order.

.. |image1| image:: https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2021/02/18/btree.jpg

Solution
--------
A balanced binary tree will have the middle element of ``nums`` as the root,
the 1/4 and 3/4 elements as the left and right children, and so on. Find the
middle element of ``nums`` and divide ``nums`` into two halves. Repeat on the
left half to form the left subtree and the right half to form the right subtree.

Code
----

.. literalinclude:: ../solutions/easy/ConvertSortedArrayToBST.py
    :language: python
    :lines: 70-

Test
----
>>> from ConvertSortedArrayToBST import sortedArrayToBST, tree2list
>>> root = sortedArrayToBST([-10, -3, 0, 5, 9])
>>> tree2list(root)
[0, -3, -10, 9, 5]
>>> root = sortedArrayToBST([1, 3])
>>> tree2list(root)
[3, 1]
"""

from typing import List


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> TreeNode | None:
    """Convert the sorted array ``nums`` to a balanced binary search tree.
    """
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


def tree2list(root: TreeNode | None) -> List[int]:
    """Convert a binary tree preorder to a list.
    """
    if root is None:
        return []
    else:
        return [root.val] + tree2list(root.left) + tree2list(root.right)
