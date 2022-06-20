"""
inverts a binary tree and returns the root.
leetcode url: https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postOrderTraversal(tree: Optional[TreeNode]) -> Optional[TreeNode]:
            if not tree:
                return None
            right = postOrderTraversal(tree.right)
            left = postOrderTraversal(tree.left)
            tree.left = right
            tree.right = left
            return tree
        return postOrderTraversal(root)