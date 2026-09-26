class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_count = {0: 0}
        def coin_func(amount):
            if amount < 0:
                return -1
            if amount in min_count:
                return min_count[amount]
            else:
                num = -1
                for coin in coins:
                    x = coin_func(amount-coin)
                    if x == -1:
                        num = max(num, x)
                    elif num == -1:
                        num = 1 + x
                    else:
                        num = min(num, 1 + x)
                min_count[amount] = num
                return num
        coin_func(amount)
        return min_count[amount]