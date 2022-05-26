# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, l, r):
            if l is None and r is None:
                return True
            elif l and r and l.val == r.val:
                left = self.isSame(l.left, r.left)
                right = self.isSame(l.right, r.right)
                return left and right
            return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (self.isSame(root, subRoot)):
            return True
        if root:
            return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))