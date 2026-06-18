class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # work right to left

        hashmap = {i: chr(64 + i) for i in range(1, 27)}
        hashmap[0] = "Z"
        res = []

        while columnNumber > 0:
            res.append(hashmap[columnNumber % 26])
            if columnNumber == 26:
                columnNumber = 0
            columnNumber = columnNumber // 26

        return ''.join(reversed(res))