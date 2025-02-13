class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        all_island_dirs = set()


        def dfs(x,y, dirs_followed, x_og, y_og):
            if (x,y) in visited or x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0 :
                return 0
            visited.add( (x,y) )
            dirs = [ [0,1], [1,0], [0,-1], [-1,0] ]

            for x_new, y_new in dirs:
                if dfs(x_new+x, y_new+y, dirs_followed, x_og, y_og) == 1:
                    dirs_followed.append((x_new+x - x_og, y_new+y-y_og))
            return 1

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == 1:
                    dirs_followed = []
                    dfs(i,j,dirs_followed, i, j)
                    dirs_followed = str(dirs_followed)
                    if dirs_followed not in all_island_dirs:
                        res += 1
                        all_island_dirs.add(dirs_followed)
        return res
            
