r"""
Problem
-------
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the ``root`` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the
longest path from the root node down to the farthest leaf node.

 

**Example 1:**

|image1|

::


   Input: root = [3,9,20,null,null,15,7]
   Output: 3

**Example 2:**

::


   Input: root = [1,null,2]
   Output: 2

 

**Constraints:**

- The number of nodes in the tree is in the range
  ``[0, 10``\ :sup:```4```\ ``]``.
- ``-100 <= Node.val <= 100``

.. |image1| image:: https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg

Solution
--------
If ``root`` is ``None``, the height of a tree is 0. Otherwise, the height of a
tree is the 1 plus the maximum of the heights of the left and right subtrees.

Pattern
-------
Tree, Depth-First Search, Breadth-First Search, Binary Tree

Code
----

.. literalinclude:: ../solutions/easy/MaximumDepthOfBinaryTree.py
    :language: python
    :lines: 69-

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


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode | None) -> int:
    """Find the maximum depth or total height of a binary tree.
    """
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
