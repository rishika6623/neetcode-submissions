class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
        print(num_count)
        often_list = sorted(list(num_count.items()), key=lambda x: x[1], reverse=True)
        print(often_list)
        final = []
        for i in range(k):
            final.append(often_list[i][0])
        return final