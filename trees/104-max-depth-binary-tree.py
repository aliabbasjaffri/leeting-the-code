"""
calculate the maximum depth of binary tree
leetcode url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def measureTreeDepth(root: Optional[TreeNode], height: int) -> None:
            if root:
                measureTreeDepth(root.left, height + 1)
                if height > self.max_depth:
                    self.max_depth = height
                measureTreeDepth(root.right, height + 1)
        if root:
            measureTreeDepth(root, 1)
        return self.max_depth