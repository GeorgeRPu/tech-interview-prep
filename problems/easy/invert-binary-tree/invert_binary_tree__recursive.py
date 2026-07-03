r"""
>>> from invert_binary_tree__recursive import TreeNode, invertTree
>>> root = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
>>> invertTree(root)
TreeNode(4, TreeNode(7, TreeNode(9, None, None), TreeNode(6, None, None)), TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None)))
>>> root = TreeNode.from_list([2, 1, 3])
>>> invertTree(root)
TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None))
>>> root = TreeNode.from_list([])
>>> invertTree(root) is None
True
"""

from __future__ import annotations

from collections import deque


class TreeNode:
    """Node in a binary tree."""

    def __init__(self, val, left=None, right=None):
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

    def __repr__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def invertTree(root: TreeNode | None) -> TreeNode | None:
    """Inverts a binary tree by swapping the left and right nodes."""
    if root is None:
        return None

    root.right, root.left = root.left, root.right
    invertTree(root.right)
    invertTree(root.left)
    return root
