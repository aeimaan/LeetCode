class Solution:
    def climbStairs(self, n: int) -> int:
        state = [0] * (n+1) 
        
        for i in range(n+1):
            if i <= 1:
                state[i] = 1
                continue
            state[i] = state[i-1] + state[i-2]

        return state[-1]



        # memo = {}

        # def dfs(num):
        #     if num == n:
        #         return 1
        #     if num > n: return 0
        #     if num in memo:
        #         return memo[num]
            
        #     ways = dfs(num+1) + dfs(num+2)
        #     memo[num] = ways
        #     return ways
        
        # return dfs(0)