class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" : return []
        lettersFromNum = {'2': ['a','b','c'], '3':['d','e','f'] , '4':['g','h','i'] , 
        '5':['j','k','l'], '6':['m','n','o'] , '7':['p','q','r', 's'] , '8':['t','u','v'], '9':['w','x','y', 'z']}

        path = ""
        res = []


        def dfs(idx, path):
            if idx >= len(digits):
                res.append(path)
                return
            neighbors = lettersFromNum[digits[idx]]

            for neigh in neighbors:
                dfs(idx+1, path+neigh)
            
            return 

        dfs(0, path)
        return res