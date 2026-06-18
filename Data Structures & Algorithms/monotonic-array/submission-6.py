class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        mon_inc, mon_dec = True, True

        i, j = 0, 1

        # iterate over once
        # if at any point the condition is violated
        # swap the boolean
        while j < len(nums):
            if nums[i] > nums[j]:
                mon_inc = False
            elif nums[i] < nums[j]:
                mon_dec = False    
            i += 1
            j += 1

        return mon_inc or mon_dec