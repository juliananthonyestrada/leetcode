class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        # maintain record as a stack 
        record = []

        for op in operations:
            if op == "+":
                num1, num2 = record.pop(), record.pop()
                record.append(num2)
                record.append(num1)
                record.append(num1 + num2)
            elif op == "D":
                record.append(2*record[-1])
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)