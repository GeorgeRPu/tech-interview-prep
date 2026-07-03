r"""
>>> from lowest_common_ancestor_of_a_binary_search_tree__recursive import lowestCommonAncestor, TreeNode
>>> root = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
>>> lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val
6
>>> lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val
2
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


def lowestCommonAncestor(
    root: TreeNode | None,
    p: TreeNode,
    q: TreeNode,
) -> TreeNode | None:
    if root is None:
        return None
    elif max(p.val, q.val) < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
