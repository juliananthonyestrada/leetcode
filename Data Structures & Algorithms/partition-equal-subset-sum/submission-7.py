class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        target = total // 2
        if total % 2 != 0: return False
        
        cache = {}

        def explore(i, curr_sum):

            if curr_sum == target:
                return True
            elif i == len(nums):
                return target == curr_sum
            elif curr_sum > target:
                return False
            
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            cache[(i, curr_sum)] = (explore(i+1, curr_sum + nums[i]) or explore(i+1, curr_sum))
            return cache[(i, curr_sum)] 
    
        return explore(0, 0)
