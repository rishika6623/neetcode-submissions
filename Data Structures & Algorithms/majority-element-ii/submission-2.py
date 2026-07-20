class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3 + 1
        final = set()

        #obvious sol
        # elems = set()
        # count = defaultdict(int)
        # for i in range(len(nums)):
        #     count[nums[i]] += 1
        #     if count[nums[i]] > majority:
        #         elems.add(nums[i])
        # return list(elems)

        #sort and then o(1) space

        #only two numbers max can be in the final array
        for j in range(len(nums)):
            i = j
            left_to_find = majority
            if nums[j] in final:
                continue

            if len(final) == 2:
                return list(final)

            while i <= len(nums) - left_to_find:
                #print(left_to_find, i, j, nums[i], nums[j], final)
                if nums[i] == nums[j]:
                    left_to_find -= 1
                    if left_to_find == 0:
                        final.add(nums[i])
                        break
                i += 1
        return list(final)

