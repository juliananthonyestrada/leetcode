class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sfrequency_map = {}
        tfrequency_map = {}

        for char in s:
           sfrequency_map[char] = s.count(char)
        
        for char in t:
            tfrequency_map[char] = t.count(char)

        if sfrequency_map == tfrequency_map:
            return True
        return False
