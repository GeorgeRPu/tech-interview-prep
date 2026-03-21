r"""
Problem
-------
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the ``root`` of a binary tree, return *the inorder traversal of
its nodes' values*.

 

**Example 1:**

.. container:: example-block

   **Input:** root = [1,null,2,3]

   **Output:** [1,3,2]

   **Explanation:**

   |image1|

**Example 2:**

.. container:: example-block

   **Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]

   **Output:** [4,2,6,5,7,1,3,9,8]

   **Explanation:**

   |image2|

**Example 3:**

.. container:: example-block

   **Input:** root = []

   **Output:** []

**Example 4:**

.. container:: example-block

   **Input:** root = [1]

   **Output:** [1]

 

**Constraints:**

- The number of nodes in the tree is in the range ``[0, 100]``.
- ``-100 <= Node.val <= 100``

 

**Follow up:** Recursive solution is trivial, could you do it
iteratively?

.. |image1| image:: https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png
.. |image2| image:: https://assets.leetcode.com/uploads/2024/08/29/tree_2.png

Solution
--------
For an inorder traversal, visit the left subtree, then the root, then the right
subtree recursively. ::

         root (2)
        /        \\
    left (1)  right (3)

Pattern
-------
Stack, Tree, Depth-First Search, Binary Tree

Code
----

.. literalinclude:: ../solutions/easy/BinaryTreeInorderTraversal.py
    :language: python
    :lines: 100-

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

from typing import List


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode | None) -> List[int]:
    """Traverse a binary tree in order from left to right.
    """
    if root is None:
        return []
    else:
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
