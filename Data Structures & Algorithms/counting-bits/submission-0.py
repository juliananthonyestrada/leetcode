class Solution:
    def countBits(self, n: int) -> List[int]:
        
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