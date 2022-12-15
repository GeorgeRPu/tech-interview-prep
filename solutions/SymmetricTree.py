"""
Problem
-------
https://leetcode.com/problems/symmetric-tree/

Solution
--------
Starting at the root, observe that it does not affect the symmetry of the tree.
Only the left and right subtrees with roots ``left = root.left`` and
``right = root.right`` do. We need to check if the left subtree is a mirror
image of the right. This is true if and only if ``left.val == right.val`` and
the subtree of``left.left`` is a mirror image of ``right.right`` and the
subtree of ``left.right`` is a mirror image of ``right.left``. Checking whether
the further subtrees are mirror images of each other can be solved using
recursion, until both children are ``null``. ::

                         root
               /                    \\
            left-                   right-
        /         \\             /          \\
    left.left+ left.right* right.left+ right.right*

The - nodes should be equal in value, while the + subtrees, and * subtrees should be
mirror images.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/SymmetricTree.py

.. literalinclude:: ../solutions/SymmetricTree.py
    :language: python
    :lines: 46-

Test
----
>>> from SymmetricTree import TreeNode, isSymmetric
>>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
>>> isSymmetric(root)
True
>>> root = TreeNode(1, TreeNode(2, None, TreeNode(2)), TreeNode(2, None, TreeNode(2)))
>>> isSymmetric(root)
False
"""


from typing import Optional


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """Returns whether a binary tree is symmetric.
    """
    if root is None:
        return True
    else:
        return check_subtrees(root.left, root.right)


def check_subtrees(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    """Returns whether the left and right subtrees are mirror images of each
    other.
    """
    if left is right is None:
        return True
    elif left is None and right is not None:
        return False
    elif left is not None and right is None:
        return False
    elif left.val != right.val:
        return False
    else:
        return check_subtrees(left.left, right.right) and check_subtrees(left.right, right.left)
