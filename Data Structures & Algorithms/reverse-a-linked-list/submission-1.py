# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        prev = None
        while curr:
            new_head = curr.next
            curr.next = prev
            prev = curr
            curr = new_head
        
        # for last node, new_head is just None,
        # so the head of the reversed list is prev

        return prev
           
        



