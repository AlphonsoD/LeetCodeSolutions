class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sPtr = 0
        for tPtr in range(len(t)):
            if sPtr < len(s) and t[tPtr] == s[sPtr]:
                sPtr += 1
        return sPtr == len(s)
    
        ### Original solution, converting to list and popping front element 
        ###     - I think converting to list takes O(N)
        # s = list(s)
        # for i in range(len(t)):
        #     if s and t[i] == s[0]:
        #         s.pop(0)
        # return (len(s) == 0)