class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            curr_sum = 0
            for j in range(i, i+n):
                curr_sum += nums[j%n]
                res = max(res, curr_sum)
                
        return res
            
    