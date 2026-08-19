class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dict = {to find:match index}
        match = {}
        for i in range(len(nums)):
            if nums[i] in match:
                return [match[nums[i]], i]
            match[target - nums[i]] = i

