class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.children:
                root.children[word[i]] = Node()
            root = root.children[word[i]]
            
        root.isWord = True
            
    def search(self, word: str) -> bool:
        root = self.root
        for i in range(len(word)):
            if word[i] in root.children:
                root = root.children[word[i]]
                
            else:
                return False
        return root.isWord
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for i in range(len(prefix)):
            if prefix[i] in root.children:
                root = root.children[prefix[i]]

            else:
                return False
        return True
        
        