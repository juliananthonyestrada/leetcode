# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # find left
        before_left, curr = None, head
        for _ in range(left-1):
            before_left = curr
            curr = curr.next
        
        tail = curr

        # reverse up until right
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # connect new head with old list
        if before_left:
            before_left.next = prev    
        
        tail.next = curr

        return prev if left == 1 else head
        
