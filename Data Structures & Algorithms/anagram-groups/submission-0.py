class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            curr = tuple(sorted(s))
            if curr in anagrams:
                anagrams[curr].append(s)
            else:
                anagrams[curr] = [s]
        
        return list(anagrams.values())