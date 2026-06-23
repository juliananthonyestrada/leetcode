# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find mid point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # head of second half
        midpoint = slow.next

        # cut off first half
        slow.next = None

        # reverse second half
        prev, curr = None, midpoint
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # the head of the newly reversed second half is now held by prev
        dummy = head
        second_head = prev

        while second_head and dummy:
            # store next pointers
            main_tmp = dummy.next
            second_tmp = second_head.next
            # update next pointers 
            dummy.next = second_head
            second_head.next = main_tmp
            # move to next set of nodes to update
            dummy = dummy.next.next
            second_head = second_tmp

        
       