class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        for i, c in enumerate(s1):
            s1_counts[c] = 1 + s1_counts.get(c, 0)
            
        s2_counts = {}
        l = 0
        for r in range(len(s2)):
            s2_counts[s2[r]] = 1 + s2_counts.get(s2[r], 0)
            
            if s2_counts == s1_counts:
                return True
            
            if s2[r] not in s1_counts:
                s2_counts = {}
                l = r+1
            elif s2_counts[s2[r]] > s1_counts[s2[r]]:
                while s2_counts[s2[r]] > s1_counts[s2[r]]:
                    s2_counts[s2[l]] -= 1
                    l += 1
        
        return False
    
    """
    "contains a permutation": letter count of s2 is <= letter count of s1
    find letter count of s1, compare to s2 on sliding window?
    """