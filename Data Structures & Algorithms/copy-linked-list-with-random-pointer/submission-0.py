"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # edge case, empty list
        if not head:
            return
        
        # track the randoms
        maps = {}

        # create a dummy to traverse the list 
        traversing = head

        # create our new head for the copy
        deep_copy = Node(traversing.val, traversing.next, None)
        maps[traversing] = deep_copy

        # create a dummy to traverse new list
        dc = deep_copy

        # move to next untraversed node
        traversing = traversing.next
        
        # traverse the list by following the next pointers
        while traversing:
            dc.next = Node(traversing.val, traversing.next, None)
            maps[traversing] = dc.next
            traversing = traversing.next
            dc = dc.next
        
        traversing = head
        dc = deep_copy
        while traversing:
            if traversing.random:
                dc.random = maps[traversing.random]
            dc = dc.next
            traversing = traversing.next

        return deep_copy
        