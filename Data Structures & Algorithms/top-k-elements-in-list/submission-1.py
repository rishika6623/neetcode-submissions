class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        sorted_nums = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)
        total = []

        for i in range(k):
            total.append(sorted_nums[i][0])

        return total