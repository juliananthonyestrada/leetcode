class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):                          # iterate through array keeping track of idx and val
            checker = target - num                              # calculate the number needed to reach the target sum
            if checker in nums and nums.index(checker) != i:    # if this number is in the array and != to idx
                if nums.index(checker) < i:
                    return (nums.index(checker), i)             # return indices
                else:
                    return (i, nums.index(checker))