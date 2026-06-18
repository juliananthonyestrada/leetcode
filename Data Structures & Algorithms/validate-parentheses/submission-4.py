class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        matching_characters = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for char in s:
            if char in matching_characters.keys():
                stack.append(char)
            else:
                if stack == [] or matching_characters[stack.pop()] != char:
                    return False
        
        if stack == []:
            return True
        else:
            return False