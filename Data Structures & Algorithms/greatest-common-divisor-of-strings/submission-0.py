class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        res, pfx = 0, 1

        # case: equal strings
        if str1 == str2:
            return str2
        
        # assign roles
        if len(str1) < len(str2):
            smaller, larger = str1, str2
        else:
            smaller, larger = str2, str1
        
        # check all prefixes
        while pfx <= len(smaller):
            # valid prefix size     
            if len(smaller) % pfx == 0 and len(larger) % pfx == 0:
                # produces correct strings
                if smaller[0:pfx] * (len(smaller) // pfx) == smaller and smaller[0:pfx] * (len(larger) // pfx) == larger:
                    res = max(pfx, res)
            pfx += 1

        return smaller[0:res]