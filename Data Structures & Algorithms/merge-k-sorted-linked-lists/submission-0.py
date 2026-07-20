# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # first thought / brute force

        # add all elements to a heap
        # then pop everythin out of the heap and build a new linked list
        # nlogn

        heap = []

        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next

        head = ListNode()
        dummy = head
        
        while heap:
            dummy.next = ListNode(val=heapq.heappop(heap), next=None)
            dummy = dummy.next
        
        return head.next

