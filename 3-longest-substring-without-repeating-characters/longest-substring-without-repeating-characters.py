class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fmap = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in fmap:
                fmap.remove(s[l])
                l += 1
            
            fmap.add(s[r])    
            max_len = max(max_len, r-l+1)

        return max_len

        