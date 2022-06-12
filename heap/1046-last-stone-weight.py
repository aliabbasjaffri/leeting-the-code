"""
takes the largest stones from a heap and returns the last one by the end
leetcode url: https://leetcode.com/problems/last-stone-weight/
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first_stone  = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)
            
            if first_stone == second_stone:
                continue
            else:
                third_stone = abs(abs(first_stone) - abs(second_stone))
                third_stone *= -1
                heapq.heappush(stones, third_stone)
        
        return abs(stones[0]) if len(stones) == 1 else 0