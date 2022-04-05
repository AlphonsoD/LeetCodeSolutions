class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        elif len(needle) > len(haystack): return -1
        else:
            left, right = 0, len(needle)
            for i in range(len(haystack)):
                if haystack[left:right] == needle:
                    return left
                else:
                    left, right = left+1, right+1
            return -1