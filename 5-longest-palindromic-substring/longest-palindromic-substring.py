class Solution:
    def longestPalindrome(self, s: str) -> str:
        resl=0
        resr = 0
        maxlen = 0
        n = len(s)
        dp = [[False]*n for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                    continue
                
                if (s[i] == s[j]) and (j-i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if maxlen < (j-i+1):
                        maxlen = j-i+1
                        resl = i
                        resr = j
        return s[resl:resr+1]