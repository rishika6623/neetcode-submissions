class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0]*len(height)
        suff = [0]*len(height)
        
        left, right = 0, len(height) - 1

        for i in range(1, len(height)):
            pref[i] = max(pref[i-1], height[left])
            suff[len(height)-1-i] = max(suff[len(height) - i], height[right])
            right -= 1
            left += 1

        total = 0

        print(pref, suff)
        for i in range(len(height)):
            total += max(0, min(pref[i], suff[i]) - height[i])

        return total