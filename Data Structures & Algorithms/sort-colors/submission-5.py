class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # key insight, we are not sorting numbers, we are arranging classes
        # we do not use direct comparison on numerical values and instead
        # tackle case by case

        # we must begin scanner at 0 unless we risk not processing the first element

        # we cannot increment scanner after encountering a 2 becuase we must process the elementthat 
        # was just placed at the scanners position (from the right position)

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

                
