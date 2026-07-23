class Solution:
    def decodeString(self, s: str) -> str:
        nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        def build(curr, freq):
            res = []
            s = ''.join(curr)

            for _ in range(int(freq)):
                res.append(s)

            return ''.join(res)

        i = 0  
        stack = []

        while i < len(s):
            if s[i] == "]":
                curr = []
                # take all elements to repeat
                while stack[-1] != "[":
                    curr.append(stack.pop())
                # remove open bracket
                stack.pop()
                freq = stack.pop()
                stack.append(build(curr, freq))     
                i += 1       
            elif s[i] in nums:
                num = []
                while s[i] in nums:
                    num.append(s[i])
                    i += 1
                stack.append(''.join(num))
            else:
                stack.append(s[i])
                i += 1
        
        res = []

        for s in stack:
            res.append(s[::-1])
        
        return ''.join(res)