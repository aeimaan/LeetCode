class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) < k : return 0     #nothing can be made here
        if k <= 1: return len(s)                    #everything valid

        fmap = {}

        for c in s:
            fmap[c] = 1 + fmap.get(c, 0)

        l = 0
        while l < len(s) and fmap[s[l]] >= k:
            l += 1
        
        if l >= len(s)-1:       #Whole string is valid
            print(len(s) , l)
            return l

        left_str = self.longestSubstring( s[0:l], k )
        while l<len(s) and fmap[s[l]] < k: l += 1
        right_str = 0
        if l < len(s):
            right_str = self.longestSubstring(s[l:], k)
        return max(left_str, right_str)