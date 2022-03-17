# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxCount = 1
        return max(maxCount, self.dfs(root.left, maxCount), self.dfs(root.right, maxCount))
        
    def dfs(self, root, maxCount):
        if root is None:
            return 0
        maxCount += 1
        left = max(maxCount, self.dfs(root.left, maxCount))
        right = max(maxCount, self.dfs(root.right, maxCount))
        return max(left, right)