r"""
>>> from binary_tree_level_order_traversal__approach_1 import levelOrder, TreeNode
>>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
>>> levelOrder(root)
[[3], [9, 20], [15, 7]]
>>> root = TreeNode(1)
>>> levelOrder(root)
[[1]]
>>> root = None
>>> levelOrder(root)
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


def levelOrder(root: TreeNode | None) -> List[List[int]]:
    """Return the level order traversal of a binary tree.
    """
    traversal = []
    level = [root] if root is not None else []
    while len(level) > 0:
        values = []
        next_level = []
        for node in level:
            values.append(node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        traversal.append(values)
        level = next_level

    return traversal
