# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue, depth = [root], 1
        while queue:
            level_size = len(queue)
            while level_size != 0 and queue:
                current = queue.pop(0)
                level_size -= 1
                if current and not current.left and not current.right:
                    return depth
                elif current:
                    queue += [current.left, current.right]
            depth += 1
            
        return depth
        