class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # declare pointers at both ends
        left = 0
        right = len(nums) - 1

        # while there are numbers to check
        while left <= right:

            # bisect the array
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # target not in nums
        return -1