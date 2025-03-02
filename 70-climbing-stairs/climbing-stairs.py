class Solution:
    def climbStairs(self, n: int) -> int:
        state = [0] * (n+1) 
        
        for i in range(n+1):
            if i <= 2:
                state[i] = i
                continue
            state[i] = state[i-1] + state[i-2]
            print(state[i-1], state[i-2], state[i])

        print(state)
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