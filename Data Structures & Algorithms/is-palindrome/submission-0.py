class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        reverse = []
        original = []

        for char in range(len(s) -1, -1, -1):
            if s[char].isalnum():
                reverse.append(s[char].upper())

        for char in range(len(s)):
            if s[char].isalnum():
                original.append(s[char].upper())

        print(original)
        print(reverse)

        if original == reverse:
            return True
        else:
            return False

