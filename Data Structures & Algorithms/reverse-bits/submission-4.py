class Solution:
    def reverseBits(self, n: int) -> int:
        
        # convert n to binary
        rep = [0] * 32

        while n > 0:
            i = 0
            while n >= (2 ** i):
                i += 1
            # add assignments
            if i == 0:
                rep[-1] = 1
            else:
                rep[len(rep) - i] = 1
            n -= 2 ** (i-1)

        # reverse that list of 
        rep.reverse()

        # compute that new number
        i = 31
        total = 0
        while i >= 0:
            if rep[i]:
                total += (2 ** (31-i))
            i -= 1
        
        return total
