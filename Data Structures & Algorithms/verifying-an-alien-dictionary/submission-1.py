class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # to check if two words are sorted 
        # go letter by letter
        dictionary = {ch:i for i, ch in enumerate(order)}

        def valid(w1, w2):
            i = j = 0

            # traverse until we reach the end of the shorter words
            while i < len(w1) and j < len(w2):
                # violation
                if dictionary[w1[i]] > dictionary[w2[j]]:
                    return False
                # equal -> check next letter
                elif dictionary[w1[i]] == dictionary[w2[j]]:
                    i += 1 
                    j += 1
                # validated
                else:
                    return True
            # only triggers if all equal 
            return len(w1) <= len(w2)
            
        # check adjacent pairs
        for idx in range(1, len(words)):
            if not valid(words[idx-1], words[idx]):
                return False
        return True
