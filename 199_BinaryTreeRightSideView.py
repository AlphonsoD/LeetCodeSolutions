# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, queue = [], [root]
        
        while queue:
            queueLength = len(queue)
            rightSide = None
            
            for i in range(queueLength):
                node = queue.pop(0)
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
            
        return res