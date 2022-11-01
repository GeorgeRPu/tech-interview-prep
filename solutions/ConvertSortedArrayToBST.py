"""
Problem
-------
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Solution
--------
A balanced binary tree will have the middle element of ``nums`` as the root,
the 1/4 and 3/4 elements as the left and right children, and so on. Find the
middle element of ``nums`` and divide ``nums`` into two halves. Repeat on the
left half to form the left subtree and the right half to form the right subtree.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/ConvertSortedArrayToBST.py

Test
----
>>> from ConvertSortedArrayToBST import sortedArrayToBST, tree2list
>>> root = sortedArrayToBST([-10,-3,0,5,9])
>>> tree2list(root)
[0, -3, -10, 9, 5]
>>> root = sortedArrayToBST([1,3])
>>> tree2list(root)
[3, 1]
"""

from typing import List, Optional


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    """Convert the sorted array ``nums`` to a balanced binary search tree.
    """
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


def tree2list(root: Optional[TreeNode]) -> List[int]:
    """Convert a binary tree preorder to a list.
    """
    if root is None:
        return []
    else:
        return [root.val] + tree2list(root.left) + tree2list(root.right)
