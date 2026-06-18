class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # work right to left

        hashmap = {i-1: chr(64 + i) for i in range(1, 27)}
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            res.append(hashmap[columnNumber % 26])
            columnNumber = columnNumber // 26

        return ''.join(reversed(res))