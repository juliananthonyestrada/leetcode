class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # True - available, False - occupied
        self.slots = [True] * maxNumbers
        self.curr = 0

    def get(self) -> int:
        seen = 0
        while not self.slots[self.curr]:
            self.curr = (self.curr + 1) % len(self.slots)
            seen += 1

            if seen == len(self.slots):
                return -1
        
        self.slots[self.curr] = False
        return self.curr

    def check(self, number: int) -> bool:
        return self.slots[number]

    def release(self, number: int) -> None:
        self.slots[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
