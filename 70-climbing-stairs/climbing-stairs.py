class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num == n:
                return 1
            if num > n: return 0
            if num in memo:
                return memo[num]
            
            ways = dfs(num+1) + dfs(num+2)
            memo[num] = ways
            return ways
        
        return dfs(0)