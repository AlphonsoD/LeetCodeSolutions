# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Account for special case where head = []
        if head == None:
            return None
        
        # Base case
        if head.next == None:
            return head
        
        # Main idea: reverse head.next (i.e., the rest of the linked list), then correct the pointers
        if head.next:
            reversedList = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            
        return reversedList