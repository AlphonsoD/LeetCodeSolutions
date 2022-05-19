class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = 5001
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            minNum = min(minNum, nums[m])
            
            # left less than mid
            if nums[l] <= nums[m]:
                if nums[r] > nums[m]:
                    r = m-1
                else:
                    l = m+1
                    
            # left greater than mid
            else:
                if nums[r] > nums[m]:
                    r = m-1
                else:
                    l = m+1
                
        return minNum
        
        