class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def differs_by_one(word1: str, word2: str) -> bool:
            found_diff = False
            w1_ptr, w2_ptr = 0, 0

            while w1_ptr < len(word1) and w2_ptr < len(word2):
                # differing ch
                if word1[w1_ptr] != word2[w2_ptr]:
                    # more than 1
                    if found_diff:
                        return False
                    else:
                        found_diff = True
                w1_ptr += 1
                w2_ptr += 1
            return found_diff

        # word : neighbors
        adj = {word : [] for word in wordList}
        adj[beginWord] = []

        for key_word in adj:
            for other_word in wordList:
                if differs_by_one(key_word, other_word):
                    adj[key_word].append(other_word)
        
        # bfs to find shortest path from beginWord to endWord
        sequence = 1
        seen = set()
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                seen.add(curr)

                if curr == endWord:
                    return sequence
                
                for nghb in adj[curr]:
                    if nghb not in seen:
                        q.append(nghb)
            sequence += 1

        return 0












