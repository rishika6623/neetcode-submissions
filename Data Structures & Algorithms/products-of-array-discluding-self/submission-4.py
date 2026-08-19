class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        haszero = False
        hasmanyzero = False

        for num in nums:
            if num == 0 and haszero:
                hasmanyzero = True
            elif num == 0:
                haszero = True
            else:
                total *= num
        print(total)
        for i in range(len(nums)):
            if hasmanyzero:
                nums[i] = 0
            elif nums[i] != 0 and haszero:
                nums[i] = 0
            elif not haszero:
                nums[i] = total // nums[i]
            else:
                nums[i] = total

        return nums
        