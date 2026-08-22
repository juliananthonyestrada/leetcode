class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def explore(row, col):
            nonlocal cache

            if (row, col) in cache:
                return cache[(row, col)]

            # out of bounds
            if row > m-1 or col > n-1:
                return 0
            # reached destination
            if row == m-1 and col == n-1:
                return 1
            # keep exploring
            cache[(row, col)] = explore(row+1, col) + explore(row, col+1)
            return cache[(row, col)]

        return explore(0,0)
