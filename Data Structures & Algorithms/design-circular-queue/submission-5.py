class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head, self.tail = None, None

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        else:
            node = Node(value)
            # begin our list
            if self.size == 0:
                self.head = self.tail = node
                self.size += 1
            # append to end 
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = self.tail.next
                node.next = self.head
                self.head.prev = node
                self.size += 1 
        
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            # clear our list
            if self.size == 1:
                self.head = self.tail = None
                self.size -= 1
            # remove some node in the middle
            else:
                tmp = self.head.next
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = tmp
                self.size -= 1
            return True

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()