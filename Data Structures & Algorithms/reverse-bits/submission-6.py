class Solution:
    def reverseBits(self, n: int) -> int:
        
        # convert n to binary
        rep = [0] * 32

        while n > 0:
            i = 0
            # find the largest power of 2 that fits in n
            while n >= (2 ** i):
                i += 1
            # edge case:  n = 1
            if i == 0:
                rep[-1] = 1
            # set corresponding position to 1
            else:
                rep[32 - i] = 1
            # update n by subtracting highest power of 2
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
