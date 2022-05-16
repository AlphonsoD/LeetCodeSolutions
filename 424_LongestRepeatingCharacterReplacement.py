class Solution:
    # O(26*n) = O(n) time
    def characterReplacement(self, s: str, k: int) -> int: 
        counts = {}
        res = 0
        left = 0
        
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            while (right-left+1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            res = max(right-left+1, res)
            
        return res