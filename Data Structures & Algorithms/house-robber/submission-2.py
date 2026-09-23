class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def rob_recurse(i):
            if i >= len(nums):
                return 0
            elif i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + rob_recurse(i+2), rob_recurse(i+1))
                return memo[i]

        return rob_recurse(0)
        