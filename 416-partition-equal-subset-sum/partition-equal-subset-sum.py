class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            # ODD
            return False
        memo = set()
        memo.add(0)
        target = sum(nums) // 2
        n = len(nums)

        for i in range(n-1, -1, -1):
            tmp = set()
            for x in memo:
                if nums[i] + x == target:
                    return True
                else:
                    tmp.add(nums[i] + x)
                    tmp.add(x)
            memo = tmp
        return False
        
            