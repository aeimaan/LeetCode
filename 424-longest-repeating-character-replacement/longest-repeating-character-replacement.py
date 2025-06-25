class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fmap = {}
        res = 0
        max_char = 0
        l = 0 

        for r in range(len(s)):
            fmap[s[r]] = fmap.get(s[r], 0 ) + 1
            max_char = max(max_char, fmap[s[r]])
            if (r-l+1) - max_char > k:
                fmap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res