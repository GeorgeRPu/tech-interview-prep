r"""
Problem
-------
https://leetcode.com/problems/invert-binary-tree/description/

Given the ``root`` of a binary tree, invert the tree, and return *its
root*.

 

**Example 1:**

|image1|

::


   Input: root = [4,2,7,1,3,6,9]
   Output: [4,7,2,9,6,3,1]

**Example 2:**

|image2|

::


   Input: root = [2,1,3]
   Output: [2,3,1]

**Example 3:**

::


   Input: root = []
   Output: []

 

**Constraints:**

- The number of nodes in the tree is in the range ``[0, 100]``.
- ``-100 <= Node.val <= 100``

.. |image1| image:: https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg

Solution
--------
Observe that when we invert the tree, we can do it in 2 steps:
1. Swap the left and right children of the root.
2. Invert the left and right subtrees.
This gives a recursive algorithm to invert a binary tree.

Pattern
-------
Tree, Depth-First Search, Breadth-First Search, Binary Tree

Code
----

.. literalinclude:: ../solutions/easy/InvertBinaryTree.py
    :language: python
    :lines: 80-

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
from __future__ import annotations

from typing import List


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, list: List[int]) -> TreeNode | None:
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


def invertTree(root: TreeNode | None) -> TreeNode | None:
    """Inverts a binary tree by swapping the left and right nodes.
    """
    if root is None:
        return None

    root.right, root.left = root.left, root.right
    invertTree(root.right)
    invertTree(root.left)
    return root
