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
            if s[i] == "I":
                if i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                    res = (res + convert[s[i+1]] - convert[s[i]])
                    i += 1
                else:
                    res += convert[s[i]]
            elif s[i] == "X":
                if i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                    res = (res + convert[s[i+1]] - convert[s[i]])
                    i += 1
                else:
                    res += convert[s[i]]
            elif s[i] == "C":
                if i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                    res = (res + convert[s[i+1]] - convert[s[i]])
                    i += 1
                else:
                    res += convert[s[i]]
            else:
                res += convert[s[i]]
            
            i += 1
            
        return res