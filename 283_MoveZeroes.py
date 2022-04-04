class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1   
                
        ### Original solution, uses extra space
#         if 0 not in nums: return
        
#         # [5,6,0,1,3,0,2,0,4]
#         # use queue to keep track of index that you pass by and will come back to later
#         queue, seenZeros, found = [], 0, False
        
#         # find and move first 0
#         for i in range(len(nums)-1):
#             if found:
#                 temp = nums[i+1]
#                 if temp == 0:
#                     seenZeros += 1
#                     queue.append(i+1)
#                     continue
#                 nums[i+1] = 0
#                 nums[i] = temp
#             elif nums[i] == 0:
#                 seenZeros, found = seenZeros + 1, True
#                 temp = nums[i+1]
#                 nums[i+1] = 0
#                 nums[i] = temp
        
#         while queue:
#             index = queue.pop()
#             for i in range(index-1, len(nums)-1):
#                 temp = nums[i+1]
#                 nums[i+1] = 0
#                 nums[i] = temp