# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        
        else:
            result = dummy = ListNode()
            
            # MISTAKE: Check list1/2, NOT list1/2.next!
            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next
                
            if list1 != None:
                dummy.next = list1
            if list2 != None:
                dummy.next = list2
                
            return result.next
            