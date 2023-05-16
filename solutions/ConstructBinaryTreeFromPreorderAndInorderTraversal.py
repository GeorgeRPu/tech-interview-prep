"""
Problem
-------
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Solution
--------
Since preorder traversal prints the root node first, we extract the value
``val`` of the root node from the tip of ``preorder``. The same value ``val``
divides ``inorder`` into two parts: the left subtree and the right subtree. We
can then recursively build the left subtree by using the rest of the
``preorder`` and the left half of ``inorder``. Once the left subtree is built,
we build the right subtree by using the rest of the ``preorder`` from buliding
the left subtree and the right half of ``inorder``.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/AddTwoNumbers.py

.. literalinclude:: ../solutions/AddTwoNumbers.py
    :language: python
    :lines: 43-

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

from typing import List, Optional, Tuple


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


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Build a binary tree from its preorder and inorder traversals.
    """
    return build_tree(preorder, inorder)[0]


def build_tree(preorder: List[int], inorder: List[int]) -> Tuple[Optional[TreeNode], List[int]]:
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
