class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:return 0

        length = 1
        LI = [1]* len(nums)

        for j in range(len(nums)-1, -1, -1):
            for i in range(j+1, len(nums)):
                if nums[j] < nums[i]:
                    LI[j] = max(LI[j], 1 + LI[i])
                    length = max(length, LI[j])
        
        return length