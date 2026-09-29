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
        

        res = []
        path = set()

        # node represents the current level/dictionary that we are at
        def dfs(row, col, node):
            if "end" in node:
                res.append(node["end"])
                node.pop("end")

            if (0 <= row < ROWS and 0 <= col < COLS and board[row][col] in node and (row, col) not in path):
                ch = board[row][col]

                path.add((row, col))

                dfs(row+1, col, node[ch])
                dfs(row, col+1, node[ch])
                dfs(row-1, col, node[ch])
                dfs(row, col-1, node[ch])
                
                path.remove((row, col))

                if not node[ch]:
                    node.pop(ch)

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie)

        return list(res)










