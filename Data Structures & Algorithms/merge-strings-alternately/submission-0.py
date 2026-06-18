class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = j = 0
        res = [] # does maintianing an array to avoid constant new string objects make it better for cache

        while i < len(word1) and j < len(word2):
            # append both characters
            res.append(word1[i])
            res.append(word2[j])
            
            # move to next character
            i += 1
            j += 1

        # word1 is larger
        if len(word1) > len(word2):
            # append the rest
            while i < len(word1):
                res.append(word1[i])
                i += 1
        # word 2 is larger
        elif len(word2) > len(word1):
            # append the rest
            while j < len(word2):
                res.append(word2[j])
                j += 1

        return ''.join(res)
