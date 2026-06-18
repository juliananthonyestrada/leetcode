class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i, j = 0, len(nums)-1

        while i <= j:
            pos = (i+j)//2

            if nums[pos] == target:
                return pos
            elif nums[pos] < target:
                i = pos + 1
            else:
                j = pos - 1
        
        return i

