class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        slen = len(s)
        cache = {}
        
        def segment(i):
            if i == slen:
                return [[]]  
            
            if i in cache:
                return cache[i]
            
            result = []
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    for rest in segment(i + len(word)):
                        result.append([word] + rest)
            
            cache[i] = result
            return result
        
        partitions = segment(0)
        return [" ".join(partition) for partition in partitions]