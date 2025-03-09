class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        res = []
        visited = set()
        # path = []

        def dfs(x, y, path):
            if (x == 0 or x == ROWS -1 or y ==0 or y == COLS-1) and board[x][y] == "O":
                return False
            if (x,y) in visited or board[x][y] == 'X':
                return True
            visited.add((x,y))
            path.append((x,y))
            dirs = [ [1,0], [0,1], [-1,0], [0,-1] ]
            res = True
            for dx, dy in dirs:
                res = dfs(dx+x, dy+y, path) and res
            
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    path = []
                    if dfs(i,j, path):
                        for x,y in path:
                            board[x][y] = "X"
        