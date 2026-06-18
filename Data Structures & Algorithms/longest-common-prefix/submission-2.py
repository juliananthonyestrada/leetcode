class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # the longest prefix is only as long as the shortest word
        smallest = float('inf')
        for word in strs:
            if len(word) < smallest:
                smallest = len(word)

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
            
