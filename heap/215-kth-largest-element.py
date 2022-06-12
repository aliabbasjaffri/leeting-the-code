"""
return kth largest element from the array
leetcode url: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        
        heapq.heapify(nums)
        
        for i in range(target):
            heapq.heappop(nums)
        
        return nums[0]