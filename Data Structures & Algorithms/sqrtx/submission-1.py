class Solution:
    def mySqrt(self, x: int) -> int:
        
        low, high = 0, x

        while low <= high:
            mid = (low + high) // 2
            square = mid*mid

            if square == x:
                return mid
            elif square > x:
                high = mid - 1
            else:
                low = mid + 1
        
        return high