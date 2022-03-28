class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        
        # longest common prefix is bound by the smallest string, and can have a 
        # possible maximum up to the largest string
        shortest = min(strs)
        longest = max(strs)
        
        for i in range(len(shortest)):
            if shortest[i] != longest[i]:
                break
            prefix += shortest[i]
        
        return prefix