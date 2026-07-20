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

        candidates = defaultdict(int)

        for num in nums:
            candidates[num] += 1
            if len(candidates) > 2:
                for key in list(candidates.keys()):
                    candidates[key] -= 1
                    if candidates[key] == 0:
                        del candidates[key]

        res = []
        for num in candidates:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res

