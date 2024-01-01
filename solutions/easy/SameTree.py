"""
Problem
-------
https://leetcode.com/problems/same-tree/

Solution
--------
Two tree are equal if and only if their roots are equal and their left and
right subtrees are equal. To check if the left and right subtrees are equal, we
can use recursion. If both roots are ``None``, then they are equal. If one is
``None`` and the other is not, then they are not equal.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/SameTree.py

.. literalinclude:: ../solutions/easy/SameTree.py
    :language: python
    :lines: 38-

Test
----
>>> from SameTree import TreeNode, isSameTree
>>> root1 = TreeNode(1, TreeNode(2), TreeNode(3))
>>> root2 = TreeNode(1, TreeNode(2), TreeNode(3))
>>> isSameTree(root1, root2)
True
>>> root1 = TreeNode(1, None, TreeNode(2))
>>> root2 = TreeNode(1, TreeNode(2), None)
>>> isSameTree(root1, root2)
False
>>> root1 = TreeNode(1, TreeNode(2), TreeNode(1))
>>> root2 = TreeNode(1, TreeNode(1), TreeNode(2))
>>> isSameTree(root1, root2)
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


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Checks if two binary trees with roots ``p`` and ``q`` are equal.
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
