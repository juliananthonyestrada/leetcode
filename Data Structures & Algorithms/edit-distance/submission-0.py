class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # 1-indexed
        # dp[i][j] represents the minimum distance to get from word1[i] -> word2[j]

        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        # to get from an empty word1 to word2[j] we insert all letters
        for j in range(len(word2)+1):
            dp[0][j] = j
        
        # to get from word1[i] to an empty word2 we delete all letters
        for i in range(len(word1)+1):
            dp[i][0] = i

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        return dp[-1][-1]
        
        