class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []
        
        def backtrack(leftCount, rightCount):
            if leftCount == rightCount == n:
                result.append("".join(stack))
                return
            
            if leftCount < n:
                stack.append("(")
                backtrack(leftCount+1, rightCount)
                stack.pop()
                
            if rightCount < leftCount:
                stack.append(")")
                backtrack(leftCount, rightCount + 1)
                stack.pop()
                
        backtrack(0, 0)
        return result