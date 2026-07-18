class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # new_nums = set(nums)
        # longest = 0

        # for num in nums:
        #     if num-1 in new_nums:
        #         continue
        #     i = num
        #     j = 0
        #     while i in new_nums:
        #         j+=1
        #         i+=1
        #     longest = max(longest, j)
        # return longest
        seen = {}
        longest = 0
        for num in nums:
            if num not in seen:
                seen[num] = seen.get(num-1, 0) + seen.get(num+1, 0) + 1
                seen[num-(seen.get(num-1, 0))] = seen[num]
                seen[num+(seen.get(num+1, 0))] = seen[num]
                longest = max(longest, seen[num])
        return longest
