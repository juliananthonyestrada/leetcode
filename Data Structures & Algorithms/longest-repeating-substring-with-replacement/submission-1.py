class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        char_set = set(s)

        for ch in char_set:
            l = count = 0
            for r in range(len(s)):
                if s[r] == ch:
                    count += 1
                
                # while the window is not valid
                while (r - l + 1) - count > k:
                    if s[l] == ch:
                        count -= 1
                
                    l += 1
                
                res = max(res, r-l+1)
            
        return res
