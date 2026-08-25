class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = []

        def explore(i, subset):

            # reached end of array -> stop exploring
            if i == len(nums):
                if subset.copy() not in subsets:
                    subsets.append(subset.copy())
                return 
            
            # take current element
            subset.append(nums[i])
            explore(i+1, subset)

            # dont take current element
            subset.pop()
            explore(i+1, subset)
        
        explore(0, [])
        return subsets