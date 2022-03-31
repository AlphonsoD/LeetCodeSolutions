# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ### Original solution:
        # dummy = headA
        # seen = set()
        # while (dummy != None):
        #     seen.add(dummy)
        #     dummy = dummy.next
        # dummy = headB
        # while (dummy != None):
        #     if dummy in seen:
        #         return dummy
        #     else:
        #         dummy = dummy.next
        # return None
        
        ### O(1) solution:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a