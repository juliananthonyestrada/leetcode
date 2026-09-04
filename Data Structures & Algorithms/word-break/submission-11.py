class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        slen = len(s)

        cache = {}

        def can_segment(i):
            if i >= slen:
                return True

            if i in cache:
                return cache[i]
            
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    if can_segment(i + len(word)):
                        cache[i] = True
                        return True
                        
            cache[i] = False
            return False
        
        return can_segment(0)