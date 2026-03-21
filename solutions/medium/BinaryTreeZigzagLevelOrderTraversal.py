"""
Problem
-------
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the ``root`` of a binary tree, return *the zigzag level order
traversal of its nodes' values*. (i.e., from left to right, then right
to left for the next level and alternate between).

 

**Example 1:**

|image1|

::


   Input: root = [3,9,20,null,null,15,7]
   Output: [[3],[20,9],[15,7]]

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
- ``-100 <= Node.val <= 100``

.. |image1| image:: https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

Solution
--------
The solution is the same as level order traversal, but reverse the order of the
values if the depth is odd, starting at 0. The reason we reverse the order of
the values instead of the order of the nodes is because then nodes added to the
next level will also be reversed.

Pattern
-------
Tree, Breadth-First Search, Binary Tree

Code
----

.. literalinclude:: ../solutions/medium/BinaryTreeZigzagLevelOrderTraversal.py
    :language: python
    :lines: 77-

Test
----
>>> from BinaryTreeZigzagLevelOrderTraversal import zigzagLevelOrder, TreeNode
>>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
>>> zigzagLevelOrder(root)
[[3], [20, 9], [15, 7]]
>>> zigzagLevelOrder(TreeNode(1))
[[1]]
>>> zigzagLevelOrder(None)
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


def zigzagLevelOrder(root: TreeNode | None) -> List[List[int]]:
    """Traverse a binary tree in level order but zigzaging from left to right
    and right to left.
    """
    traversal = []
    level = [root] if root is not None else []
    depth = 0
    while len(level) > 0:
        values = []
        next_level = []
        for node in level:
            values.append(node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        if depth % 2 == 1:
            values = values[::-1]
        traversal.append(values)
        level = next_level
        depth += 1

    return traversal
