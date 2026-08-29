class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        target = float('inf')

        for i in range(len(nums)):
            if -nums[i] == target:
                continue
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                    saved = nums[j]
                    while j < len(nums) and nums[j] == saved:
                        j += 1
                    k -= 1

                elif nums[j] + nums[k] < target:
                    j += 1

                else:
                    k -= 1

        return triplets