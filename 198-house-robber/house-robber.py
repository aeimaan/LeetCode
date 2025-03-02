class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) <= 2: return max(nums) 
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])

        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        # return dp[n-1]


        # Top Down Approach
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            robbed = max(dfs(i+1) , nums[i] + dfs(i+2))
            memo[i] = robbed
            return robbed
        
        return dfs(0)


