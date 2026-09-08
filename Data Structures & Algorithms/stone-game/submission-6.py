class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        cache = {}

        def dfs(l, r):

            # all stones processed
            if r < l:
                return 0 
            
            if (l,r) in cache:
                return cache[(l,r)]
            
            # every time alice chooses there is an even # of piles
            alices_turn = 1 if (r-l+1) % 2 == 0 else 0

            # alice can take from the left or the right
            left = piles[l] if alices_turn else 0
            right = piles[r] if alices_turn else 0

            cache[(l,r)] = max(left + dfs(l+1, r), right + dfs(l, r-1)) 
            return cache[(l,r)]    

        total = sum(piles)
        alice = dfs(0, len(piles)-1) 
        return alice > total - alice