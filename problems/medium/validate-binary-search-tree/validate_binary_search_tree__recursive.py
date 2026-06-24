r"""
>>> from validate_binary_search_tree__recursive import isValidBST, TreeNode
>>> isValidBST(TreeNode.from_list([2, 1, 3]))
True
>>> isValidBST(TreeNode.from_list([5, 1, 4, None, None, 3, 6]))
False
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


def is_valid_bst(node, left, right):
    if node is None:
        return True

    if not (left < node.val < right):
        return False

    return is_valid_bst(node.left, left, node.val) and is_valid_bst(
        node.right, node.val, right
    )


def isValidBST(root: TreeNode | None) -> bool:
    return is_valid_bst(root, float("-inf"), float("inf"))
