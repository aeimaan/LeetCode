class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def dfs(x,y,visited):
            if x < 0 or x >= ROWS or y<0 or y>=COLS:
                return
            if (x,y) in visited or grid[x][y] == "0":
                return

            visited.add((x,y))
            dirs = [ [1,0], [0,1], [-1,0], [0,-1] ]

            for _x, _y in dirs:
                dfs(x + _x, y + _y, visited)
            return

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == "1" and (x,y) not in visited:
                    dfs(x,y,visited)
                    res += 1
        return res