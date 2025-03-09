class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = []
        visited = set()
        rot = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1: rot += 1
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
        if rot == 0: return 0

        time = 0
        while q:
            for i in range(len(q)):
                x,y = q.pop(0)
                dirs = [[1,0],[0,1],[-1,0],[0,-1]]
                for dx, dy in dirs:
                    dx = x+dx
                    dy = y+dy
                    if (dx,dy) not in visited and 0<=dx<ROWS and 0<=dy<COLS and grid[dx][dy] == 1:
                        q.append((dx,dy))
                        visited.add((dx,dy))
                        rot -= 1
            time += 1


        if rot > 0: return -1
        return time-1
