class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fmap1 = {}

        for c in s1:
            fmap1[c] = fmap1.get(c,0) + 1

        fmap2 = {}

        l = 0
        r = 0

        while r < len(s2):
            c = s2[r]
            fmap2[c] = fmap2.get(c,0)+1
            if r < len(s1)-1:
                r += 1
                continue
            if fmap2 == fmap1:
                return True
            fmap2[s2[l]] -= 1
            if fmap2[s2[l]] == 0: del fmap2[s2[l]]
            l += 1
            r += 1

        return False
            