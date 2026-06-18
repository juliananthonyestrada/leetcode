class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # basically just sort the array in place

        # start at first index, scan whole array, find the smallest value, swap

        length = len(nums)

        for i in range(length):
            j = i+1
            for j in range(length):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

