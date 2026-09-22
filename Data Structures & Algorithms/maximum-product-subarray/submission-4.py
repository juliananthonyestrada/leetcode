class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # the maxProduct can come from 2 places
            # the curr number * the smallest product attained 
            # the curr * number times the greatest product attained 
        
        min_seen = 1
        max_seen = 1
        dp = [nums[0]] * (len(nums)+1)

        for i, n in enumerate(nums):
            tmp = n*max_seen
            max_seen = max(n, tmp, n*min_seen)
            min_seen = min(n, tmp, n*min_seen)
            dp[i] = max(max_seen, dp[i-1])
        
        return max(dp)

               