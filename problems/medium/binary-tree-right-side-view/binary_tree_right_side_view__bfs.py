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
    """Node in a binary tree.
    """

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
