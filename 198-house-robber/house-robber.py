class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1: return max(nums)

        memory = [0] * len(nums)
        memory[0] = nums[0] 
        memory[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            # can either rob current house pluse i - 2
            # or not rob current house so continue i-1
            # Choose by max
            memory[i] = max(nums[i] + memory[i-2], memory[i-1])

        return memory[-1]