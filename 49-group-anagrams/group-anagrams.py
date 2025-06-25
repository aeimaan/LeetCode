class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fmap = {}
        for s in strs:
            tmp = sorted(s)
            tmp = "".join(tmp)
            if tmp not in fmap:
                fmap[tmp] = []
            fmap[tmp].append(s)
        return list(fmap.values() )