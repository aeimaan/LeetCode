class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def dfs(x, y, visited, prev):
            if x <0 or x >= ROWS or y <0 or y>= COLS or (x,y) in visited:
                return 
            cur = heights[x][y]
            if cur < prev:
                return 
            visited.add((x,y))
            dirs = [ [1,0], [0,1], [-1,0], [0,-1] ]
            for dx, dy in dirs:
                dfs(x+dx, y+dy, visited, heights[x][y])
            return

        for i in range(COLS):
            dfs(0,i, pacific, heights[0][i])
            dfs(ROWS-1, i, atlantic, heights[ROWS-1][i])
        for i in range(ROWS):
            dfs(i, 0 , pacific, heights[i][0])
            dfs(i, COLS-1, atlantic, heights[i][COLS-1])

        for t in pacific:
            if t in atlantic:
                res.append(t)
        return res
        