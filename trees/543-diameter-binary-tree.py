"""
calculate the width of binary tree
leetcode url: https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        
        def measureDiameter(tree: Optional[TreeNode]) -> int:
            if not tree:
                return 0
            
            left_side = measureDiameter(tree.left)
            right_side = measureDiameter(tree.right)
            
            self.diameter = max(self.diameter, left_side + right_side)
            
            return max(left_side, right_side) + 1
        
        measureDiameter(root)
        return self.diameter
    