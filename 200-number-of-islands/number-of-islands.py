class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0

        def dfs(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x,y) in visited or grid[x][y]=="0":
                return
            
            visited.add((x,y))
            dirs = [ [1,0], [-1,0], [0,1], [0,-1]]
            for dx,dy in dirs:
                dx += x
                dy += y
                dfs(dx,dy)

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1" and (x,y) not in visited:
                    count += 1
                    dfs(x,y)


        return count

