class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            if ( i != 0 and nums[i] == nums[i-1]):
                continue
            twoSum(nums, i+1, len(nums)-1, -nums[i], res)
        return list(res)
            

def twoSum(nums, l, r, target, res):
    while l < r:
        y = nums[l]
        z = nums[r]
        cur = z+y
        if cur > target: r -= 1
        elif cur < target: l += 1
        else:
            # res.append([-target, y, z])
            res.add((-target, y, z))
            l += 1
            r -= 1