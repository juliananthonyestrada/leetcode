class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # we are checking bit by bit, the last 1, one at a time
        # 01 and n returns 1 if the last bit is a 1 and 0 other wise
        # >> 1 pushes everything to the right, allowing a new bit to be checked

        output = [0] * (n+1)

        def count_1s(n: int) -> int:
            counter = 0
            
            while n != 0:
                counter += n&1

                n >>= 1
            
            return counter

        for i in range(n+1):
            output[i] = count_1s(i)
        
        return output