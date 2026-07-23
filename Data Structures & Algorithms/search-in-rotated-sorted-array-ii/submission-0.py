class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True

            # this half is sorted
            if nums[l] < nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m
                else:
                    l = m+1

            # right half is sorted
            elif nums[l] > nums [m]:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r=m

            else:
                l += 1

        return False
            

        