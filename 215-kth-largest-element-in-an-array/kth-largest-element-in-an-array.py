class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        fmap = {}
        maxNum = nums[0]
        minNum = nums[0]
        for x in nums:
            fmap[x] = 1+ fmap.get(x, 0)
            maxNum = max(maxNum, x)
            minNum = min(minNum, x)

        if minNum == maxNum: return maxNum

        for i in range(maxNum, minNum-1, -1):
            if i in fmap:
                k -= fmap[i]
                if k <= 0:
                    return i
        