from __future__ import annotations

__doc__ = """
Problem
-------

Solution
--------

Code
----

Test
----
>>> from InvertBinaryTree import TreeNode, invertTree
>>> root = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
>>> invertTree(root)
TreeNode(4, TreeNode(7, TreeNode(9, None, None), TreeNode(6, None, None)), TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None)))
>>> root = TreeNode.from_list([2, 1, 3])
>>> invertTree(root)
TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None))
>>> root = TreeNode.from_list([])
>>> invertTree(root) is None
True
"""

from typing import List, Optional


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, list: List[int]) -> Optional[TreeNode]:
        """Creates a binary tree from a list of integers pre-order.
        """
        if len(list) == 0:
            return None

        root = TreeNode(list[0])
        queue = [root]
        i = 1
        while i < len(list):
            node = queue.pop()
            if list[i] is not None:
                node.left = TreeNode(list[i])
                queue.insert(0, node.left)
            i += 1
            if i < len(list) and list[i] is not None:
                node.right = TreeNode(list[i])
                queue.insert(0, node.right)
            i += 1
        return root

    def __repr__(self) -> str:
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Inverts a binary tree by swapping the left and right nodes.
    """
    if root is None:
        return None

    root.right, root.left = root.left, root.right
    invertTree(root.right)
    invertTree(root.left)
    return root
