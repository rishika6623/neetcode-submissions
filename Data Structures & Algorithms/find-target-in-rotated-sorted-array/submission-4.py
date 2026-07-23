class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m
                else:
                    l = m+1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m+1
                else:
                    r = m
        return -1