"""
calculating the maximum robbery amount
leetcode url: https://leetcode.com/problems/house-robber/
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        odd_houses_rob_amount = 0
        even_houses_rob_amount = 0
        
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even_houses_rob_amount += nums[i]
            else:
                odd_houses_rob_amount += nums[i]
        
        return max(odd_houses_rob_amount, even_houses_rob_amount)