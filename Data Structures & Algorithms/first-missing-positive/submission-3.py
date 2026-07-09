class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i, l = 0, len(nums)

        while i < l:
            while nums[i] > 0 and nums[i] <= l:
                if (nums[i] == i+1) or (nums[i] == nums[nums[i]-1]):
                    break
                nums[nums[i] - 1], nums[i]  = nums[i], nums[nums[i] - 1]        
            i += 1

        for i, n in enumerate(nums):
            if i+1 != n:
                return i+1
            elif i+1 == l:
                return l+1