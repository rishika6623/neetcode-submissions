class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            best_profit = max(best_profit, prices[i]-buy)
            buy = min(buy, prices[i])
        return best_profit