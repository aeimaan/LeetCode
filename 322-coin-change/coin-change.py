class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(remain):
            if remain == 0: return 0
            if remain in dp: return dp[remain]
            if remain < 0: return float('inf')

            coinsNeeded = float('inf')
            for x in coins:
                coinsNeeded = min(coinsNeeded, dfs(remain - x) + 1)

            dp[remain] = coinsNeeded
            return coinsNeeded

        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res