class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        result = []
        
        def backtrack(currentIndex, currentString):
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            
            for character in mapping[digits[currentIndex]]:
                backtrack(currentIndex + 1, currentString + character)
                
        if digits:
            backtrack(0, "")
            
        return result
        