class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0: return False
        
        cache = {}

        def explore(i, curr_sum):

            # reached end of nums
            if i == len(nums):
                return total // 2 == curr_sum
            elif curr_sum > total:
                return False
            
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            cache[(i, curr_sum)] = (explore(i+1, curr_sum + nums[i]) or explore(i+1, curr_sum))

            return cache[(i, curr_sum)] 
    
        return explore(0, 0)
