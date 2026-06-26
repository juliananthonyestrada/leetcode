class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # XOR operator returns 1 iff bits are differnet
        # The XOR operator is commutative and associative 
        # Any number XOR with itself returns 0
        # Any number XOR with 0 returns that number

        res = 0

        for n in nums:
            res ^= n
        
        return res