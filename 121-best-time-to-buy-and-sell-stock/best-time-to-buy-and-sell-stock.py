class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        l =0 
        r = 1

        while r < len(prices):
            profit = max(profit, prices[r]- prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return profit