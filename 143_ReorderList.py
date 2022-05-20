# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Better solution: O(1) space
        # Idea:
        #   - Use fast/slow pointer method to find middle
        #   - Reverse second half of the list
        #   - Merge thw two halves to form the solution
        
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge two halfs
        first, second = head, prev #after the above loop completes, second will have been set to null, but prev will be set to the last node in the linked list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        # ORIGINAL SOLUTION
        # O(n) time (I think), but used O(n) space as well
#         dummy = head
#         nodes = []
#         while dummy != None:
#             nodes.append(dummy)
#             dummy = dummy.next
            
#         # edge case: 1 node
#         if len(nodes) == 1:
#             return head
        
#         l, r = 1, len(nodes)-1
#         dummy = head
#         while l < r:
#             dummy.next = nodes[r]
#             dummy.next.next = nodes[l]
#             dummy = dummy.next.next
#             r -= 1
#             l += 1
            
#         if len(nodes) % 2 == 0: # even edge case
#             dummy.next = nodes[r]
#             dummy = dummy.next
#         dummy.next = None