class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()

        def dfs(x,y, length):
            if length == len(word):
                return True
            if (x < 0 or x>= ROWS or y < 0 or y >= COLS or (x,y) in path or board[x][y] != word[length]):
                return False
            
            path.add((x,y))
            res = False
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]
            for dx,dy in dirs:
                res = res or dfs(x+dx, y+dy, length + 1)

            path.remove((x,y))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False