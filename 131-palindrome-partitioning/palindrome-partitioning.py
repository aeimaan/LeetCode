class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def isPalindrome(s):
            return s == s[::-1]

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i: j+1]):
                    partition.append(s[i: j+1])
                    dfs(j+1)
                    partition.pop()

        dfs(0)
        return res
