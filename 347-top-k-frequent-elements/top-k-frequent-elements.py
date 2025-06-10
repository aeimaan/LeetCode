class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        highest = 0
        for x in nums:
            fmap[x] = fmap.get(x, 0) + 1
            highest = max(highest, fmap[x])
        
        fmap2 = {i+1:[] for i in range(len(nums))} 
        for num, count in fmap.items():
            fmap2[count].append(num)

        res = []

        for i in range(highest, -1, -1):
            for x in fmap2[i]:
                k -= 1
                res.append(x)
                if k == 0: return res
        
        return res

