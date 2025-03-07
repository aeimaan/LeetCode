class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = 0
        maxLen = 0
        n = len(s)
        dp = [ [False]*n for i in range(n) ]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                curLen = j-i+1
                if (s[i] == s[j]) and (curLen <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if curLen > maxLen:
                        maxLen = curLen
                        l = i
                        r = j
        return s[l:r+1]