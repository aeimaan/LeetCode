class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []


        def backtrack(cur_sum, target, i):
            if cur_sum == target:
                res.append(path.copy())
                return
            if cur_sum > target or i > len(candidates):
                return
            
            # recurse on the elements
            for i in range(i, len(candidates)):
                path.append(candidates[i])
                backtrack( cur_sum + candidates[i], target, i )
                path.pop()
        
        backtrack(0,target,0)
        return res