class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        dp = [1] * n
        res = 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i]  < nums[j]: # Can add to this subseq
                    dp[i] = max( dp[i] ,  1+ dp[j])
                res = max(dp[i], res)
        return res