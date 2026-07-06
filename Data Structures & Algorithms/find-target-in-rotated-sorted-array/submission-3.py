class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # insight: think about the pointers as markers
        # if mid is greater than left then the left is sorted
        # if the target is greater than mid then it cant be anywhere in the left
        # if the target is less than mid AND less than left then it must be to the right
        # that is the key the AND check 
        
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