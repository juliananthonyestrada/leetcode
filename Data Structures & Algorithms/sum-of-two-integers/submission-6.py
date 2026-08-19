class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # b will represent our carry

        while b != 0:
            # compute all carries for current iteration
            tmp = ((a & b) << 1) & 0xFFFFFFFF
            # compute value (reg addition for current iteration)
            a = (a ^ b) & 0xFFFFFFFF
            b = tmp
        
        # check if negative
        if a >= 0x80000000:
            a = a - 0x100000000

        return a