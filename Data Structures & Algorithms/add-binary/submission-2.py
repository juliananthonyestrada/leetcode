class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # XOR produces what bit we need to add to the result
        # AND tells us if there is a carry when we perform the addition
        
        carry = 0
        result = []
    
        a_ptr, b_ptr = len(a)-1, len(b)-1

        # while there are bits to process
        while a_ptr >= 0 or b_ptr >= 0:
            # handle for different length strings by validating current position
            bit_a = int(a[a_ptr]) if a_ptr >= 0 else 0
            bit_b = int(b[b_ptr]) if b_ptr >= 0 else 0
            # compute result bit 
            result_bit = bit_a ^ bit_b ^ carry
            # compute our carry bit
            carry = (bit_a and carry) or (bit_b and carry) or (bit_a and bit_b)
            # add our result
            result.append(str(result_bit))
            # decrement pointers for next computation 
            a_ptr -= 1
            b_ptr -= 1
        
        # add last carry if needed
        if carry:
            result.append(str(carry))

        result.reverse()
        return ''.join(result)