# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Improved solution:
            - Use while loop and account for None values inside (use default values like val1 = 0, for example)
        """
        result = dummy = ListNode()
        carry = 0
        
        # 
        while l1 or l2:
            val1, val2 = 0, 0
            if l1:
                val1, l1 = l1.val, l1.next
            if l2:
                val2, l2 = l2.val, l2.next
            val = val1 + val2 + carry
            dummy.next = ListNode(val%10)
            dummy, carry = dummy.next, val//10
            
        if carry > 0:
            dummy.next = ListNode(carry)
            
        return result.next
        
"""
Original solution; still works, but has a lot of repeated code
"""
#         traverseList = ListNode()
#         sumList = traverseList
#         carry = 0
        
#         traverseList.val = l1.val + l2.val
#         if traverseList.val > 9:
#             carry = traverseList.val // 10
#             traverseList.val = traverseList.val % 10
#         else:
#             carry = 0
#         l1 = l1.next
#         l2 = l2.next
        
#         while l1 != None and l2 != None:
#             sumVal = l1.val + l2.val + carry
#             if sumVal > 9:
#                 carry = sumVal // 10
#                 sumVal = sumVal % 10
#             else:
#                 carry = 0
#             traverseList.next = ListNode(sumVal)
#             traverseList = traverseList.next
#             l1 = l1.next
#             l2 = l2.next
            
#         if l1 is None and l2 is not None:
#             while l2 is not None:
#                 sumVal = l2.val + carry
#                 if sumVal > 9:
#                     carry = sumVal // 10
#                     sumVal = sumVal % 10
#                 else:
#                     carry = 0
#                 traverseList.next = ListNode(sumVal)
#                 traverseList = traverseList.next
#                 l2 = l2.next
                
#         if l2 is None and l1 is not None:
#             while l1 is not None:
#                 sumVal = l1.val + carry
#                 if sumVal > 9:
#                     carry = sumVal // 10
#                     sumVal = sumVal % 10
#                 else:
#                     carry = 0
#                 traverseList.next = ListNode(sumVal)
#                 traverseList = traverseList.next
#                 l1 = l1.next
        
#         if carry > 0:
#             traverseList.next = ListNode(carry)
            
#         return sumList

