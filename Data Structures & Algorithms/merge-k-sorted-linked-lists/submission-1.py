# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # first thought / brute force

        # add all elements to a heap
        # then pop everything out of the heap and build a new linked list
        # nlogn

        heap = []
        count = 0

        for l in lists:
            heapq.heappush(heap, [l.val, count, l])
            count += 1

        head = ListNode()
        dummy = head
        
        while heap:
            curr_min = heapq.heappop(heap)[2]
            dummy.next = curr_min
            dummy = dummy.next
            if curr_min.next:
                heapq.heappush(heap, [curr_min.next.val, count, curr_min.next])
                count += 1
        
        return head.next

