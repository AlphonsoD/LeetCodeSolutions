# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
        
        # Original solution: not bad, but uses O(N) space and can be more efficient
#         fast = slow = head
#         nodes = list()
#         while fast:
#             slow = slow.next
#             nodes.append(fast)
#             if fast.next:
#                 nodes.append(fast.next)
#                 fast = fast.next.next
#             else:
#                 break
        
#         count = len(nodes)
#         index = count - n
        
#         if index > 0 and n != 1:
#             nodes[index-1].next = nodes[index+1]
#             nodes[index].next = None
#             return head
#         elif len(nodes) == 1:
#             return None
#         elif index == 0:
#             nodes[0].next = None
#             return nodes[1]
#         elif n == 1:
#             nodes[count-2].next = None
#             return head
        
        
        