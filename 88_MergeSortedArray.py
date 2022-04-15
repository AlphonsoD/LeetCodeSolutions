class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        # Handle case when for when n > m, e.g.:
        #   [3,3,5,0,0,0,0,0,0] (m = 3) and [1,2,4,4,5,6] (n=6)
        nums1[:n] = nums2[:n] 
                    