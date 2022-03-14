# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nodes = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # had to reset nodes because apprently LeetCode doesn't use a new instance of the Solution class for each test
        self.nodes = []
        self.dfs(root)
        return self.nodes
        
    def dfs(self, root: Optional[TreeNode]):
        if root == None:
            return
        self.dfs(root.left)
        self.nodes.append(root.val)
        self.dfs(root.right)