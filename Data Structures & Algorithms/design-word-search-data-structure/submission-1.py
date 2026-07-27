class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def helper(self, root, word):
        for i, c in enumerate(word):   
            if c == ".":
                for child in root.children.values():
                    if self.helper(child, word[i+1:]):
                        return True
                return False 
            elif c not in root.children:
                return False
            root = root.children[c]
        return root.word

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            if c == ".":
                for child in curr.children.values():
                    if self.helper(child, word[i+1:]):
                        return True
                return False
            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
