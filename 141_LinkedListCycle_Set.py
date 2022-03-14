# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # idea: store nodes we've seen in a dictionary?
        tracker = set()
        if head == None or head.next == None:
            return False
        else:
            while head.next != None:
                if head in tracker:
                    return True
                else:
                    tracker.add(head)
                    head = head.next