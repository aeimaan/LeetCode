class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fmap = set()

        l = 0
        res = 0

        for r in range(len(s)):
            c = s[r] 
            if c not in fmap:
                fmap.add(c)
            else:
                while c in fmap and l<= r:
                    fmap.remove(s[l])
                    l += 1
                fmap.add(c)
            
            res = max(res, r-l+1)
        return res
        