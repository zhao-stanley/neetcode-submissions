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

        # set the smallest node to be start (default to left)
        if list2.val > list1.val:
            head = list1
            other = list2
        else:
            head = list2
            other = list1
        
        # keep track of the start of the new merged linked list
        merged_start = head
        
        while head.next:
            # next node of the same list as head
            nxt_same = head.next

            # if the node of other list is < next node of current list, change ptr
            if other.val < nxt_same.val:
                head.next = other
                head = other
                other = nxt_same
            else:
                # otherwise, keep progressing ptr in current list
                head = nxt_same
        
        # if excess nodes in other list (they must all be greater), append to the end
        if other:
            head.next = other
        
        return merged_start





            
