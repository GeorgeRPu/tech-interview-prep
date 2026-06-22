r"""
>>> from convert_sorted_array_to_binary_search_tree__recursive import sortedArrayToBST, tree2list
>>> root = sortedArrayToBST([-10, -3, 0, 5, 9])
>>> tree2list(root)
[0, -3, -10, 9, 5]
>>> root = sortedArrayToBST([1, 3])
>>> tree2list(root)
[3, 1]
"""

from typing import List


class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> TreeNode | None:
    """Convert the sorted array ``nums`` to a balanced binary search tree.
    """
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


def tree2list(root: TreeNode | None) -> List[int]:
    """Convert a binary tree preorder to a list.
    """
    if root is None:
        return []
    else:
        return [root.val] + tree2list(root.left) + tree2list(root.right)
