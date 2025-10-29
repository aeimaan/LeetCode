class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1] * len(nums)
        left = [1] * len(nums)
        tmp = 1

        for i in range(len(nums)):
            left[i] = tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            right[i] = tmp
            tmp *= nums[i]
        
        for i in range(len(nums)):
            right[i] *= left[i]
        return right