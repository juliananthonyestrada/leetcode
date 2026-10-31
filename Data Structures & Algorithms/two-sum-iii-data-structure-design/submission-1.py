from collections import defaultdict
class TwoSum:
    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        for num in self.counts:
            target = value - num
            if num == target:
                if self.counts[num] >= 2:
                    return True
            elif target in self.counts:
                return True
            
        return False