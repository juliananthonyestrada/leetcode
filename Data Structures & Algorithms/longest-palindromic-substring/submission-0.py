class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the issue is that we never update start
        start, res_len = 0, 0

        def lp(mid):   
            nonlocal res_len
            nonlocal start

            # longest palindromic substring of even size
            l, r = mid, mid + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            even = r-l-1
            if even > res_len:
                start = l+1
                res_len = even

            # longest palindromic substring of odd size
            l = r = mid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            odd = r-l-1
            if odd > res_len:
                start = l+1
                res_len = odd

        for i in range(len(s)):
            lp(i)

        return s[start : start+res_len]