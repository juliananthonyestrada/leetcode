class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)

        # dp[i] represents the max amt of money that I can take up until this idx
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + dp[0]

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        
        return max(dp)