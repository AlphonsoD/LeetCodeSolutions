# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ### Cleaner solution, but same idea; this time, keep track of max as an instance variable
    maxSoFar = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findMaxDepth(root):
            if not root:
                return 0
            left, right = findMaxDepth(root.left), findMaxDepth(root.right)
            self.maxSoFar = max(self.maxSoFar, left+right)
            return 1 + max(left, right)
        findMaxDepth(root)
        return self.maxSoFar
    
    ### Original solution
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def findMaxDepth(root):  
#             if not root:
#                 return 0, 0
#             leftDepth, leftMax = findMaxDepth(root.left)
#             rightDepth, rightMax = findMaxDepth(root.right)
#             return 1 + max(leftDepth, rightDepth), max(leftMax, rightMax, leftDepth+rightDepth)
        
#         leftDepth, leftMax = findMaxDepth(root.left)
#         rightDepth, rightMax = findMaxDepth(root.right)
#         return max(leftDepth, rightDepth, leftDepth+rightDepth, leftMax, rightMax)
        
        
        
        