class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def lcs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # no more chrs to parse
            if i == len(text1) or j == len(text2):
                return 0
            # chars differ: skip one char from either string and keep the longer LCS
            elif text1[i] != text2[j]:
                cache[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
            # curr chars are equal - advance both
            else:
                cache[(i, j)] =  1 + lcs(i+ 1, j + 1)
            
            return cache[(i, j)]
        
        return lcs(0, 0)