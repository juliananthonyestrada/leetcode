# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # find left
        before_left, curr = ListNode(0, head), head
        for _ in range(left-1):
            before_left = curr
            curr = curr.next
        
        # beginning of portion that we are reversing -> after reversing, will be the tail
        tail = curr

        # reverse up until right
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # connect new head with old list -> edge case where before left is None bc left=1
        before_left.next = prev    
        tail.next = curr

        return before_left.next if left == 1 else head
        
