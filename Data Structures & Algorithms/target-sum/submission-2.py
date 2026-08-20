class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def explore(i, curr_sum):
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            if i == len(nums):
                if curr_sum == target:
                    return 1
                return 0

                   # subtract curr_num                 # add curr num
            dp[(i, curr_sum)] =  (explore(i+1, curr_sum - nums[i])+  
                                  explore(i+1, curr_sum + nums[i]))
                                  
            return dp[(i, curr_sum)]

        return explore(0, 0)
        
