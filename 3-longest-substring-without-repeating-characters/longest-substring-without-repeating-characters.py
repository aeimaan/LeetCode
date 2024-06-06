class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fmap = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            char = s[r]
            fmap[char] = fmap.get(char, 0) + 1

            while fmap[char] > 1:
                fmap[ s[l] ] -= 1
                if fmap[s[l]] == 0:
                    del fmap[s[l]]
                l += 1
                
            max_len = max(max_len, r-l+1)

        return max_len

        