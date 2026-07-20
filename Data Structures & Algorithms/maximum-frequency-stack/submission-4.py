class FreqStack:
    from collections import defaultdict

    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = []
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val]-1 == len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.freq[val]-1].append(val)

    def pop(self) -> int:
        # pop most freq
        res = self.stacks[-1][-1]
        self.stacks[-1].pop()

        # clear out stack 
        if not self.stacks[-1]:
            self.stacks.pop()

        # update freq
        self.freq[res] -= 1        

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()