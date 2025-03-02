class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        n = len(nums)
        firstSum = helper(nums[0:n-1])
        secondSum = helper(nums[1:])
        return max(firstSum, secondSum)


def helper(nums: List[int]) -> int:
    if len(nums) <= 2: return max(nums) 
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
    return dp[n-1]