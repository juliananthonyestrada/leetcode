class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.curr_char = self.compressed[0]
        self.iter_left = 0
        self.ptr = 0
    
    def load_next(self) -> None:
        self.curr_char = self.compressed[self.ptr]
        self.ptr += 1
        count = 0

        while self.ptr < len(self.compressed) and self.compressed[self.ptr].isdigit():
            count = (count * 10) + int(self.compressed[self.ptr])
            self.ptr += 1
        
        self.iter_left = count

    def next(self) -> str:
        if not self.hasNext():
            return " "
        
        if self.iter_left == 0:
            self.load_next()
       
        self.iter_left -= 1
        return self.curr_char

    def hasNext(self) -> bool:
        return self.ptr < len(self.compressed) or self.iter_left > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
