r"""
>>> from kth_smallest_element_in_a_bst__inorder_traversal import kthSmallest, TreeNode
>>> kthSmallest(TreeNode.from_list([3, 1, 4, None, 2]), 1)
1
>>> kthSmallest(TreeNode.from_list([5, 3, 6, 2, 4, None, None, 1]), 3)
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


def kthSmallest(root: TreeNode | None, k: int) -> int:
    stack = deque()
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val

        curr = curr.right
