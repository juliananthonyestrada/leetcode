class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        size, res = 1, 1
        prev, curr = None, None
        
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                curr = "<"
            elif arr[i-1] > arr[i]:
                curr = ">"
            else:
                curr = "="

            if curr == "=":
                size = 1
                prev = None
                continue
            elif prev is None or curr != prev:   # first element OR valid alternation
                size += 1
            else:                                # curr == prev → streak broken
                size = 2                         # current pair might start a new run arr[i-1], arr[i] form a valid pair, size = 2
            
            prev = curr
            res = max(res, size)

        return res
                        
            
                