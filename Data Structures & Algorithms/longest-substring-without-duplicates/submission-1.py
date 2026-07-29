class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        freq = defaultdict(int)
        res = left = right = 0

        while right < length:
            # dupe
            if s[right] in freq:
                # delete from the left until we find the duplicate
                while s[left] != s[right]:
                    del freq[s[left]]
                    left += 1
                # remove the duplicate and advance the left
                del freq[s[left]]
                left += 1
            # no dupe -> keep growing -> update max
            else:
                res = max(res, right-left+1)
            
            # add new element -> check next element
            freq[s[right]] += 1
            right += 1

        
        return res