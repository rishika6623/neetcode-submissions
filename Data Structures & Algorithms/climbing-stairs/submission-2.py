class Solution:
    def climbStairs(self, n: int) -> int:
        m = {0:1, 1: 1}

        def withmemo(n, memo):
            if n in memo:
                return memo[n]
            else:
                memo[n] = withmemo(n-2, memo) + withmemo(n-1, memo)
                return memo[n]

        return withmemo(n, m)