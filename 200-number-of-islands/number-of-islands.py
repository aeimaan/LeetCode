class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def dfs(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS: return
            if grid[x][y] == "0" or (x,y) in visited: return

            visited.add((x,y))
            dirs = [[1,0] , [0,1] ,[-1,0], [0,-1]]
            for dx,dy in dirs:
                dfs(dx+x, dy+y)
            
            return
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    res += 1
        return res