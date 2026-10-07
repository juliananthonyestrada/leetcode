class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)
        
        print(self.word_indices)

    def shortest(self, word1: str, word2: str) -> int:
        min_dist = float("inf")
        word1_ptr, word2_ptr = 0, 0
        word1_indices, word2_indices = self.word_indices[word1], self.word_indices[word2]

        while word1_ptr < len(word1_indices) and word2_ptr < len(word2_indices):
            min_dist = min(min_dist, abs(word1_indices[word1_ptr] - word2_indices[word2_ptr]))

            if word1_indices[word1_ptr] < word2_indices[word2_ptr]:
                word1_ptr += 1
            else:
                word2_ptr += 1

        return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
