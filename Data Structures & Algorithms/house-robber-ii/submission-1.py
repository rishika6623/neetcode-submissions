class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_dp(nums, i, seen):
            if i == len(nums):
                return 0
            elif i == len(nums) - 1:
                return nums[i]
            elif i in seen:
                return seen[i]
            else:
                seen[i] = max(nums[i] + rob_dp(nums, i+2, seen), rob_dp(nums, i+1, seen))
                return seen[i]
    
        return max(rob_dp(nums[0:len(nums)-1], 0, {}), rob_dp(nums[1:], 0, {}))