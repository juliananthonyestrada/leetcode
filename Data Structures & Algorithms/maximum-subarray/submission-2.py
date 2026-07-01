class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        res = nums[0]   # equal to first element in case all elements are negative

        for n in nums:
            if curr_sum < 0:    # current streak is no longer fruitful
                curr_sum = 0
            curr_sum += n       
            res = max(res, curr_sum)
    
        return res

   