class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = set([n for n in nums if n > 0])

        res = 1

        while True:
            if res in nums:
                res += 1
            else:
                return res
        
        
       