class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        freq = defaultdict(int)
        res = left = right = 0

        while right < length:
            if s[right] in freq:
                # dup
                # delete from the left until 
                while s[left] != s[right]:
                    del freq[s[left]]
                    left += 1
                del freq[s[left]]
                left += 1
            else:
                res = max(res, right-left+1)
            
            freq[s[right]] += 1
            right += 1

        
        return res