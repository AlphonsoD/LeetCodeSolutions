class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        # My original solution -> very inefficient
        numStr = str(x)
        for i in range(len(numStr)):
            if i >= len(numStr) - i - 1:
                return True
            if numStr[i] != numStr[len(numStr)-i-1]:
                return False
        """
        
        """
        # Better string solution: just reverse the string and see if they're equal
        # And note that negative numbers will never be a palindrome
        # Note: (a string)[::-1] reverses a string
        if x < 0:
           return False
        return str(x) == str(x)[::-1]
        """
        
        """
        # One solution without converting to string involves building the new number 
        # in reverse order. Some math notes:
        #     To get the last digit of a number, simply mod with 10
        #         E.g., 123 % 10 = 3
        #     To remove the last digit of a number, floor divide (//) by 10
        #         E.g., 123 // 10 = 12
        if x<0:
		return False

	    inputNum = x
	    newNum = 0
	    while x>0:
		    newNum = newNum * 10 + x%10
		    x = x//10
	    return newNum == inputNum
        """
        
        """
        For the super optimal solution, see here: https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added 
        """
        if x<0 or (x>0 and x%10==0):
            return False
        
        result = 0
        while x > result:
            result = result*10+x%10
            x = x//10
        
        # first case: number is even
        # second case: number is odd (remove the formerly-middle number)
        return True if (x == result or x == result // 10) else False
        
        

        