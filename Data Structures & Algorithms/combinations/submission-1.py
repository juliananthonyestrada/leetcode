class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # for each number 1 - n we have a choice
        # take it or dont take it
        # while we are taking numbers, we need to check if we reach our size limit k
        res = []

        def dfs(curr, arr):
            # at size limit, add to result
            if len(arr) == k:
                res.append(arr.copy())
                return
            
            if curr == n+1:
                return
            
            # take curr element
            arr.append(curr)
            dfs(curr+1, arr)
            # dont take curr element
            arr.pop()
            dfs(curr+1, arr)
        
        dfs(1,[])

        return res