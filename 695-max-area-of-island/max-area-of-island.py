class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(x,y,visited):
            area = 0
            if x < 0 or x >= ROWS or y < 0 or y >= COLS :
                return 0
            
            if (x,y) in visited or grid[x][y] == 0:
                return 0

            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            area += 1
            visited.add((x,y))

            for x_new, y_new in dirs:
                area += dfs(x_new+x, y_new+y, visited)

            return area

        for x in range(ROWS):
            for y in range(COLS):
                if (x,y) not in visited and grid[x][y] == 1:
                    res = dfs(x,y,visited)
                    max_area = max(max_area, res)

        return max_area