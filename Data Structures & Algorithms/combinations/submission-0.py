class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(arr, curr):
            if curr > n:
                if len(arr) == k:
                    res.append(arr.copy())
                return

            arr.append(curr)
            dfs(arr, curr+1)
            arr.pop()
            dfs(arr, curr+1)
        
        dfs([], 1)

        return res










