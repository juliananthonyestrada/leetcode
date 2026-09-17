class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = curr_sum = 0
        max_sum = float('-inf')

        while r < len(nums):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[r]
            max_sum = max(curr_sum, max_sum)
            r += 1
        return max_sum