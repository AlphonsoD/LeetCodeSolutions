# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        def addByLevel(self, root, level, res):
            if root:
                res.setdefault(level, []).append(root.val)
                if root.left:
                    addByLevel(self, root.left, level+1, res)
                if root.right:
                    addByLevel(self, root.right, level+1, res)
        
        addByLevel(self, root, 0, res)
        return(list(res.values()))
        