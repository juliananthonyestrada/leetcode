class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # the longest prefix is only as long as the shortest word
        smallest = float('inf')
        for word in strs:
            if len(word) < smallest:
                smallest = len(word)

        # track the largest prefix
        largest = ""

        # any prefix must be present in the first word - we start with its first letter
        first_word = strs[0]
        i = 0

        # loop only while needed
        while i < smallest:
            for word in strs:
                if first_word[i] != word[i]:
                    return largest
            largest += first_word[i]
            i += 1
        
        return largest
            
