class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new = Node(value)
        tmp = self.tail.prev
        self.tail.prev = new
        new.next = self.tail
        tmp.next = new
        new.prev = tmp
        self.size += 1

    def appendleft(self, value: int) -> None:
        new = Node(value)
        tmp = self.head.next
        self.head.next = new
        new.next = tmp
        tmp.prev = new
        new.prev = self.head
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        res = self.tail.prev.val
        tmp = self.tail.prev.prev
        self.tail.prev = self.tail.prev.prev
        tmp.next = self.tail
        self.size -= 1
        return res

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        res = self.head.next.val
        tmp = self.head.next.next
        self.head.next = self.head.next.next
        tmp.prev = self.head
        self.size -= 1
        return res

