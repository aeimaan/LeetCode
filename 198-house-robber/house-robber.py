class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        mem = [0] * len(nums)
        maxMoney = max(nums[0], nums[1])
        mem[1] = maxMoney
        mem[0] = nums[0]
        
        for i in range(2, len(nums)):
            num = nums[i]
            mem[i] = max( num+mem[i-2], mem[i-1] )
        return mem[-1]
