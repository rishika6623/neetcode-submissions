class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3

        elems = set()
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
            if count[nums[i]] > majority:
                elems.add(nums[i])
        return list(elems)