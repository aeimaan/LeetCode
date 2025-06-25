class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        n = len(word)
        visited = set()
        dirs = [ [1,0], [0,1], [-1,0], [0,-1] ]

        def dfs(x,y,idx):
            if idx >= n: return True
            if (x,y) in visited: return False
            if x < 0 or x >= ROWS or y < 0 or y >= COLS: return False
            if board[x][y] != word[idx]: return False
            visited.add((x,y))
            for dx,dy in dirs:
                if dfs(dx+x, dy+y, idx+1):
                    return True
            visited.remove((x,y))
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i,j,0): return True
        return False
            














        # ROWS = len(board)
        # COLS = len(board[0])
        # path = set()

        # def dfs(x,y, length):
        #     if length == len(word):
        #         return True
        #     if (x < 0 or x>= ROWS or y < 0 or y >= COLS or (x,y) in path or board[x][y] != word[length]):
        #         return False
            
        #     path.add((x,y))
        #     res = False
        #     dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        #     for dx,dy in dirs:
        #         res = res or dfs(x+dx, y+dy, length + 1)

        #     path.remove((x,y))
        #     return res

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c]==word[0] and dfs(r,c,0):
        #             return True
        # return False