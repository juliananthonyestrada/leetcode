class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # for each element n in nums we have a decision
        # do we include n in this subset: yes or no
        # this naturally forms a tree 
    
        if not nums:
            return nums

        l = len(nums)
        subsets = []
        def dfs(i, curr_sub):
            if i == l:
                subsets.append(curr_sub.copy()) 
            else:
                # include
                curr_sub.append(nums[i])
                dfs(i+1, curr_sub.copy())    
                # exclude
                curr_sub.pop()
                dfs(i+1, curr_sub.copy())            


        dfs(0, [])

        return subsets