r"""
>>> from same_tree__approach_1 import TreeNode, isSameTree
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
