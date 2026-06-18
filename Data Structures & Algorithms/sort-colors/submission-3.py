class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, scanner, right = 0, 0, len(nums)-1

        while scanner <= right:
            # encountered a 0 
            if nums[scanner] == 0:
                # move to left
                nums[scanner], nums[left] = nums[left], nums[scanner]
                left += 1
                scanner += 1
            # encountered a 2    
            elif nums[scanner] == 2:
                # move to right
                nums[scanner], nums[right] = nums[right], nums[scanner]
                right -= 1
            # encountered a 1
            else:
                scanner += 1
        print(nums)

                
