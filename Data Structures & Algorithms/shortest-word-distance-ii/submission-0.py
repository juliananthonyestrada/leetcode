class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)
        
        print(self.word_indices)

    def shortest(self, word1: str, word2: str) -> int:
        min_dist = float("inf")

        for i in self.word_indices[word1]:
            for j in self.word_indices[word2]:
                min_dist = min(min_dist, abs(i-j))
        
        return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
