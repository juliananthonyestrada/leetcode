class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Find two numbers in array that when added = target
        # condition i!=j

        # Make one pass through array and compute difference
        # If difference in the array, then return the indices

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums:
                if i != nums.index(difference):
                    return sorted([i, nums.index(difference)])

