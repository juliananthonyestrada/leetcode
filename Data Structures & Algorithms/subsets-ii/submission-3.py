class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = []

        def explore(i, subset):

            # reached end of array -> stop exploring
            if i == len(nums):
                subsets.append(subset.copy())
                return 
            
            # take current element
            subset.append(nums[i])
            explore(i+1, subset)

            # find last idx of next unique element
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # dont take current element
            subset.pop()
            explore(i+1, subset)
        
        explore(0, [])
        return subsets