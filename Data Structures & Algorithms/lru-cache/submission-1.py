class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = None, None
    
    def move_to_tail(self, key):
            # update pointers
            node = self.cache[key]
            if self.tail == node:
                return
            elif self.head == node:
                self.head = self.head.next

            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = self.tail.next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_tail(key)
            return self.cache[key].val
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_tail(key)
        else:
            if self.size == self.capacity:
                # evict least recently used cache
                k = self.head.key
                if self.head.next:
                    self.head.next.prev = self.head.prev
                if self.head.prev:
                    self.head.prev.next = self.head.next
                del self.cache[k]
                self.head = self.head.next
                self.size -= 1

            if self.size == 0:
                self.head = None
                self.tail = None

            # add to dll
            node = Node(key, value)

            # add/update the map
            self.cache[key] = node
            self.size += 1

            if self.size == 1:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = self.tail.next

            

            