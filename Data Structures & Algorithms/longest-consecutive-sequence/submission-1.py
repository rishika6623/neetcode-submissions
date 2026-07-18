class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 in new_nums:
                continue
            i = num
            j = 0
            while i in new_nums:
                j+=1
                i+=1
            longest = max(longest, j)
        return longest
