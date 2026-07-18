class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final = []
        for i in nums:
            final.append(i)

        for i in nums:
            final.append(i)
        return final