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
        
        l, r = pivot_index, pivot_index
        while (r-l) + 1 < k:
            if r+1 >= len(arr):
                l-=1
            elif l-1<0:
                r+=1
            else:
                if abs(arr[r+1]-x) < abs(arr[l-1]-x):
                    r+=1
                else:
                    l-=1

        return arr[l:r+1] 