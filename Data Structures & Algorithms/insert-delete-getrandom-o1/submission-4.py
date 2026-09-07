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

            idx_to_remove = self.random_set[val]
            last = self.arr[-1]

            # swap to end and pop for constant time removal
            last, self.arr[idx_to_remove] = self.arr[idx_to_remove], last
            
            # update idx of what was the last element
            self.random_set[self.arr[idx_to_remove]] = idx_to_remove

            self.arr.pop()
            del self.random_set[val]

            self.size -= 1

            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()