class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # XOR produces what bit we need to add to the result
        # AND tells us if there is a carry when we perform the addition
        
        carry = 0
        result = []
    
        a_ptr, b_ptr = len(a)-1, len(b)-1

        # looping conditions -> while both are greater than 0
        while a_ptr >= 0 and b_ptr >= 0:
            # compute result bit 
            result_bit = int(a[a_ptr]) ^ int(b[b_ptr]) ^ carry
            # compute our carry bit
            carry = (int(a[a_ptr]) and carry) or (int(b[b_ptr]) and carry) or (int(a[a_ptr]) and int(b[b_ptr]))
            # add our result
            result.append(str(result_bit))
            # decrement pointers for next computation 
            a_ptr -= 1
            b_ptr -= 1
        
        # check if both strings are fully processed
        while a_ptr >= 0:
            # compute result
            result_bit = int(a[a_ptr]) ^ carry
            # add our result
            result.append(str(result_bit))
            # recompute our carry
            carry = int(a[a_ptr]) and carry
            # decrement that pointer
            a_ptr -= 1
        
        while b_ptr >= 0:
            # compute result
            result_bit = int(b[b_ptr]) ^ carry
            # add our result
            result.append(str(result_bit))
            # recompute our carry
            carry = int(b[b_ptr]) and carry
            # decrement that pointer
            b_ptr -= 1
        
        if carry:
            result.append(str(carry))

        result.reverse()
        return ''.join(result)