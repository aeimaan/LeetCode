class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL =0
        resLen = 0
        n = len(s)
        dp = [ [False]*n for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (s[i] == s[j] ) and (j-i+1 <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 >= resLen:
                        resLen = j-i+1
                        resL = i
                    
        return s[resL: resL+resLen]