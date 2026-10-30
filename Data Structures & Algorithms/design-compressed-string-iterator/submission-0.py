class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.char = self.compressed[0]
        self.iter_left = 0
        self.bound = len(self.compressed)

        self.ptr = 1
        while self.ptr < self.bound and self.compressed[self.ptr].isdigit():
            self.iter_left = (self.iter_left * 10) + int(self.compressed[self.ptr])
            self.ptr += 1

    def next(self) -> str:
        if self.hasNext():
            if self.iter_left == 0:
                self.char = self.compressed[self.ptr]
                self.ptr += 1
                while self.ptr < self.bound and self.compressed[self.ptr].isdigit():
                    self.iter_left = (self.iter_left * 10) + int(self.compressed[self.ptr])
                    self.ptr += 1
                    
            self.iter_left -= 1
            return self.char
        else:
            return " "

    def hasNext(self) -> bool:
        return self.ptr < self.bound or self.iter_left > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
