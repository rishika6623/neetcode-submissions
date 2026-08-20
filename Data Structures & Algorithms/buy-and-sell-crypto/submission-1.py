class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_price = 0
        curr = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > curr:
                max_price = max(prices[i] - curr, max_price)
            elif prices[i] < curr:
                curr = prices[i]

        return max_price
