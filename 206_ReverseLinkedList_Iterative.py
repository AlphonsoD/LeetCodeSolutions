# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        reversedList = ListNode(head.val, None)
        head = head.next
        
        # IDEA: base case for recursive solution?
        while head != None:
            dummy = ListNode(head.val)
            dummy.next = reversedList
            reversedList = dummy 
            head = head.next
            
        return reversedList
            