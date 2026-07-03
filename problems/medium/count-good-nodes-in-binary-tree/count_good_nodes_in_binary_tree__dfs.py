r"""
>>> from count_good_nodes_in_binary_tree__dfs import goodNodes, TreeNode
>>> goodNodes(TreeNode.from_list([3, 1, 4, 3, None, 1, 5]))
4
>>> goodNodes(TreeNode.from_list([3, 3, None, 4, 2]))
3
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

    def to_list(self) -> list:
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result


def good_nodes(node, max_val):
    if node is None:
        return 0

    max_val = max(max_val, node.val)
    result = 1 if node.val >= max_val else 0
    result += good_nodes(node.left, max_val)
    result += good_nodes(node.right, max_val)

    return result


def goodNodes(root: TreeNode) -> int:
    return good_nodes(root, root.val)
