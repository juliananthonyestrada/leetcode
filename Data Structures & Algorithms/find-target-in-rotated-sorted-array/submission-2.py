class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
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