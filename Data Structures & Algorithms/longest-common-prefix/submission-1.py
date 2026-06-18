class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        smallest = float('inf')
        for word in strs:
            if len(word) < smallest:
                smallest = len(word)

        # edge case - single word
        if len(strs) == 1:
            return strs[0]

        largest = ""
        first_word = strs[0]
        i = 0

        while i < smallest:
            curr_prefix = first_word[i]
            for word in strs:
                if curr_prefix != word[i]:
                    return largest
            largest += curr_prefix
            i += 1
        
        return largest
            
