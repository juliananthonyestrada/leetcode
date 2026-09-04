class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l,r) in cache:
                return cache[(l,r)]

            alices_turn = (l % 2 == 0)

            left = piles[l] if alices_turn else 0
            right = piles[r] if alices_turn else 0
            
            cache[(l,r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return cache[(l, r)]

        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > total - alice_score