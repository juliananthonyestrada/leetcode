class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for i in range(32):
            res += 2 ** (32-i-1) if (n & 1) else 0
            n = n>>1

            if n == 0:
                break
        
        return res