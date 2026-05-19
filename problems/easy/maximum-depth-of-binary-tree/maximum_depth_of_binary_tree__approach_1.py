r"""
>>> from maximum_depth_of_binary_tree__approach_1 import TreeNode, maxDepth
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
