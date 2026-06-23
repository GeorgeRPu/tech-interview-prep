r"""
>>> from count_good_nodes_in_binary_tree__dfs import goodNodes, TreeNode
>>> goodNodes(TreeNode.from_list([3, 1, 4, 3, None, 1, 5]))
4
>>> goodNodes(TreeNode.from_list([3, 3, None, 4, 2]))
3
"""

from __future__ import annotations


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
