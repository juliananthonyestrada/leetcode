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
                subsets.append(curr_sub) 
            else:
                dfs(i+1, curr_sub)              # exclude
                dfs(i+1, curr_sub + [nums[i]])  # include
        dfs(0, [])

        return subsets