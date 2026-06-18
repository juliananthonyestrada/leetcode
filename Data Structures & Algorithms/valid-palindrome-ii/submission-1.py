class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left <= right:
            # they match - keep scanning
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        
        while left <= right:
            # they match - keep scanning
            if s[left] == s[right]:
                left += 1
                right -= 1
            # they do not match 
            else:
                # we must check two cases
                # sub starting at left and sub starting at left+1 (ending at right)
                print("helper")
                return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1])
        
        return True