class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l, r = 0, len(arr) - 1

        pivot_index = 0

        while l < r:
            m = (l+r) // 2

            if arr[m] == x:
                pivot_index = m
                break
            else:
                if x < arr[m]:
                    r = m
                else:
                    l = m+1

                if r == l+1 or r == l:
                    if abs(arr[l] - x) > abs(arr[r] - x):
                        pivot_index = r
                    else:
                        pivot_index = l
                    break
        
        left, right = pivot_index, pivot_index
        while right - left + 1 < k:
            if left == 0:
                right += 1
            elif right == len(arr) - 1:
                left -= 1
            elif x - arr[left - 1] <= arr[right + 1] - x:
                left -= 1
            else:
                right += 1

        return arr[left: right+1] 