# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            left = right = head
            while right is not None:
                if right.val != left.val:
                    left.next = right
                    left = left.next
                right = right.next
            left.next = None
        return head
            