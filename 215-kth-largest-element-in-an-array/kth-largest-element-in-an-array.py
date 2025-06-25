class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        fmap = {}
        minn = nums[0]
        maxx = nums[0]
        count = 0
        for x in nums:
            fmap[x] = fmap.get(x, 0) + 1
            minn = min(minn, x)
            maxx = max(maxx, x)
        if maxx == minn: return maxx
        for i in range(maxx, minn-1, -1):
            if i in fmap:
                count += fmap[i]
                if k <= count: return i
