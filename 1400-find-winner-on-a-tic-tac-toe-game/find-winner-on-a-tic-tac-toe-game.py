class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        grid = [[0]*n for i in range(n)]

        def checkCol(col, player):
            for i in range(n):
                if grid[i][col] != player:
                    return False
            return True

        def checkRow(row, player):
            for i in range(n):
                if grid[row][i] != player:
                    return False
            return True
        def checkDiag(player):
            for i in range(n):
                if grid[i][i] != player:
                    return False
            return True
        def checkDiag2(player):
            for i in range(n):
                if grid[i][n-1-i] != player:
                    return False
            return True

        
        player = "A"
        for move in moves:
            row, col = move
            grid[row][col] = player

            res = False
            res = checkCol(col, player) or res
            res = checkRow(row, player) or res
            if row == col: res = checkDiag(player) or res
            if row+col == 2:res = checkDiag2(player) or res
            if res:
                return player
            if player == "A": player = "B"
            else: player = "A"
        return "Draw" if len(moves) == 9 else "Pending"

