class Solution:
    def scoreOfString(self, s: str) -> int:
        
        i,j = 0, 1
        res = 0

        while j < len(s):
            res += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1
        return res