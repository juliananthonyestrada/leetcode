class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        mini = float('inf')

        if target in nums:
            return 1

        left = right = 0

        while right < len(nums):
            if sum(nums[left:right+1]) >= target:
                mini = min(mini, right-left+1)
                left += 1
            else:
                right += 1
        
        return mini if mini != float('inf') else 0
                