class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            # ODD
            return False
        memo = {}
        target = sum(nums) // 2

        def dfs(idx, val):
            if val == target: return True
            if (idx, val) in memo: return memo[(idx, val)]
            if idx >= len(nums) or val > target: return False

            options = dfs(idx+1, val) or dfs(idx + 1, val + nums[idx])
            memo[(idx, val)] = options
            return options
        return dfs(0, 0)
            