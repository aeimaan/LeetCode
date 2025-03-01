class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = ""
        res = []

        def dfs(opened, closed, path):
            if len(path) == 2*n:
                res.append(path)
                return

            if opened < n:
                dfs(opened+1, closed, path + '(')
            if closed < opened:
                dfs(opened, closed+1, path + ')')
            return
        dfs(0,0, path)
        return res