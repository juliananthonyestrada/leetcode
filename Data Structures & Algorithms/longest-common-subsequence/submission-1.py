class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def lcs(i1, i2):
            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if i1 == len(text1) or i2 == len(text2):
                return 0
            elif text1[i1] != text2[i2]:
                cache[(i1, i2)] = max(lcs(i1 + 1, i2), lcs(i1, i2 + 1))
            else:
                cache[(i1, i2)] =  1 + lcs(i1+ 1, i2 + 1)
            
            return cache[(i1, i2)]
            
        
        return lcs(0, 0)