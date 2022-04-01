# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast, prev = head, head, None
        # careful here: we need AND, not OR, because the left while-loop condition is evaluated before the right
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            slow, fast = slow.next, fast.next
        return True
        
        ### Original solution: O(n^2)
        # palindrome = ""
        # while head != None:
        #     palindrome += str(head.val)
        #     head = head.next
        # return palindrome == palindrome[::-1]
    
    