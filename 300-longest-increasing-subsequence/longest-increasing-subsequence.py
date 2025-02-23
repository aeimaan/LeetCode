class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        length = 1
        memory = [1] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]: #Can add to a sub seq
                    memory[i] = max(memory[i] , 1 + memory[j])
                
                length = max(length, memory[i])

        return length