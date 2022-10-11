"""
Problem
-------
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Solution
--------
If ``root`` is ``None``, the height of a tree is 0. Otherwise, the height of a
tree is the 1 plus the maximum of the heights of the left and right subtrees.

Test
----
>>> from MaximumDepthOfBinaryTree import TreeNode, maxDepth
>>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
>>> maxDepth(root)
3
>>> root = TreeNode(1, None, TreeNode(2))
>>> maxDepth(root)
2
"""

from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
