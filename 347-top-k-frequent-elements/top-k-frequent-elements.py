class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        highest = 0
        for x in nums:
            fmap[x] = fmap.get(x, 0) + 1
            highest += 1
        
        fmap2 = {} 
        for num, count in fmap.items():
            if count not in fmap2: fmap2[count] = []
            fmap2[count].append(num)

        res = []

        for i in range(highest, -1, -1):
            if i not in fmap2: continue
            for x in fmap2[i]:
                k -= 1
                res.append(x)
                if k == 0: return res
        
        return res

