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

from collections import deque


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

        root = cls(vals[0])
        queue = deque([root])
        children = iter(vals[1:])

        while queue:
            node = queue.popleft()
            for side in ("left", "right"):
                val = next(children, None)
                if val is not None:
                    child = cls(val)
                    setattr(node, side, child)
                    queue.append(child)

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
