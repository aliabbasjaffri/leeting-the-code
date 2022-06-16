"""
fibonacci sequence to calculate the number of ways to climb stairs
leetcode url: https://leetcode.com/problems/climbing-stairs/
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {}
        def stair_steps(i: int, n: int) -> int:
            if i > n:
                return 0
            elif i == n:
                return 1
            elif i in steps and steps[i] > 0:
                return steps[i]
            else:
                steps[i] = stair_steps(i+1, n) + stair_steps(i+2, n)
                return steps[i]
        return stair_steps(0, n)