class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l, r = 0, len(arr)-1
        anchor = float('inf')

        while l <= r:
            m = (l+r)//2
            if arr[m] == x:
                l = m
                break
            elif x > arr[m]:
                l = m + 1
            else:
                r = m - 1
        
        # Clamp `l` so it doesn't go out of bounds if `x` is larger than all elements
        l = min(l, len(arr) - 1)
        
        # Compare `l` and its left neighbor to find the true closest anchor
        if l > 0 and abs(arr[l - 1] - x) <= abs(arr[l] - x):
            anchor = l - 1
        else:
            anchor = l

        l = r = anchor

        while (r-l)+1 < k:
            if r+1 >= len(arr):
                l -= 1
            elif l-1 < 0:
                r += 1
            else:
                if abs(arr[r+1]-x) < abs(arr[l-1]-x):
                    r += 1
                else:
                    l -= 1
        
        return arr[l:r+1]


       






       