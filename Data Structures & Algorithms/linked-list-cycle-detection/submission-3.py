# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # navigate with a fast and slow pointer
        # if there is a cycle, they will eventually meet
        if not head:
            return False
            
        slow, fast = head, head.next

        while head and head.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast and fast.next:
                    fast = fast.next.next
                else:
                    return False
        return False