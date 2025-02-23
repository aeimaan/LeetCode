class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def isPalindrome(s):
            l  = 0
            r = len(s) -1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

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
