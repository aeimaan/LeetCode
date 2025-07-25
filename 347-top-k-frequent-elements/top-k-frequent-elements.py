class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        res = []
        for x in nums:
            fmap[x] = fmap.get(x, 0 ) + 1
        fmap2 = {}
        for num, count in fmap.items():
            if count not in fmap2:
                fmap2[count] = []
            fmap2[count].append(num)
        for i in range(len(nums), -1, -1):
            if i in fmap2:
                for x in fmap2[i]:
                    res.append(x)
                    k -=1 
                    if k == 0: return res
        return res
