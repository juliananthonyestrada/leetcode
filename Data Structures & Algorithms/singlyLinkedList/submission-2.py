class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        i = 0
        dummy = self.head

        while i < index:
            dummy = dummy.next
            i += 1
        
        return dummy.val

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            tmp = self.head
            self.head = Node(val)
            self.head.next = tmp
        
        self.length += 1

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False

        i, prev, curr = 0, None, self.head

        while i < index:
            prev = curr
            curr = curr.next
            i += 1
        
        # removing head
        if index == 0:
            self.head = self.head.next
        # removing tail
        elif index == self.length - 1:
            self.tail = prev
            self.tail.next = None
        # removing middle
        else:
            prev.next = curr.next

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        dummy = self.head

        while dummy:
            values.append(dummy.val)
            dummy = dummy.next
        
        return values
