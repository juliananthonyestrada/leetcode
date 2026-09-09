class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # key insight: a window is valid if the window size - the freq of the most common character <= replacements needed
        
        res = 0
        l, r = 0, 0
        max_freq = 0
        freq = defaultdict(int)

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            # window became invalid -> shrink
            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            # string is valid -> keep growing
            res = max(res, r-l+1)
            r += 1

        return res
