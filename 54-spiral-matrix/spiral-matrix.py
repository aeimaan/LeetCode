class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
         dirs = [ [0,1], [1,0], [0,-1], [-1,0] ]
         res = []
         visited = set()
         ROWS = len(matrix)
         COLS = len(matrix[0])

         if ROWS == 1:
            return matrix[0]


         def visitedAllNeighbors(x,y):
            for dx,dy in dirs:
                dx = x + dx
                dy = y + dy
                if not checkBounday(dx,dy):
                    continue
                if (dx, dy) not in visited:
                    return False
            return True

         def checkBounday(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                return False
            if (x,y) in visited:
                return False
            return True

         def dfs(x, y, i):
            res.append(matrix[x][y])
            if visitedAllNeighbors(x,y):
                return
            visited.add((x,y))
            dx,dy = dirs[i]
            if not checkBounday(x+dx, y+dy):
                i = (i+1) % len(dirs)
                dx,dy = dirs[i]
            dfs(x+dx, y+dy, i)
            return

         dfs(0,0,0)
         return res
