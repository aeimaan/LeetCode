class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = {}
        

        def dfs(amnt):
            if amnt == 0: return 1
            if amnt in dp: return dp[amnt]
            if amnt < 0: return 9999999
            
            minCoins = 9999999
            for x in coins:
                minCoins = min(dfs(amnt - x), minCoins)

            dp[amnt] = 1 + minCoins
            return 1 + minCoins
        

        x = dfs(amount)-1
        if x == 9999999: return -1
        return x

