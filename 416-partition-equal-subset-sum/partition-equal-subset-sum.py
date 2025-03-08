class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            # ODD
            return False
        memo = {}
        target = sum(nums) // 2

        def dfs(idx, val):
            if val == target: return True
            if (idx, val) in memo or val > target: return False
            if idx >= len(nums): return False

            options = dfs(idx+1, val) or dfs(idx + 1, val + nums[idx])
            memo[(idx, val)] = 0
            return options
        return dfs(0, 0)
            