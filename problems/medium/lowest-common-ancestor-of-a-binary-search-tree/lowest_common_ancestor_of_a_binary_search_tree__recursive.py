r"""
>>> from lowest_common_ancestor_of_a_binary_search_tree__recursive import lowestCommonAncestor, TreeNode
>>> root = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
>>> lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val
6
>>> lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val
2
"""

from __future__ import annotations

from typing import List


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, vals: List[int | None]) -> TreeNode | None:
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


def lowestCommonAncestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if root is None:
        return None
    elif max(p.val, q.val) < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
