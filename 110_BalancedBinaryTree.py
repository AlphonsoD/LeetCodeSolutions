# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        else:
            return max(left, right) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1
    
    ### First approach, brute force: NOT EFFICIENT since we're checking nodes that we've already checked
#     def height(self, root):
#         if not root:
#             return 0
#         left = self.height(root.left)
#         right = self.height(root.right)
#         return max(left, right) + 1
    
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         left = self.height(root.left)
#         right = self.height(root.right)
#         return abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
        