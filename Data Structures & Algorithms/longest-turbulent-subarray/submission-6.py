class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        res = 1
        l, r = 0, 0
        prev, curr = None, None
        
        while r < len(arr):
            if arr[r-1] < arr[r]:
                curr = "<"
            elif arr[r-1] > arr[r]:
                curr = ">"
            else:
                curr = "="

            if curr == "=":
                l = r
                r += 1
                prev = None
                continue
            elif prev is None or curr != prev:   # first element OR valid alternation
                r += 1
            else:                                # curr == prev → streak broken
                l = r-1
                r += 1                        # current pair might start a new run arr[i-1], arr[i] form a valid pair, size = 2
            
            prev = curr
            res = max(res, r-l)

        return res
                        
            
                