# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ### Compact recursive version
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        
        ### Iterative version using stack
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return root
        
        ### Original solution
        # if not root or (not root.left and not root.right): 
        #     return root
        # dummy = root.left
        # root.left = root.right
        # root.right = dummy
        # root.left = self.invertTree(root.left)
        # root.right = self.invertTree(root.right)
        # return root
    
        