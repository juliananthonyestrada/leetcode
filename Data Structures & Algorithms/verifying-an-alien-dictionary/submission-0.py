class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # to check if two words are sorted 
        # go letter by letter
        dictionary = {ch:i for i, ch in enumerate(order)}

        def valid(w1, w2):
            i = j = 0

            while i < len(w1) and j < len(w2):
                if dictionary[w1[i]] > dictionary[w2[j]]:
                    return False
                elif dictionary[w1[i]] == dictionary[w2[j]]:
                    i += 1 
                    j += 1
                else:
                    return True
            
            return len(w1) <= len(w2)
            
        for idx in range(1, len(words)):
            if not valid(words[idx-1], words[idx]):
                return False
        return True
