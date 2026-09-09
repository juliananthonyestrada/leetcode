class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        l, r = 0, 0
        max_freq = 0
        freq = defaultdict(int)

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(freq.values())

            # window became invalid -> shrink
            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1

        return res

# max_freq takes the value that appears most in the entire string, however, what if the string that appears most in the entire string is not at all present in our current substring? is this not an issue? 