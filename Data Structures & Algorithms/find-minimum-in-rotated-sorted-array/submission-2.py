class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            # we know that nums[l] is greater to everything to the right of m
            if nums[l] > nums[m]:
                # bc of this, it is safe to bring r down to m
                r = m
            # we know that everything to the left and including 
            # m is greater than everything to the right of m
            elif nums[m] > nums[r]:
                # they cannot be the minimum and it is safe to bring l to m+1
                l = m+1
            # if we enter here then the array is sorted 
            else:
                # we return the leftmost element
                return nums[l]
        
        # Note: we do not get an infinte loop because a single element
        # is already sorted and therefore we return it in the else block
        
        