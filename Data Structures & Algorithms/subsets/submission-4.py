class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # for each element n in nums we have a decision
        # do we include n in this subset: yes or no
        # this naturally forms a tree 
    
        

        l = len(nums)
        subset, subsets = [], []

        def dfs(i):
            if i == l:
                subsets.append(subset.copy()) 
            else:
                # include
                subset.append(nums[i])
                dfs(i+1)    
                # exclude
                subset.pop()
                dfs(i+1)            


        dfs(0)

        return subsets