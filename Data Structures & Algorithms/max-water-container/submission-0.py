class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        best_area = 0
        while start < end:
            best_area = max(best_area, (end-start) * (min(heights[start], heights[end])))
            if heights[start] > heights[end]:
                end -=1
            else:
                start +=1
        return best_area