class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0

        # AND returns true iff both bits are 1
        # n&1 therefore returns true if and only if the last bit is 1, else 0
        # Right Slide moves all bits one position to the right, dropping any that fall off

        while n != 0:
            counter += n&1

            n >>= 1
        
        return counter