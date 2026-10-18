class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        mover = self.trie
        for ch in word:
            if ch not in mover:
                mover[ch] = {}
            mover = mover[ch]
        mover["end"] = True

    def search(self, word: str) -> bool:
        mover = self.trie
        for ch in word:
            if ch not in mover:
                return False
            mover = mover[ch]
        return True if "end" in mover else False

    def startsWith(self, prefix: str) -> bool:
        mover = self.trie
        for ch in prefix:
            if ch not in mover:
                return False
            mover = mover[ch]
        return True        