class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i, j, count = 0, 0, 0

        while i < len(word) and j < len(abbr):

            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False

                strt = j
                while j+1 < len(abbr) and abbr[j+1].isdigit():
                    j += 1
                
                num = int(''.join(abbr[strt:j+1]))
                count += num
                i += num
                j += 1
            else:
                if word[i] != abbr[j]:
                    return False
                
                i += 1
                j += 1
                count += 1
        
        return i == len(word) and j == len(abbr)
