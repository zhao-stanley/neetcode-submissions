# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        

        if list2.val > list1.val:
            head = list1
            other = list2
        else:
            head = list2
            other = list1
            
        merged_start = head
        
        while head.next:
            # next node of the same list as head
            nxt_same = head.next

            if other.val < nxt_same.val:
                head.next = other
                head = other
                other = nxt_same
            else:
                head = nxt_same
        
        if other:
            head.next = other
        
        return merged_start





            
