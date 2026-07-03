r"""
>>> from subtree_of_another_tree__dfs import TreeNode, isSubtree
>>> isSubtree(TreeNode.from_list([3, 4, 5, 1, 2]), TreeNode.from_list([4, 1, 2]))
True
>>> root = TreeNode.from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
>>> isSubtree(root, TreeNode.from_list([4, 1, 2]))
False
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


def isSubtree(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    """Return whether ``subRoot`` is a subtree of ``root``."""
    if subRoot is None:
        return True
    if root is None:
        return False
    if _same_tree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def _same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return (
        p.val == q.val
        and _same_tree(p.left, q.left)
        and _same_tree(p.right, q.right)
    )
