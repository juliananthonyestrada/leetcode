class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        # begin at root
        node = self.trie       
        # add if needed        
        for ch in word:
            if ch not in node:          
                node[ch] = {}
            # move to next level
            node = node[ch]
        node["end"] = True

    def helper(self, child, word):
        # begin at specified level
        node = child                    
        for i, ch in enumerate(word):
            # regular char, go to next level
            if ch in node:              
                node = node[ch] 
            # wild card
            elif ch == ".":       
                for char_key in node:
                    # skip end
                    if char_key == 'end':
                        continue
                    # recursively search in all of the next level of the nodes of the current level
                    if self.helper(node[char_key], word[i + 1:]):
                        return True
                # wild card fails
                return False
            # char is not in node and not a dot 
            else:
                return False
        # successfully found all the letters -> verify if it marks the end of a word
        return "end" in node

    def search(self, word: str) -> bool:
        return self.helper(self.trie, word)
