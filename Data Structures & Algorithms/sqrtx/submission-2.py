class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x
        elif x == 4:
            return 2

        low, high = 0, x//2

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