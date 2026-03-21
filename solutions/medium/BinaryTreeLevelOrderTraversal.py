"""
Problem
-------
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the ``root`` of a binary tree, return *the level order traversal
of its nodes' values*. (i.e., from left to right, level by level).

 

**Example 1:**

|image1|

::


   Input: root = [3,9,20,null,null,15,7]
   Output: [[3],[9,20],[15,7]]

**Example 2:**

::


   Input: root = [1]
   Output: [[1]]

**Example 3:**

::


   Input: root = []
   Output: []

 

**Constraints:**

- The number of nodes in the tree is in the range ``[0, 2000]``.
- ``-1000 <= Node.val <= 1000``

.. |image1| image:: https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

Solution
--------
A level order traversal is a breadth-first traversal of a binary tree. Track
all the nodes in the current level and add their values to the traversal. At
the same time, add their children to the next level. We finish traversing once
all the chilren are ``None``.

Pattern
-------
Tree, Breadth-First Search, Binary Tree

Code
----

.. literalinclude:: ../solutions/medium/BinaryTreeLevelOrderTraversal.py
    :language: python
    :lines: 79-

Test
----
>>> from BinaryTreeLevelOrderTraversal import levelOrder, TreeNode
>>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
>>> levelOrder(root)
[[3], [9, 20], [15, 7]]
>>> root = TreeNode(1)
>>> levelOrder(root)
[[1]]
>>> root = None
>>> levelOrder(root)
[]
"""


from typing import List


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode | None) -> List[List[int]]:
    """Return the level order traversal of a binary tree.
    """
    traversal = []
    level = [root] if root is not None else []
    while len(level) > 0:
        values = []
        next_level = []
        for node in level:
            values.append(node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        traversal.append(values)
        level = next_level

    return traversal
