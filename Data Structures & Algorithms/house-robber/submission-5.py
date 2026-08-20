class Solution:
    def rob(self, nums: List[int]) -> int:

        # space optimized - we do not need to build all of dp - we only need 2 most recent houses
        
        if len(nums) == 1:
            return nums[0]

        two_away = nums[0]
        one_away = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(one_away, two_away + nums[i])
            two_away = one_away
            one_away = curr
           
        return one_away