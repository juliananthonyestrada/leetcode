class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # given an array of length n
        # the largest smallest positive integer is n+1
        # we can take advantage of this by doing 2 things
        # traverse the array
        # if a number is < 0 or > n then we skip it
        # else we put it in its corresponding index

        i, l = 0, len(nums)

        while i < l:
            while nums[i] != i+1:
                # invalid (negative) or out of bounds or num alr in correct place
                if nums[i] < 1 or nums[i] >= l or nums[i] == nums[nums[i]-1]:
                    break 
                # swap
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            i += 1
        
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        
        return l+1