class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # for each num in nums we have a decision
        # include or leave out

        subsets = []

        def explore(i, subset):
            # reached end of array
            if i == len(nums):
                subsets.append(subset.copy())
                return 
            
            # take 
            subset.append(nums[i])
            explore(i+1, subset)

            # dont take
            subset.pop()
            explore(i+1, subset)

        explore(0, [])
        return subsets
            
