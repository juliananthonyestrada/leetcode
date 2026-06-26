class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0

        for _ in range(32):
            counter += n&1

            n >>= 1
        
        return counter