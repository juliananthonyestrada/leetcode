class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n 
        trib = [0] * (n+1)
        trib[1], trib[2] = 1, 1

        for i in range(3, n+1):
            trib[i] = trib[i-3] + trib[i-2] + trib[i-1]
        
        return trib[n]