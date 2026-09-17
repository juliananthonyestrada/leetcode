from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        l = r = 0
        resL, resR = 0, 0
        res_len = float("inf")
        t_freq = Counter(t)
        need, have = len(t_freq), 0
        window_freq = defaultdict(int)

        while r < len(s):
            # add curr ch and if in t, track in have
            window_freq[s[r]] += 1
            if s[r] in t_freq and window_freq[s[r]] == t_freq[s[r]]:
                have += 1
            # while the window is valid -> update res and shrink
            while have == need:
                if (r-l+1) < res_len:
                    resL = l
                    resR = r
                    res_len = r-l+1
                # if in t, decrement in have
                if s[l] in t_freq and window_freq[s[l]] == t_freq[s[l]]:
                    have -= 1
                window_freq[s[l]] -= 1
                l += 1       
            # not valid, grow
            r += 1
        
        return s[resL:resR+1] if res_len != float("inf") else ""