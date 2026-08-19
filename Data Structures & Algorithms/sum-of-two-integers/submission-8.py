class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # we must manually enforce that our variables stay within 32 bit ints
        # bc python integers can grow 'arbitrarily'

        while b != 0:
            # compute all carries for current iteration
            tmp = ((a & b) << 1) & 0xFFFFFFFF
            # compute value (reg addition for current iteration)
            a = (a ^ b) & 0xFFFFFFFF
            b = tmp
        
        # check if negative (0x80000000 is the 32nd bit so if a is >= it should be neg)
        if a >= 0x80000000:
            a = a - 0x100000000

        return a