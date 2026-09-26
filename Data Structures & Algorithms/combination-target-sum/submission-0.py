class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def getCombos(i, target, combo):
            if target == 0:
                results.append(combo.copy())
                return
            elif i == len(nums):
                return
            elif nums[i] <= target:
                combo.append(nums[i])
                getCombos(i, target - nums[i], combo)
                combo.pop()

            getCombos(i+1, target, combo)

        getCombos(0, target, [])

        return results


        