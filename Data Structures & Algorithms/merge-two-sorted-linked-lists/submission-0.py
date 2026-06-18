# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         
        dummy = ListNode()              # initialize a dummy head
        curr = dummy                    # the current position is the dummy head

        while list1 and list2:          # while both lists have nodes
            if list1.val < list2.val:   # if the val at L1 < L2 
                curr.next = list1       # add this node to the merged iist
                list1 = list1.next      # move to the next node in L1 (so we can compare with curr node of L2)
            else:
                curr.next = list2       # if the val at L2 < L1 add this node to the merged list
                list2 = list2.next      # move to the next node in L2
            curr = curr.next            # regardless of which node gets added -> move to the next position in the merged list

        if list1:                       # if there are remaining elements in L1
            curr.next = list1           # add the remaining list to the merged list
        elif list2:                     # if there are remaining elements in L2
            curr.next = list2           # add the remaining list to the merged list
        
        return dummy.next               # return the head of the merged list

        