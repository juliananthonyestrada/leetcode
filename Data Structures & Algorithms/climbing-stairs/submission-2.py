class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(curr):
            if curr in cache:
                return cache[curr]

            if curr == n:
                return 1
            elif curr > n:
                return 0
            
            cache[curr] = dfs(curr+1) + dfs(curr+2)
            return cache[curr]

        return dfs(0)



















