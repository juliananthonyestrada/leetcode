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

    def search(self, word: str, node=None) -> bool:
        curr = node if node else self.root  # edge case for 1st call -> default val is None
        for i, c in enumerate(word):
            if c == ".":
                return any(self.search(word[i+1:], child) for child in curr.children.values())
            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
