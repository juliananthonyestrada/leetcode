class FreqStack:
    from collections import defaultdict

    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(list)
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        # pop most freq
        key = max(self.stacks.keys())
        res = self.stacks[key][-1]
        self.stacks[key].pop()

        # update freq
        self.freq[res] -= 1

        # clear out stack 
        if not self.stacks[key]:
            del self.stacks[key]

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()