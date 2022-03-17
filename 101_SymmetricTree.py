# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        # Base Case
        # If they're both None, then they're symmetrical
        if left == None and right == None:
            return True
        # Otherwise, if either left or right (but not both) are None, then they're not symmetrical
        if (left and not right) or (right and not left):
            return False
        
        if left.val == right.val:
            outside = self.isMirror(left.left, right.right)
            inside = self.isMirror(left.right, right.left)
            return outside and inside
        else:
            return False