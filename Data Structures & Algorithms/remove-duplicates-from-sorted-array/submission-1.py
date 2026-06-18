class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return len(nums)

        i, j = 0, 1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[j])
            else:
                i += 1
                j += 1
            
        return len(nums)