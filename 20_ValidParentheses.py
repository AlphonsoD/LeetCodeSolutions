class Solution:
    def isValid(self, s: str) -> bool:
        b = list(s)
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bracket in b:
            # (Dictionary 'in' checks keys, not values)
            # If there is something in the stack, the bracket is a closing one, and the top
            # of the stack is the corresponding open bracket, then remove from stack
            if stack and (bracket in pairs and pairs[bracket] == stack[-1]):
                stack.pop()
            # Otherwise, add to stack
            else:
                stack.append(bracket)
            
        if len(stack) > 0:
            return False
        else:
            return True
            