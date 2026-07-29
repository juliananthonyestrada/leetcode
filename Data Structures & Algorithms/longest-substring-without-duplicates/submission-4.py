class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        seen = set()
        res = left = right = 0

        while right < length:
            if s[right] in seen:
                # remove elements until we take out the duplicate
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

            res = max(res, right-left+1)
            seen.add(s[right])
            right += 1

        
        return res