r"""
>>> from symmetric_tree__recursive import TreeNode, isSymmetric
>>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
>>> isSymmetric(root)
True
>>> root = TreeNode(1, TreeNode(2, None, TreeNode(2)), TreeNode(2, None, TreeNode(2)))
>>> isSymmetric(root)
False
"""




class TreeNode:
    """Node in a binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode | None) -> bool:
    """Returns whether a binary tree is symmetric.
    """
    if root is None:
        return True
    else:
        return check_subtrees(root.left, root.right)


def check_subtrees(left: TreeNode | None, right: TreeNode | None) -> bool:
    """Returns whether the left and right subtrees are mirror images of each
    other.
    """
    if left is right is None:
        return True
    elif left is None and right is not None:
        return False
    elif left is not None and right is None:
        return False
    elif left.val != right.val:
        return False
    else:
        return check_subtrees(left.left, right.right) and check_subtrees(left.right, right.left)
