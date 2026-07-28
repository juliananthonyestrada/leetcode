class Solution:
    def romanToInt(self, s: str) -> int:
        
        convert = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
    
        i, res = 0, 0
    
        while i < len(s):
            if i+1 < len(s) and convert[s[i]] < convert[s[i+1]]:
                res = (res + convert[s[i+1]] - convert[s[i]])
                i += 2
            else:
                res += convert[s[i]]            
                i += 1
            
        return res