r"""
>>> from diameter_of_binary_tree__dfs import TreeNode, diameterOfBinaryTree
>>> diameterOfBinaryTree(TreeNode.from_list([1, 2, 3, 4, 5]))
3
>>> diameterOfBinaryTree(TreeNode.from_list([1, 2]))
1
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


def diameterOfBinaryTree(root: TreeNode | None) -> int:
    """Return the diameter of the binary tree."""
    result = 0

    def dfs(node: TreeNode | None) -> int:
        nonlocal result
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        result = max(result, left + right)
        return 1 + max(left, right)

    dfs(root)
    return result
