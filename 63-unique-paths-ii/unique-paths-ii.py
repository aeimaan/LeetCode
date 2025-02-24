class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        memo = {}

        def dfs(x,y):
            if x>= ROWS or y>= COLS or obstacleGrid[x][y] ==1:
                return 0
            if (x,y) in memo:
                return memo[(x,y)]
            if x == ROWS-1 and y == COLS-1:
                return 1

            ways = dfs(x+1, y) + dfs(x, y+1)
            memo[(x,y)] = ways
            return ways

        return dfs(0,0)
