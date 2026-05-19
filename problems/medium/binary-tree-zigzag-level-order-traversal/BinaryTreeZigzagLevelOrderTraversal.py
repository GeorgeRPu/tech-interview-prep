r"""
>>> from BinaryTreeZigzagLevelOrderTraversal import zigzagLevelOrder, TreeNode
>>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
>>> zigzagLevelOrder(root)
[[3], [20, 9], [15, 7]]
>>> zigzagLevelOrder(TreeNode(1))
[[1]]
>>> zigzagLevelOrder(None)
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


def zigzagLevelOrder(root: TreeNode | None) -> List[List[int]]:
    """Traverse a binary tree in level order but zigzaging from left to right
    and right to left.
    """
    traversal = []
    level = [root] if root is not None else []
    depth = 0
    while len(level) > 0:
        values = []
        next_level = []
        for node in level:
            values.append(node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        if depth % 2 == 1:
            values = values[::-1]
        traversal.append(values)
        level = next_level
        depth += 1

    return traversal
