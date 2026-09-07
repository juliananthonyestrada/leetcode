import random 
class RandomizedSet:

    def __init__(self):
        self.random_set = {}
        self.arr = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            self.random_set[val] = self.size
            self.arr.append(val)
            self.size += 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            # remove from arr
            idx = self.random_set[val]
            self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
            self.random_set[self.arr[idx]] = idx
            self.arr.pop()
            self.size -= 1
            del self.random_set[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()