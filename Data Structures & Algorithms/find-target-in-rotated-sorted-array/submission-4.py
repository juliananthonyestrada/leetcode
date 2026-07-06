class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # insight: find which half is sorted by comparing extremes to mid
        # then determine if target falls in that sorted range by \
        # comparing it to mid and then extreme 
        
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid 

            # right half is sorted
            if nums[mid] < nums[right]:
                if target < nums[mid]:
                    right = mid
                else:
                    if target > nums[right]:
                        right = mid
                    else:
                        left = mid+1
            # left half is sorted
            else:
                if target > nums[mid]:
                    left = mid+1
                else:
                    if target < nums[left]:
                        left = mid+1
                    else:
                        right = mid
    
        return -1