class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # first thought is a freq map and a sliding window
        # added insight: have the window be of a fixed size
            # there is no need to allow it to expand or shrink to a size it cannot be

        # build a frequency map
        freq = {}
        for char in s1:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        # check if the current window is a permutation
        def check_window(sub):
            for char in sub:
                if char not in s1:
                    return False
                elif sub.count(char) != freq[char]:
                    return False
            return True

        # check all possible windows
        left, right = 0, len(s1)-1
        while right < len(s2):
            if check_window(s2[left:right+1]):
                return True
            left += 1
            right += 1
        
        return False