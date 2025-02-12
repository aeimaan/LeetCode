class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        fmap2 = {}
        fmap1= {}
        l_idx, r_idx= 0,0
        found_one = False

        min_len = 9999999
        def check_equal():
            for key in fmap2:
                if fmap1.get(key, 0) < fmap2[key]:
                    return False
            return True

        for c in t:
            fmap2[c] = 1 + fmap2.get(c,0)

        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in fmap2:
                fmap1[char] = 1 + fmap1.get(char, 0)
                while(check_equal() and l<= r):
                    found_one = True
                    if (r-l+1) < min_len:
                        l_idx = l
                        r_idx = r
                        min_len = r-l+1
                    min_len = min( min_len, r-l+1)
                    if s[l] in fmap2:
                        fmap1[s[l]] -= 1
                        if fmap1[s[l]] == 0: del fmap1[s[l]]
                    l += 1
                    

        if found_one:
            return s[l_idx:r_idx+1]
        else: return ""