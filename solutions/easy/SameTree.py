"""
Problem
-------
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees ``p`` and ``q``, write a function to
check if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

 

**Example 1:**

|image1|

::


   Input: p = [1,2,3], q = [1,2,3]
   Output: true

**Example 2:**

|image2|

::


   Input: p = [1,2], q = [1,null,2]
   Output: false

**Example 3:**

|image3|

::


   Input: p = [1,2,1], q = [1,1,2]
   Output: false

 

**Constraints:**

- The number of nodes in both trees is in the range ``[0, 100]``.
- ``-10``\ :sup:```4```\ ``<= Node.val <= 10``\ :sup:```4```

.. |image1| image:: https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg
.. |image2| image:: https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg
.. |image3| image:: https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg

Solution
--------
Two tree are equal if and only if their roots are equal and their left and
right subtrees are equal. To check if the left and right subtrees are equal, we
can use recursion. If both roots are ``None``, then they are equal. If one is
``None`` and the other is not, then they are not equal.

Code
----

.. literalinclude:: ../solutions/easy/SameTree.py
    :language: python
    :lines: 88-

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



class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Checks if two binary trees with roots ``p`` and ``q`` are equal.
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
