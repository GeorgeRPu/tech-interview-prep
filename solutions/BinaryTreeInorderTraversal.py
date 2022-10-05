"""
Problem
-------
https://leetcode.com/problems/binary-tree-inorder-traversal/

Solution
--------
For an inorder traversal, visit the left subtree, then the root, then the right
subtree recursively. ::

         root (2)
        /        \\
    left (1)  right (3)

Test
----
>>> from BinaryTreeInorderTraversal import inorderTraversal, TreeNode
>>> root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
>>> inorderTraversal(root)
[1, 3, 2]
>>> root = None
>>> inorderTraversal(root)
[]
>>> root = TreeNode(1)
>>> inorderTraversal(root)
[1]
"""

from typing import List, Optional


class TreeNode:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    """
    if root is None:
        return []
    else:
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
