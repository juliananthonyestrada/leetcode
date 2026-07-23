class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [["", 1]]
        num = ""

        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack.append(["", int(num)])
                num = ""
            elif ch == "]":
                substr, freq = stack.pop()
                stack[-1][0] += (substr * freq)
            else:
                stack[-1][0] += ch
        
        return stack[0][0]