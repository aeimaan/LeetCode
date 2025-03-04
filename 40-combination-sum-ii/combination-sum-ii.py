class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        memo = {}
        def dfs(idx, val, path):
            if val == target:
                res.append(path.copy())
                return 1
            if val >= target:
                return 0
            
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, val+ candidates[i], path)
                path.pop()
            
            return 

        dfs(0,0,path)
        return res