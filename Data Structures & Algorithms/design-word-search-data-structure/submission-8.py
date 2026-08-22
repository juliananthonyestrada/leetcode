class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["end"] = True

    def helper(self, child, word):
        node = child
        for i, ch in enumerate(word):
            if ch in node:
                node = node[ch]
            elif ch == ".":
                for char_key in node:
                    if char_key == 'end':
                        continue
                    if self.helper(node[char_key], word[i + 1:]):
                        return True
                return False
            else:
                return False
        return "end" in node

    def search(self, word: str) -> bool:
        return self.helper(self.trie, word)
