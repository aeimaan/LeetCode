class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        fmap = set()
        checked = set()
        count = 0
        for x in nums:
            fmap.add(x)
        for x in fmap:
            if x-1 not in fmap:
                tmp = x
                while tmp + 1 in fmap:
                    tmp += 1
                count = max(count, tmp-x +1)
            checked.add(x)
        return count