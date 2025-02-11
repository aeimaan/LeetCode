class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        
        def dfs(x,y, visited):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x,y) in visited or grid[x][y]=="0":
                return
            
            visited.add((x,y))
            dirs = [ [1,0], [0,1], [-1,0], [0,-1] ]

            for x_new, y_new in dirs:
                dfs(x+x_new, y+y_new, visited)

        
        for x in range(ROWS):
            for y in range(COLS):
                if (x,y) not in visited and grid[x][y] == "1":
                    dfs(x,y,visited)
                    islands += 1

        return islands