class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        res = 0
        needed = 1
        while True:
            if n >= needed:
                res += 1
                n -= needed
                needed += 1
            else:
                return res
        