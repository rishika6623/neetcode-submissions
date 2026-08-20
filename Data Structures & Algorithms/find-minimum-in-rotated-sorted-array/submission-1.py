class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) -1

        while low <= high:
            print(nums[low:high+1])
            mid = (low + high) // 2

            if nums[low] > nums[mid]:
                high = mid

            elif nums[mid] > nums[high]:
                low = mid+1

            else:
                return nums[low]
        
        #return nums[low]