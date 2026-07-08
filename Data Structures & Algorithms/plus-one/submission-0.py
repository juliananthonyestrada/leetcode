class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # case: no carry
        if digits[-1] != 9:
            digits[-1] += 1
        # carry
        else:
            ptr = len(digits) - 1
            while ptr > -1 and digits[ptr] == 9:
                digits[ptr] = 0
                ptr -= 1
            
            if ptr == -1:
                digits.insert(0, 1)
            else:
                digits[ptr] += 1

        return digits
