class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                count += 1
            # Case 2: s[i] is guaranteed to be a space if it makes it past the first 'if' statement,
            # so check if the running count is greater than 0 since that means we've already 
            # encountered a word
            elif count > 0:
                break
        return count
        
        ### Original solution: used a flag variable 'foundWordStart', but we acutally don't need to
        # count, foundWordStart = 0, False
        # for explorer in range(len(s)-1, -1, -1):
        #     if s[explorer] != " " and not foundWordStart:
        #         count += 1
        #         foundWordStart = True
        #     elif s[explorer] != " " and foundWordStart:
        #         count += 1
        #     elif s[explorer] == " " and foundWordStart:
        #         break
        # return count