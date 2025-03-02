class Solution:
    def longestPalindrome(self, s: str) -> str:
        resl = 0
        resr = 0
        resLen = resr-resl+1
        n = len(s)
        dp = [ [False]*n  for i in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (s[i] == s[j]) and ( j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    curLen = j-i+1
                    if curLen >= resLen:
                        resLen = curLen
                        resl = i 
                        resr = j

        return s[resl: resl+resLen]