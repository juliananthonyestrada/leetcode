# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # navigate with a fast and slow pointer
        # if there is a cycle, they will eventually meet

        # edge case: empty list
        if not head:
            return False

        # initialize slow pointers
        slow, fast = head, head.next


        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
            
        return False