r"""
>>> from binary_tree_right_side_view__bfs import rightSideView, TreeNode
>>> rightSideView(TreeNode.from_list([1, 2, 3, None, 5, None, 4]))
[1, 3, 4]
>>> rightSideView(TreeNode.from_list([1, None, 3]))
[1, 3]
>>> rightSideView(None)
[]
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


def rightSideView(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    view = []

    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

        if len(queue) == 0 or level < queue[0][1]:
            view.append(node.val)

    return view
