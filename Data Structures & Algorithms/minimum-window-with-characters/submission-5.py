from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Brute force - O(n^2) - build every substring and take the smallest that has every char of t
        # Case sensitive - upper and lower matters
        # optimal - O(n) - sliding window 

        t_freq = Counter(t)
        window_freq = defaultdict(int)

        l = r = 0
        resL, resR = 0, 0
        res_len = float("inf")
        need, have = len(t_freq), 0

        while r < len(s):

            window_freq[s[r]] += 1
            if s[r] in t_freq and window_freq[s[r]] == t_freq[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < res_len:
                    resL = l
                    resR = r
                    res_len = r-l+1

                if s[l] in t_freq and window_freq[s[l]] == t_freq[s[l]]:
                    have -= 1
                window_freq[s[l]] -= 1
                l += 1       

            r += 1
        
        return s[resL:resR+1] if res_len != float("inf") else ""