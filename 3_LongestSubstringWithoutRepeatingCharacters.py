class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Faster solution: use two "pointers", one for left position and one for
        # current position, and enumerate
        
        leftPtr = maxCount = 0
        seen = {}
        
        for i, char in enumerate(s):
            if char in seen and leftPtr <= seen[char]:
                # Move left pointer to just after the previously-seen character
                leftPtr = seen[char] + 1
            else:
                maxCount = max(maxCount, i-leftPtr+1)
            seen[char] = i
            
        return maxCount
        
        """
        My original solution (pretty slow since I iterate over the dictionary)
        
        count, maxCount = 0, 0
        seen = dict()
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = i-seen[s[i]]
                seen = {key:val for key,val in seen.items() if val > seen[s[i]]}
                seen[s[i]] = i
                
        return max(count, maxCount)
        """
        
