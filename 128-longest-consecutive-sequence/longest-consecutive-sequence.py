class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        fmap = set()
        checked = set()
        maxx = minn = nums[0]
        res = 0

        for x in nums:
            fmap.add(x)
            maxx = max(maxx, x)
            minn = min(minn, x)
        
        tmp = 0
        for i in nums:
            if i + 1 not in fmap and i in fmap and i not in checked:
                # have a number thats the start of the chain
                checked.add(i)
                k = i
                while k - 1 in fmap:
                    k -= 1
                res = max(res, i - k+1)
        return res