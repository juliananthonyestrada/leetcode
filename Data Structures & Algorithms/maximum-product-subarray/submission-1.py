class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # the maxProduct can come from 2 places
            # the curr number * the smallest product attained 
            # the curr * number times the greatest product attained 
        
        min_seen = 1
        max_seen = 1
        res = max(nums)

        for n in nums:
            tmp = n*max_seen
            max_seen = max(n, tmp, n*min_seen)
            min_seen = min(n, tmp, n*min_seen)
            res = max(res, max_seen)

        return res

               