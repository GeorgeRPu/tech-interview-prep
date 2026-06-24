r"""
>>> from balanced_binary_tree__dfs import TreeNode, isBalanced
>>> isBalanced(TreeNode.from_list([3, 9, 20, None, None, 15, 7]))
True
>>> isBalanced(TreeNode.from_list([1, 2, 2, 3, 3, None, None, 4, 4]))
False
>>> isBalanced(TreeNode.from_list([]))
True
"""

from __future__ import annotations


class TreeNode:
    """Node in a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, vals: list[int | None]) -> TreeNode | None:
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue = [root]
        i = 1
        while i < len(vals):
            node = queue.pop(0)
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root


def isBalanced(root: TreeNode | None) -> bool:
    """Return whether the binary tree is height-balanced."""

    def dfs(node: TreeNode | None) -> int:
        if node is None:
            return 0
        left = dfs(node.left)
        if left == -1:
            return -1
        right = dfs(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return dfs(root) != -1
