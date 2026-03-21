"""
Problem
-------
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays ``preorder`` and ``inorder`` where ``preorder``
is the preorder traversal of a binary tree and ``inorder`` is the
inorder traversal of the same tree, construct and return *the binary
tree*.

 

**Example 1:**

|image1|

::


   Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
   Output: [3,9,20,null,null,15,7]

**Example 2:**

::


   Input: preorder = [-1], inorder = [-1]
   Output: [-1]

 

**Constraints:**

- ``1 <= preorder.length <= 3000``
- ``inorder.length == preorder.length``
- ``-3000 <= preorder[i], inorder[i] <= 3000``
- ``preorder`` and ``inorder`` consist of **unique** values.
- Each value of ``inorder`` also appears in ``preorder``.
- ``preorder`` is **guaranteed** to be the preorder traversal of the
  tree.
- ``inorder`` is **guaranteed** to be the inorder traversal of the tree.

.. |image1| image:: https://assets.leetcode.com/uploads/2021/02/19/tree.jpg

Solution
--------
Since preorder traversal prints the root node first, we extract the value
``val`` of the root node from the tip of ``preorder``. The same value ``val``
divides ``inorder`` into two parts: the left subtree and the right subtree. We
can then recursively build the left subtree by using the rest of the
``preorder`` and the left half of ``inorder``. Once the left subtree is built,
we build the right subtree by using the rest of the ``preorder`` from buliding
the left subtree and the right half of ``inorder``.

Pattern
-------
Array, Hash Table, Divide and Conquer, Tree, Binary Tree

Code
----

.. literalinclude:: ../solutions/medium/ConstructBinaryTreeFromPreorderAndInorderTraversal.py
    :language: python
    :lines: 86-

Test
----
>>> from ConstructBinaryTreeFromPreorderAndInorderTraversal import buildTree
>>> preorder = [3, 9, 20, 15, 7]
>>> inorder = [9, 3, 15, 20, 7]
>>> root = buildTree(preorder, inorder)
>>> root.preorder()
[3, 9, 20, 15, 7]
>>> root.inorder()
[9, 3, 15, 20, 7]
>>> preorder = [-1]
>>> inorder = [-1]
>>> root = buildTree(preorder, inorder)
>>> root.preorder()
[-1]
>>> root.inorder()
[-1]
"""

from typing import List, Tuple


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def preorder(self):
        preorder = [self.val]
        if self.left is not None:
            preorder.extend(self.left.preorder())
        if self.right is not None:
            preorder.extend(self.right.preorder())
        return preorder

    def inorder(self):
        inorder = [self.val]
        if self.left is not None:
            inorder = self.left.inorder() + inorder
        if self.right is not None:
            inorder.extend(self.right.inorder())
        return inorder


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode | None:
    """Build a binary tree from its preorder and inorder traversals.
    """
    return build_tree(preorder, inorder)[0]


def build_tree(preorder: List[int], inorder: List[int]) -> Tuple[TreeNode | None, List[int]]:
    """Recursively build a binary tree from part of its preorder and inorder
    traversals.
    """
    if len(inorder) == 0:
        return None, preorder

    val = preorder[0]
    idx = inorder.index(val)

    root = TreeNode(val)
    left_child, preorder = build_tree(preorder[1:], inorder[:idx])
    right_child, preorder = build_tree(preorder, inorder[idx + 1:])

    root.left = left_child
    root.right = right_child

    return root, preorder
