class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        # implement a trie
        trie = {}
        for word in words:
            mover = trie
            for ch in word:
                if ch not in mover:
                    mover[ch] = {}
                mover = mover[ch]
            mover["end"] = word
        
        print(trie)

        res = set()
        path = set()
        def dfs(row, col, node):
            if "end" in node:
                res.add(node["end"])

            if (0 <= row < ROWS and 0 <= col < COLS and board[row][col] in node and (row, col) not in path):
                path.add((row, col))

                dfs(row+1, col, node[board[row][col]])
                dfs(row, col+1, node[board[row][col]])
                dfs(row-1, col, node[board[row][col]])
                dfs(row, col-1, node[board[row][col]])
                
                path.remove((row, col))
            else:
                return

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie)

        return list(res)










