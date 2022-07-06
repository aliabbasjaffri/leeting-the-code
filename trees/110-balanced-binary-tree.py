"""
check whether the binary tree is balanced or not.
leetcode url: https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            if left == -1:
                return -1
            
            right = check(root.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1