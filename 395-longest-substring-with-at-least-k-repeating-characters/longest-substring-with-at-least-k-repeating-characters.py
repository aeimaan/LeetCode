class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s)<k:
            return 0
        if k == 1: return len(s)

        fmap = {}
        l = 0
        for c in s:
            fmap[c] = fmap.get(c, 0) + 1

        while l < len(s) and fmap[s[l]]>= k:
            l += 1

        if l >= len(s) - 1:
            return l
        
        left_str = self.longestSubstring( s[0:l] , k)
        while l < len(s) and fmap[s[l]] < k: l += 1
        right_str = self.longestSubstring(s[l:], k)
        return max(left_str, right_str)
